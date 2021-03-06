using System;
using System.Diagnostics.CodeAnalysis;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Runtime.InteropServices;

namespace BinPack.Runtime
{
    [SuppressMessage("ReSharper", "InconsistentNaming")]
    internal unsafe class PeSectionLoader
    {
        #region File Header Structures

        // Grabbed the following definition from http://www.pinvoke.net/default.aspx/Structures/IMAGE_SECTION_HEADER.html

        [StructLayout(LayoutKind.Explicit)]
        [SuppressMessage("ReSharper", "FieldCanBeMadeReadOnly.Local")]
        private struct IMAGE_SECTION_HEADER
        {
            [FieldOffset(0)] public fixed byte Name
                [8];
            [FieldOffset(12)] public uint VirtualAddress;
            [FieldOffset(16)] public uint SizeOfRawData;
            [FieldOffset(36)] private uint Characteristics;
        }

        #endregion File Header Structures


        private static void Main(string[] args)
        {
            // Call GetHINSTANCE() to obtain a handle to our module
            byte* basePtr = (byte*) Marshal.GetHINSTANCE(Assembly.GetCallingAssembly().ManifestModule);

            byte* ptr = basePtr;
            // Parse PE header using the before obtained module handle
            // DOS Header толгой файлаас  e_lfanew утгийг уншиж авах.
            ptr += *(ushort*) (ptr + 0x3C);

            // File Header толгой файлаас NumberOfSections утгийг уншиж авах
            ushort NumberOfSections = *(ushort*) (ptr + 0x6);

            ushort optHeaderSize = *(ushort*) (ptr + 0x14);

            ptr += 0x18 + optHeaderSize;

            // Section толгой файлыг уншиж хувьсагчид хадгалах
            var ImageSectionHeaders = new IMAGE_SECTION_HEADER[NumberOfSections];
            for (int headerNo = 0;
                headerNo < ImageSectionHeaders.Length;
                headerNo++)
            {
                ImageSectionHeaders[headerNo] = *(IMAGE_SECTION_HEADER*) ptr;
                ptr += sizeof(IMAGE_SECTION_HEADER);
            }

            // EntryPoint-ын нэрийг авах
            string name = Assembly.GetCallingAssembly().EntryPoint.Name;

            // PE Section буюу хэсэг бүрэлдэхүүн тус бүрд давтах
            foreach (var section in ImageSectionHeaders)
            {
                // Section name буюу хэсгийн нэр EntryPoint Stub-ын эхний 8 байттай таарж байгаа эсэхийг шалгана.
                bool flag = true;
                for (int h = 0; h < 8; h++)
                    if (name[h] != *(section.Name + h))
                        flag = false;

                if (flag)
                {
                    // Raw өгөгдлийн хэмжээтэй buffer хувьсагч үүсгэнэ.
                    byte[] buffer = new byte[section.SizeOfRawData];
                    basePtr += section.VirtualAddress;
                    // Binary файлын section хэсгийг буффер-руу бичих ба Deflate алгоритмаар шахаж XOR алгоритмаар нууцласан өгөгдлийг decode хийж авна.
                    fixed (byte* p = &buffer[0])
                    {
                        for (int i = 0; i < buffer.Length; i++)
                        {
                            *(p + i) = (byte) (*(basePtr + i) ^ name[i % name.Length]);
                        }
                    }

                    // Decompress data from the buffer
                    using var origin = new MemoryStream(buffer);
                    using var destination = new MemoryStream();
                    using var deflateStream = new DeflateStream(origin, CompressionMode.Decompress);
                    deflateStream.CopyTo(destination);

                    // Load assembly using the previously decompressed data
                    var asm = Assembly.Load(destination.GetBuffer());

                    MethodBase entryPoint = asm.EntryPoint ??
                                            throw new EntryPointNotFoundException(
                                                "BinPacker could not find a valid EntryPoint to invoke");
                    ;
                    object[] parameters = new object[entryPoint.GetParameters().Length];
                    if (parameters.Length != 0)
                        parameters[0] = args;
                    entryPoint.Invoke(null, parameters);
                }
            }
        }
    }
}