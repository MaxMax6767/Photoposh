from FilePromptBMP import FileSelect
from Functions import IntConvert

hexdata = FileSelect()

BMP_Header = {
    "Full": hexdata[:28],  # Full BMP Header
    "Signature": hexdata[:4],  # BMP Signature (should be 424d)
    "FileSize": hexdata[4:12],  # Total file size
    "Reserved1": hexdata[12:16],  # Application Specific
    "Reserved2": hexdata[16:20],  # Application Specific
    "Offset": hexdata[20:28]  # Offset where the pixel array starts
    }

DIB_Header = {
    "Full": hexdata[28:108],  # Full DIB Header
    "DIBSize": hexdata[28:36],  # Size from this point
    "Width": hexdata[36:44],  # Left to right
    "Height": hexdata[44:52],  # Bottom to top
    "Planes": hexdata[52:56],  # Number of color planes used
    "BPP": hexdata[56:60],  # Bits per pixels
    "Compression": hexdata[60:68],  # Compression (More info : https://t.ly/YjSp)
    "ArraySize": hexdata[68:76],  # Pixel Array Size
    "P/MX": hexdata[76:84],  # Pixel / Meter horizontal (X axis)
    "P/MY": hexdata[84:92],  # Pixel / Meter vertical (Y axis)
    "ColorsInPalette": hexdata[92:100],  # Amount of colors in the palette
    "ImportantColors": hexdata[100:108]  # Amount 0f important colors in the palette (0 = all important)
}

# - Pixel Array -
Pixel_Array = [[hexdata[IntConvert(BMP_Header["Offset"])*2+X:IntConvert(BMP_Header["Offset"])*2+X+8] for X in range(0, IntConvert(DIB_Header["Width"])*8, 8)] for Y in range(IntConvert(DIB_Header["Height"]))]

# https://en.wikipedia.org/wiki/BMP_file_format

def DataPrint():
    print(f'Full Hex : {hexdata}')
    print(f'BMP Header :'
          f'\n  Full : {BMP_Header["Full"]}'
          f'\n  Signature : {BMP_Header["Signature"]}'
          f'\n  File Size : {IntConvert(BMP_Header["FileSize"])} octet'
          f'\n  Reserved 1 : {BMP_Header["Reserved1"]}'
          f'\n  Reserved 2 : {BMP_Header["Reserved2"]}'
          f'\n  Offset : {IntConvert(BMP_Header["Offset"])}')
    print(f'DIB Header :'
          f'\n  Full : {DIB_Header["Full"]}'
          f'\n  DIBSize : {IntConvert(DIB_Header["DIBSize"])}'
          f'\n  Width : {IntConvert(DIB_Header["Width"])}'
          f'\n  Height : {IntConvert(DIB_Header["Height"])}'
          f'\n  Planes : {IntConvert(DIB_Header["Planes"])}'
          f'\n  BPP : {IntConvert(DIB_Header["BPP"])}'
          f'\n  Compression : {IntConvert(DIB_Header["Compression"])}'
          f'\n  Array Size : {IntConvert(DIB_Header["ArraySize"])}'
          f'\n  Pixel / Meter (Horizontal) : {IntConvert(DIB_Header["P/MX"])}'
          f'\n  Pixel / Meter (Vertical) : {IntConvert(DIB_Header["P/MY"])}'
          f'\n  Colors In The Palette : {IntConvert(DIB_Header["ColorsInPalette"])}'
          f'\n  Important Colors : {IntConvert(DIB_Header["ImportantColors"])}')
    print("Pixel Array :")
    for pixel in Pixel_Array:
        print(pixel)

DataPrint()
