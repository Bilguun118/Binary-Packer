using System;
using System.IO;
using BinPack.Packers;


namespace BinPack
{
    // Классын нэр
    internal static class Program
    {
        // Программын Main функц
        private static void Main(string[] args)
        {
            // Оюутны код
            Console.WriteLine("BinPacker - B180970400 \r\n");
            if (args.Length == 0)
            {
                Console.WriteLine("Usage: BinPack.exe <file>");
                Console.ReadKey();
                return;
            }

            // Binary файлын замын утгийг хувьсагчид хадгалах.
            string file = args[0];

            // Binary файл байгаа эсэхийг шалгах
            if (!File.Exists(file))
                throw new FileNotFoundException($"Could not find file: {file}");

            // .exe өргөтгөлтэй эсэхийг шалгах
            if (Path.GetExtension(file) != ".exe")
                throw new InvalidDataException("BinPack only supports .net executable files");

            // Binary файлыг (System.IO.File) классын (ReadAllBytes) функцийг ашиглан (byte) төрлөөр уншиж аван хувьсагчид хадгалах.
            byte[] InputData = File.ReadAllBytes(file);
            // Pack хийгдсэн binary файлыг өмнө байсан замд _binpacked нэрийг залгаж буцаан хадгалах.
            string outputPath = file.Insert(file.Length - 4, "_binpacked");
            
            // Packer нэртэй объект үүсгэх
            IPacker packer;
            if (args.Length > 1)
            {
                throw new InvalidProgramException("Number of Arguments are greater than expected");
            }
            else
            {
                // Binary файлыг хүлээж авах (SectionPacker) классын объектыг үүсгэж binary өгөгдлийг дамжуулна.
                packer = new SectionPacker(InputData, outputPath);
            }

            // packer объектын функцыг дуудаж ажилуулах.
            packer.Execute();

            // Pack хийгдсэн файлын замыг дэлгэцэд хэвлэх
            Console.WriteLine("Packed Binary File: {0}", outputPath);
            // Терминалын өнгийг ногоон болгох
            Console.ForegroundColor = ConsoleColor.Green;
            // Программ дууссан гэх мессежийг терминалруу хэвлэх
            Console.WriteLine("Finished Return");

            Console.ReadKey();
        }
    }
}