from lief import PE
import const
import lief
import time
import pefile
import pydasm
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
        pe = pefile.PE(self.args.input)
        for section in pe.sections:
            print(section.Name, hex(section.VirtualAddress),
            hex(section.Misc_VirtualSize), section.SizeOfRawData )
        pe.parse_data_directories()

        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            print(entry.dll)
            for imp in entry.imports:
                print('\t', hex(imp.address), imp.name)
        ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        ep_ava = ep+pe.OPTIONAL_HEADER.ImageBase
        data = pe.get_memory_mapped_image()[ep:ep+100]
        offset = 0
        while offset < len(data):
          i = pydasm.get_instruction(data[offset:], pydasm.MODE_32)
          print(pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, ep_ava+offset))
          offset += i.length
    
    def build_bin_dat(self, bin_data, section):
        packed_binary = PE.Binary("C:/Users/Bilguun/Desktop/NewPacked.exe", PE.PE_TYPE.NET)
        section_text = PE.Section(".text")
        data = list(map(ord, section))
        section_text.content = data
        section_text.virtual_address = 0x1000
        builder = lief.PE.Builder(packed_binary)
        builder.build_imports(True)
        builder.build()
        builder.write("NewPacked.exe")


    def read_bin_data(self):
        binary_data = lief.PE.parse(self.args.input)
        self.printdetails(binary_data)
        text_section = binary_data.get_section(".text")
        return binary_data, bytes(text_section.content)

    def printdetails(self, binary_data):
        print("Программын DOS HEADER", "-"*100)
        print(binary_data.dos_header)
        print("Программын HEADER", "-"*100)
        print(binary_data.header)
        print("Программын OPTIONAL HEADER", "-"*100)
        print(binary_data.optional_header)
        print("Программын EntryPoint хаяг: ", hex(binary_data.optional_header.addressof_entrypoint))
        print("Программын section бүрэлдэхүүн хэсгүүд:" , "-"*100)
        for section in binary_data.sections:
            print(section)
        for imported_library in binary_data.imports:
          print("Import хийсэн сан: " + imported_library.name)


# Программын нэр болон тайлбарыг эхлэлд хэвлэх 
def PrintBeginning():
    print("Binary File Packer --------------------")
    print("Application Name: ", const.APPLICATIONNAME)
    time.sleep(1.5)
    return