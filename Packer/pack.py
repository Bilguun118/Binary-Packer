import const
import lief
import time

# Binary Pack хийх класс
class BinPack(object):
    
    # Байгуулагч функц
    def __init__(self, args):
        self.args = args
    
    # def align(self, var, align):
    #     if var % align == 0:
    #         return var
    #     else:
    #         return var - (var % align) + align

    # def pad_data(packed_data, file_align):
    #     return packed_data + ([0] * (self.align(len(packed_data), file_align) - len(packed_data)))

    # Command Line-д өгөгдсөн утгийг хүлээж аван python кодод унших функц
    def open_bin_dat(self):
        data = open(self.args.input, const.READBIN)
        bytesdata = data.read()
        return bytesdata
    
    # def unpack_bin_dat(self):
    #     pack_data = self.open_bin_dat(self)
    #     unpack_PE = lief.PE.parse(self.args.p)
    #     file_alignment = unpack_PE.optional_header.file_alignment
    #     section_alignment = unpack_PE.optional_header.section_alignment
    #     packed_data = list(pack_data)
    #     packed_data = self.pad_data()

# Программын нэр болон тайлбарыг эхлэлд хэвлэх 
def PrintBeginning():
    print("Binary File Packer --------------------")
    print("Application Name: ", const.APPLICATIONNAME)
    time.sleep(1.5)
    return