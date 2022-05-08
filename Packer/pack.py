from termcolor import colored, cprint
from lief import PE
import const
import lief
import time
import pefile
import clr
# from System import String
# from System.Collections import *
# from System.Windows.Forms import Form
# import pydasm
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
        try:
            pe = pefile.PE(self.args.input)
            pe.parse_data_directories([pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG']])
            if pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR']].VirtualAddress != 0:
                dotnet = True
                print(".NET Executabl file found")
            if pe.OPTIONAL_HEADER.ImageBase:
                imagebase = hex(pe.OPTIONAL_HEADER.ImageBase)
            epoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint
            print("Image base is: %s"% imagebase)
            print("Entry-Point-ын хаяг = %s" %hex(epoint))
            print("Хэсгүүдийн тоо = %s"%hex(pe.FILE_HEADER.NumberOfSections))
            print("Data Directory-ын тоо = %d" %pe.OPTIONAL_HEADER.NumberOfRvaAndSizes)
            code_section = find_entry_point_section(pe, epoint)
            # for section in pe.sections:
            #     print (section.Name, hex(section.VirtualAddress))
            # print(pe.print_info())
            # for entry in pe.DIRECTORY_ENTRY_IMPORT:
            #     print(entry.dll.decode('utf-8'))
                # if sect.Name == '.text':
                    # print ("%s %s" % (section.PointerToRawData),hex(section.Misc_VirtualSize))
                # print("%17s" % (sect.Name).decode('utf-8'), end='')
                # print(("\t%5.2f" % sect.get_entropy()))
            # The List will contain all the extracted Unicode strings

            # strings = list()

            # # Fetch the index of the resource directory entry containing the strings
            # rt_string_idx = [entry.id for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_STRING'])
            # print(rt_string_idx)
            # Get the directory entry
            #
            # rt_string_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_string_idx]
            # # For each of the entries (which will each contain a block of 16 strings)
            # #
            # for entry in rt_string_directory.directory.entries:
            
            #   # Get the RVA of the string data and
            #   # size of the string data
            #   #
            #   data_rva = entry.directory.entries[0].data.struct.OffsetToData
            #   size = entry.directory.entries[0].data.struct.Size
            #   print ('Directory entry at RVA', hex(data_rva), 'of size', hex(size))
            #   # Retrieve the actual data and start processing the strings
            #   #
            #   data = pe.get_memory_mapped_image()[data_rva:data_rva+size]
            #   print("-------------------",data)
            #   offset = 0
            #   while True:
            #     # Exit once there's no more data to read
            #     if offset>=size:
            #       break
            #     # Fetch the length of the unicode string
            #     #
            #     ustr_length = pe.get_word_from_data(data[offset:offset+2], 0)
            #     offset += 2
            #     # If the string is empty, skip it
            #     if ustr_length==0:
            #       continue
            #     # Get the Unicode string
            #     #
            #     ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=ustr_length)
            #     offset += ustr_length*2
            #     strings.append(ustr)
            #     print ('String of length', ustr_length, 'at offset', offset)
            # shellcode = bytes(b"\xd9\xeb\x9b\xd9\x74\x24\xf4\x31\xd2\xb2\x77\x31\xc9")
            # shellcode += b"\x64\x8b\x71\x30\x8b\x76\x0c\x8b\x76\x1c\x8b\x46\x08"
            # shellcode += b"\x8b\x7e\x20\x8b\x36\x38\x4f\x18\x75\xf3\x59\x01\xd1"
            # shellcode += b"\xff\xe1\x60\x8b\x6c\x24\x24\x8b\x45\x3c\x8b\x54\x28"
            # shellcode += b"\x78\x01\xea\x8b\x4a\x18\x8b\x5a\x20\x01\xeb\xe3\x34"
            # shellcode += b"\x49\x8b\x34\x8b\x01\xee\x31\xff\x31\xc0\xfc\xac\x84"
            # shellcode += b"\xc0\x74\x07\xc1\xcf\x0d\x01\xc7\xeb\xf4\x3b\x7c\x24"
            # shellcode += b"\x28\x75\xe1\x8b\x5a\x24\x01\xeb\x66\x8b\x0c\x4b\x8b"
            # shellcode += b"\x5a\x1c\x01\xeb\x8b\x04\x8b\x01\xe8\x89\x44\x24\x1c"
            # shellcode += b"\x61\xc3\xb2\x08\x29\xd4\x89\xe5\x89\xc2\x68\x8e\x4e"
            # shellcode += b"\x0e\xec\x52\xe8\x9f\xff\xff\xff\x89\x45\x04\xbb\x7e"
            # shellcode += b"\xd8\xe2\x73\x87\x1c\x24\x52\xe8\x8e\xff\xff\xff\x89"
            # shellcode += b"\x45\x08\x68\x6c\x6c\x20\x41\x68\x33\x32\x2e\x64\x68"
            # shellcode += b"\x75\x73\x65\x72\x30\xdb\x88\x5c\x24\x0a\x89\xe6\x56"
            # shellcode += b"\xff\x55\x04\x89\xc2\x50\xbb\xa8\xa2\x4d\xbc\x87\x1c"
            # shellcode += b"\x24\x52\xe8\x5f\xff\xff\xff\x68\x6f\x78\x58\x20\x68"
            # shellcode += b"\x61\x67\x65\x42\x68\x4d\x65\x73\x73\x31\xdb\x88\x5c"
            # shellcode += b"\x24\x0a\x89\xe3\x68\x58\x20\x20\x20\x68\x4d\x53\x46"
            # shellcode += b"\x21\x68\x72\x6f\x6d\x20\x68\x6f\x2c\x20\x66\x68\x48"
            # shellcode += b"\x65\x6c\x6c\x31\xc9\x88\x4c\x24\x10\x89\xe1\x31\xd2"
            # shellcode += b"\x52\x53\x51\x52\xff\xd0\x31\xc0\x50\xff\x55\x08"
            
            # ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
            # print("[*] Writting %d bytes at offset %s" % (len(shellcode), hex(ep)))
            # pe.set_bytes_at_offset(ep, shellcode)
            # new_exe_path = "C:/Users/Bilguun/Desktop/Hello_World_New.exe"
            # pe.write(new_exe_path)
        except OSError as e:
            print(e)
        except pefile.PEFormatError as e:
            print("[-] PeFormatError: %s" % e.value)

    def net_open(self):
        return
    
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