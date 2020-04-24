# ALU-what kind of instructions ALU processes


An arithmetic-logic unit (ALU) is the part of a computer processor (CPU) that carries out arithmetic and logic operations on the operands in computer instruction words. In some processors, the ALU is divided into two units, an arithmetic unit (AU) and a logic unit (LU).
Machine instructions that use the ALU specify four things:

The operation to perform.
The the first operand (often in a register).
The second operand (often in a register).
The register that receives the result.

Logic gates can be composed into circuits that can do far more than Boolean logical operations.

You can build an ALU, for example, that does arithmetic and comparisons using only logic gates.

ALU OPS

ADD  10100000 00000aaa 00000bbb
SUB  10100001 00000aaa 00000bbb
MUL  10100010 00000aaa 00000bbb
DIV  10100011 00000aaa 00000bbb
MOD  10100100 00000aaa 00000bbb

INC  01100101 00000rrr
DEC  01100110 00000rrr

CMP  10100111 00000aaa 00000bbb

AND  10101000 00000aaa 00000bbb
NOT  01101001 00000rrr
OR   10101010 00000aaa 00000bbb
XOR  10101011 00000aaa 00000bbb
SHL  10101100 00000aaa 00000bbb
SHR  10101101 00000aaa 00000bbb


https://whatis.techtarget.com/definition/arithmetic-logic-unit-ALU

# CPU-what it does
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
        * Registers must be very fast to access (to read and write) compared to RAM 
        -ssembly language programs use registers whenever possible to keep speed up.
    * __CPU clock__ : When they say your CPU is 3.2 GHz, this is what they are referring to. It’s the number of times per second the CPU does some processing
        * Each time the clock cycles, the CPU does a bit more work.
        * Some instructions take one clock cycle to complete, but others might take several.
    * __System bus__ :  A collection of wires on the motherboard between the CPU, memory, and peripherals.
        * The memory bus connects the CPU to RAM.
        * The I/O bus connects the CPU to peripherals.
        * The control bus allows the CPU to say exactly what it wants to do on the bus, e.g. read or write a word or byte.
    *__Concurrency and Parallelism__: The CPU can do multiple things once through a variety of mechanisms, including haveing multiple cores, or other features
    such as pipelining, or hyperthreading 


# CPU stack 


* Most CPUs have a built-in stack that’s useful for keeping temporary data, making subroutine calls, and handling interrupts.
    -__Since the number of registers is limited on a CPU, the stack is a useful place to store data temporarily.__ 


Turns out a stack is a really useful data structure for a number of reasons:

It's a great place to temporarily store data to free registers for other uses.
It's useful for holding a return address for a subroutine/function.
It's a place to pass arguments to subroutines.
It's a good place to hold a subroutine's local variables.
It can hold all the information that needs to be saved while the CPU is servicing an interrupt.
-Saving registers so they can be restored after a function call or interrupt handler.
Additionally, it's pretty cheap to implement. All CPUs already come with this functionality:

Memory (for the stack data)
Registers (for the stack pointer)
A way to decrement and increment registers (to move the stack pointer)
A way to read and write data to and from RAM (to retrieve and store data on the stack)
Since the CPU was doing all that anyway, adding PUSH and POP instructions is a pretty low-hanging fruit.

====================================

  What it consists of Minimally:

    -An array for storing values (a chunk of RAM).
    -A pointer to the top element of the stack (known as the stack pointer or commonly SP)
    -PUSH and POP instructions.


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


=======================================

# How are stacks and subroutines used & work by higher-level languages like Python?
In Python, when you make a function call, a bunch of space is allocated (pushed) on the stack to hold a number of things:

The return address to come back to after the function completes
Space for all the function parameters
Space for all the other local variables in the function
This allocated chunk of stack is called a stack frame.

When you call any function:

A new stack frame is allocated (pushed)
Parameter values are copied from the function arguments to their spots on the stack frame
When you return from any function:

Any return value is copied from the stack frame into a dedicated register
The stack frame is deallocated (popped)
In assembly language, CALL doesn't allow any arguments to be passed, and RET doesn't allow any values to be returned.

Using stack frames gives CALL the power to give parameters to subtroutines.

And we can use a dedicated register, like R0, to pass returned values back to the caller over a RET instruction.

Since all the local variables for a function are stored in the stack frame, they all vaporize as soon as the stack is popped when the function returned. This is why local variables are not persistent from call to call.

Furthermore, using the stack to hold frames allows us to call functions to an arbitrary nesting level. Indeed, it is what allows for recursion at all.

==========================

What are the << and >> shift operators useful for?
Most commonly, they're used to get or set individual bits within a number.

This is useful if multiple values are packed into a single byte. Bytes hold numbers from 0 to 255, but parts of a byte can hold smaller numbers. For example, if you have 4 values that you know only go from 0-3 each, you can pack that into a byte as four 2-bit numbers.
==============================================
Why is hex base 16? Seems so random.
Conveniently, one hex digit represents exactly 4 bits (AKA a nibble).

This means a byte can be represented by exactly 2 hex digits (assuming you put a leading zero on numbers less than 0x10). And the biggest byte's value roundly ends at 0xff.

It's compact, and easy to convert to and from binary.
=================================================

Why does the CPU allow for stack overflow or underflow?
It takes time for the CPU to check to see if either condition has occurred. And most of the time it won't have.

CPUs are interested in running instructions as quickly as possible.

Also, you'd need additional hardware in place to make those checks, and that costs money.

==============================================

# How number bases work, how to count in them, and how to convert between bases.

0 1 2 3 4 5 6 7 8 9 A=10 B=11 C=12 D=13 E=14 F=15

128 64 32 16 8 4 2 1


    * The count of the number of items doesn’t change just because we refer to it in a numbering system of a different base.
    * (the only place the numbering system matters is when we write down the number someplace ) And remember that when you do write it down, the count of what the number refers to remains the same regardless of the base you choose to write it down in.
__Bases__ : 
        * The base of a numbering system refers to how many digits the numbering system has. 
        * Decimal numbers like we’re used to have 10 digits: 0 through 9. Decimal numbers are base-10.
            * In decimal, we have 10 digits, 0-9. Multi-digit numbers have the 1’s place, the 10’s place, and the 100’s place, etc
        * Binary numbers have two digits: 0 and 1. Binary is base-2.
            * binary, we only have two digits, 0-1. Multi-digit numbers have the 1’s place, the 2’s place, the 4’s place, the 8’s place, the 16’s place, etc.
            * 1 2 4 8 16 32 64 128 256 512 1024
            2048 4096 8192 16384 32768 65536
            * These are all powers of 2. 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, etc.
            * Computers find it convenient to represent numbers in base 2 for a variety of reasons. One is that it’s easy to represent as a voltage on a wire: 0 volts is a 0 and 5 volts (or whatever) is a 1. Another is that you can do boolean logic with 0 being FALSE and 1 being TRUE.
        * Hexadecimal had 16 digits: 0-9 then A-F. It’s base-16.
        * Octal; it’s base-8. (In Unix when you issue a command like chmod 755 or chmod 644, those numbers are octal.