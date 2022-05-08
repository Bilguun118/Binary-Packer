using System;
using System.IO;
using BinPack.Packers;

// Namespace Of Programm
namespace BinPack
{
    // Class Name
    internal static class Program
    {
        // Main Function of Programm
        private static void Main(string[] args)
        {
            Console.WriteLine("BinPacker - B180970400 \r\n");
            if (args.Length == 0)
            {
                Console.WriteLine("Usage: BinPack.exe <file>");
                Console.ReadKey();
                return;
            }

            string file = args[0];

            if (!File.Exists(file))
                throw new FileNotFoundException($"Could not find file: {file}");
 
            if (Path.GetExtension(file) != ".exe")
                throw new InvalidDataException("BinPack only supports .net executable files");

            // Pack хийх binary файлын замийг болон output path-ыг программ хүлээн авах.
            byte[] payloadData = File.ReadAllBytes(file);
            string outputPath = file.Insert(file.Length - 4, "_binpacked");
            
            IPacker packer;
            if (args.Length > 1)
            {
                throw new InvalidProgramException("Number of Arguments are greater than expected");
            }
            else
            {
                packer = new SectionPacker(payloadData, outputPath);
            }

            // Run packer
            packer.Execute();


            Console.WriteLine("Packed Binary File: {0}", outputPath);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Finished Return");

            Console.ReadKey();
        }
    }
}