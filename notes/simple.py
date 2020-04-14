import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4  # SAVE A VALUE TO A REGISTER
PRINT_REGISTER = 5  # PRINT A VALUE FROM REGISTER
ADD = 6  # regA += regB

# our add doesnt read from memory, saving that value into register

memory = [  # represents our RAM
    PRINT_BEEJ,
    SAVE,
    65,  # save 65 to reg 2
    2,
    SAVE,
    20,  # save 20 to reg 3
    3,
    ADD,  # sum up value in reg 2+=reg3
    2,
    3,
    PRINT_REGISTER,  # print reg 2
    2,
    HALT


]


register = [0] * 8

pc = 0  # register that points to this location in memory!!!/ index counter in memory
running = True
while running:  # our processor
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
    elif command == HALT:
        running = False
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc+1]
        print(num)
        pc += 2  # increment by 2 to skip num arg
    elif command == SAVE:
        num = memory[pc+1]
        reg = memory[pc + 2]
        register[reg] = num
        # increment by 3 (opcode, argument, number) b/c we had 2 arguments to save,
        pc += 3
    elif command == PRINT_REGISTER:
        reg = memory[pc+1]
        print(register[reg])
        pc += 2  # for our opcode & our register argument
    elif command == ADD:
        reg_a = memory[pc+1]
        reg_b = memory[pc+2]
        register[reg_a] += register[reg_b]
        pc += 3  # opcode, & arg rega & regb
    else:
        print(f"Uknown instruction: {command}")
        sys.exit(1)


# built into hardware, & lives where CPU is, extremly fast way to store & use data without requesting from RAM/memory
# very small & can only hold a word = base unit of data measurement
# ls-8 registers are all 8-bit values , register will hold as much as architecture value, can be 32bit pn 32 bit architecture
# 64 bit architecture each register will hold 64 bit.
 # ^ value is called word, built into register
 # cache is  alittle bigger than register, _but_ slightly slower than register, but faster than RAM
 # RAM is much bigger, but the slowest of the 3

# virtual memory, when run out of RAM will start using your HDD like RAM
# above HD is cloud, like AWS, infinte terabytes, slow== read write to remote network (cheaper storage, but slower)
# HD dont need power, can unplug & still persist
# RAM need a power source to run
# GPU, graphic processing? VRAM on GPU, is parallel
