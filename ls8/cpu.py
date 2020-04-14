"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self, memory=None, registers=None, bytes=None):
        """Construct a new CPU."""
        self.bytes = 256
        self.memory = [0] * self.bytes
        self.reg = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8 #130
            0b00000000,  # 0
            0b00001000,  # 8
            0b01000111,  # PRN R0 #71
            0b00000000,  # 0
            0b00000001,  # HLT #1
        ]
  # LDI register immediate Set the value of a register
  # to an integer.
     # arg order = opcode, register#, value
# PRN Print to the console the decimal integer value that is stored in the given register.
        for instruction in program:
            self.memory[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """
        Run the CPU.
        -It needs to read the memory address that's stored in register PC, 
        -and store that result in IR, the Instruction Register. This can just be a local variable in run().

        -Some instructions requires up to the next two bytes of data after the PC in memory to perform operations on. 
        Sometimes the byte value is a register number, other times it's a constant value (in the case of LDI). 
        - Using ram_read(), read the bytes at PC+1 and PC+2 
        from RAM into variables operand_a and operand_b in case the instruction needs them.

        -Then, depending on the value of the opcode, perform the actions needed for the instruction per the LS-8 spec. Maybe an if-elif cascade...? There are other options, too.

        -After running code for any particular instruction, the PC needs to be updated to point to the next instruction for the next iteration of the loop in run(). The number of bytes an instruction uses can be determined 
        from the two high bits (bits 6-7) of the instruction opcode. See the LS-8 spec for details.
        """
        pc = 0
        running = True
        while running:
            # read the memory address that's stored in register PC == memory data
            if self.memory[pc] == 130:
                #self.mem[pc+1] = reg  self.mem[pc+2] value to store in reg #
                self.reg[self.memory[pc+1]] = self.memory[pc+2]
                # increment to next value in memory (after 1.opcode, 2. reg#, 3.value)
                pc += 3
            elif self.memory[pc] == 71:
                # PRN Print to the console the decimal integer value that is stored in the given register.
                print(self.reg[self.memory[pc+1]])
                # skip the opcode and reg# we need to print
                pc += 2
            elif self.memory[pc] == 1:
                running = False
    pc = CPU()
    pc.run()

    def ram_read(self):
        print(
            f"Ram address is {self.pc}, value at this address is {self.memory[self.pc]} ")

        return self.memory[self.pc]

    def ram_write(self, value_write_to_memory, addressIn_memoryTowrite):
        return self.memory[addressIn_memoryTowrite] = value_write_to_memory
