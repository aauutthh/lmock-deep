# file: asm_compile_binary.s
movq $0x1234567890abcdef, %rax
JMPQ *%RAX
