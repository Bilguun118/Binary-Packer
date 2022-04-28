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
    ReadData = BinObject.open_bin_dat()
    compressed_data, tree = encoding.Encoding(ReadData)
    print(compressed_data)
    uncompressed_data = encoding.Decoding(compressed_data, tree)
    print(uncompressed_data)