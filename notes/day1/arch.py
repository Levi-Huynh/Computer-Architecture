0b10100110

2 ** 0 = 1  # (2s just double each time )
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128

2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1020


1010

2+8 = 10

0b00110101
1+4+16+32 = 53  # 0x35 hex

0b11111111 = 0xFF = 255

# byte = 8 bits

# rgb(red, g b) rgb(171, 286, 239)

# asciitable.com
# unicode alows emojis, encoding works
# emulator= emulating machine  using software


# binary to dec
program = [
    # From print8.ls8
    0b10000010,  # LDI R0,8
    0b00000000,
    0b00001000,
    0b01000111,  # PRN R0
    0b00000000,
    0b00000001,  # HLT
]

for i in program:
    word = bin(i)
    word1 = int(word, 2)
    print(f"\n {word1}")

