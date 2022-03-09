all: code.bin display

code.bin: asm_compile_binary.o
	#ld -e 0 --oformat binary a.o -o $@
	objcopy -S -g -B i386 -O binary $< $@

%.o:%.s
	as -o $@ $^

display: code.bin
	od -tx1 $<
	#objdump -D -Mintel,x86-64 -b binary -m i386 $<
	objdump -D -Mx86-64 -b binary -m i386 $<
	python disassm.py  code.bin

clean:
	rm -Rf *.o *.bin
