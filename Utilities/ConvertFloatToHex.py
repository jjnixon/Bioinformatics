__author__ = 'Mark Nixon'
from ctypes import *
import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

print(float_to_hex(17.5)) # Output: '0x418c0000'

ll = [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 16.3, 3.85, 16.2, 3.87, 15.05]
for l in ll:
    print(l, float_to_hex(l))