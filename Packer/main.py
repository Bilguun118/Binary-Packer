import os
import argparse
import lief
import encoding
import const
import pack


if __name__=="__main__":
    parser = argparse.ArgumentParser(description=".NET PE Binary Packer")
    parser.add_argument('input', metavar="FILE", help='input file')
    # parser.add_argument('-p', metavar='UNPACKER', help='unpacker.exe', required=True)
    # parser.add_argument('-o', metavar="FILE", help='output', default="packed.exe")
    args = parser.parse_args()
    pack.PrintBeginning()
    BinObject = pack.BinPack(args)
    BinObject.open_bin_dat()
    # ReadData, sectiondata = BinObject.read_bin_data()
    # sectiondata = open("CompressTest.txt", "r")
    # data = sectiondata.read()
    # compressed_data, tree = encoding.Encoding(data)
    # sectiondata.close()
    # print("Encode хийж шахсан өгөгдөл")
    # print("-"*100)
    # print(compressed_data)
    # print("-"*100)
    # # BinObject.build_bin_dat(ReadData, str(sectiondata))
    # uncompressed_data = encoding.Decoding(compressed_data, tree)
    # print("Decode хийсэн өгөгдөл")
    # print(uncompressed_data)
    # print("-"*100)