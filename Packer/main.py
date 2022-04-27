import os
import argparse
import lief
import encoding
import const


if __name__=="__main__":
    # parser = argparse.ArgumentParser(description=".NET PE Binary Packer")
    # parser.add_argument('input', metavar="FILE", help='input file')
    # parser.add_argument('-p', metavar='UNPACKER', help='unpacker.exe', required=True)
    # parser.add_argument('-o', metavar="FILE", help='output', default="packed.exe")
    # args = parser.parse_args()
    BinObject = BinaPack()