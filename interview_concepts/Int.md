ALU-what kind of instructions ALU processes


An arithmetic-logic unit (ALU) is the part of a computer processor (CPU) that carries out arithmetic and logic operations on the operands in computer instruction words. In some processors, the ALU is divided into two units, an arithmetic unit (AU) and a logic unit (LU).
Machine instructions that use the ALU specify four things:

The operation to perform.
The the first operand (often in a register).
The second operand (often in a register).
The register that receives the result.

https://whatis.techtarget.com/definition/arithmetic-logic-unit-ALU

CPU-what it does
CPUs, or Central/Core Processing Units, are responsible for processing and executing instructions

CPUs are built by placing billions of microscopic transistors onto a single computer chip. Those transistors allow it to make the calculations it needs to run programs that are stored on your system’s memory. 

The instruction is represented as a series of numbers and is passed to the CPU from the RAM. The current instruction address is held by a program counter (PC). The PC and instructions are then placed into an Instruction Register (IR). The PC length is then increased to reference the next instruction’s address.

# Functional Components of CPU
what a CPU word is
    * CPU word: the natural size of a piece of data with which the CPU can interact. Usually written down in the bit “size” of the CPU, i.e. “This is a 64-bit CPU.”
    * The CPU can quickly perform math and other operations on data of its __word__ size. (It can also work with other size data, as well, though it might not be as speedy).
    * __RAM(Random Access Memory)__: Big array of bytes that can be retrieved by index, just like a regular array.
        * The index into memory is referred to as an address or a pointer.
        * Similiar to regular indexed array: when you have the address of a value (AKA a pointer to that value), you can retrieve that value stored at that address.
    *  Nowadays most desktop computers use either 32-bit CPUs or 64-bit CPUs. The instructions in a 32-bit CPU are good at handling data that is 32 bits in size (most instructions "think" in 32 bits in a 32-bit CPU). Likewise, a 64-bit CPU is good at handling data that is 64 bits in size (and often good at handling 32-bit data too). The size of data that a CPU handles best is often called the word size of the CPU.
    * __CPU instruction__ :  A byte or sequence of bytes in RAM that the computer knows how to interpret and perform actions based on.
        *There are instructions to do math, like ADD and SUB, instructions for comparing values like CMP, instructions for jumping to other parts of memory like JMP, and many more.
        *The exact instruction names and values vary depending on architecture.
    * __CPU register__ : The CPU has a fixed, small number of special storage locations built-in. Usually there are 16 or 32 of these, and they have fixed names, such as R0, R1, R2, and so on. (Details vary by architecture.)
        *Think of them like variables you have at your disposal to use with the various instructions.
        *store the data that the instructions operate on (the data that they read and write)
        * Registers must be very fast to access (to read and write)
    * __CPU clock__ : When they say your CPU is 3.2 GHz, this is what they are referring to. It’s the number of times per second the CPU does some processing
        * Each time the clock cycles, the CPU does a bit more work.
        * Some instructions take one clock cycle to complete, but others might take several.
    * __System bus__ :  A collection of wires on the motherboard between the CPU, memory, and peripherals.
        * The memory bus connects the CPU to RAM.
        * The I/O bus connects the CPU to peripherals.
        * The control bus allows the CPU to say exactly what it wants to do on the bus, e.g. read or write a word or byte.
    *__Concurrency and Parallelism__: The CPU can do multiple things once through a variety of mechanisms, including haveing multiple cores, or other features
    such as pipelining, or hyperthreading 

CPU stack


* Most CPUs have a built-in stack that’s useful for keeping temporary data, making subroutine calls, and handling interrupts.
    -__Since the number of registers is limited on a CPU, the stack is a useful place to store data temporarily.__ 
    -[The stack is a data structure so useful that CPU designers typically include it in their instruction sets.]

    -Temporarily storing values if you need to free registers for other uses.
    -Saving registers so they can be restored after a function call or interrupt handler.
    -Allocating space for local variables in a subroutine call.

    The minimalist stack consists of just a few things:

    -An array for storing values (a chunk of RAM).
    -A pointer to the top element of the stack (known as the stack pointer or commonly SP)
    -PUSH and POP instructions.
    -[Usually there’s no specific instruction for peeking at the value at the top of the stack. A standard memory access instruction such as LD is used for -that purpose, if necessary].

-In many architectures, the stack begins at a high address in RAM and grows downward. 
-That is, the SP is decremented when additional items are pushed on the stack. 
-ie your stack is growing down from the ceiling as you push onto it.

To __PUSH__ a value in a register onto the stack:
Decrement SP.
Store the value in the register into RAM (at the address stored in SP).

To __POP__ a value from the stack into a register:
-Retrieve the value from RAM (at the address stored in SP), 
and store that value in the register.
Increment SP.

https://www.geeksforgeeks.org/introduction-of-stack-based-cpu-organization/