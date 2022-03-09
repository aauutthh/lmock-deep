#!/usr/bin/python3

from capstone import *
import sys

#CODE = b"\x50\x51\x52\x53\x54\x55\x56\x57"
CODE = open(sys.argv[1],'br').read()

md = md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(CODE, 0x1000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
