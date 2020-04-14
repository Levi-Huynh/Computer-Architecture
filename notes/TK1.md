Transisotrs -most basic switches
Gates- logic gates made of transistors

DIGITAL LOGIC COMMON OPS PERFORMED BY GATES:
-AND, OR, NOT, LIKE YOUVE SEEN IN CONDITIONALS IN CODE
-XOR, NOR, NAND

Gates can be put together into far more complex structures
-ALU
-CPUS


RAM-WHERE WE STORE DATA & INSTRUCTIONS THE CPU RUNS

-CPU- brain that exectutes instructions
-ALU- logic unit that does math 
-can talk to keyboard

# RAM 
RAM- stands for Random Access Memory
-Fast compared to hard drives (& even compared to SSDs)
-Think like big array of bytes that you can access by index, just like an array in your favorite programming languge
    -address=index
-Each element in RAM can store one byte, an 8-bit number 
    -1 byte per address, each 8-bit
-Larger, multi-byte values are stored in seq addresses in RAM
- CPU communicates with RAM via the memory bus 

-faster data access, better user experience 
-memory bus connectes cpu to ram (onnection of wires)
    -CPU to RAM: "give me the value at memory address 12" 
    -RAM : "memory at address 12 is 47"
    -CPU can talk that value & do other computations

Addres: 0   1   2   3   4

value: 07   A2  FF  7D  F4 

^ Hexidecimal value example 2 digits long in hex (can be written in hex/binary)
^ RAM stores values in bytes, CPU operates on words
    -words the size of your cpu as advertised (64 bit computer = 8 bytes)

-Bytes of data are stored in RAM (memory)
- Larger 64-bit (8 byte) numbers stored seq in RAM, that the CPU can operate on at once called words
-The exact number of bytes per word depends on the architecture
-8 bytes for a 64-bit CPU
    =can add 2 64-bit nums together at once if 64bit pc
-4 bytes for a 32-bit CPU
-1 byte for an 8-bit CPU
    -8 bit pc can add 2 8-bit nums together at once.. else if want to add nums greater than that together must add nums `one byte at at time`


CPU REGISTERS
-Store words that can be accessed at ultra-high speed
-think like variables that CPU has at its disposal
-Similar to RAM, except `stored directly on the CPU so they are much faster`
-There are `limited number of them at your disposal, usually 8, 16, 32, depending on the CPU`
-They have fixed names, eg `RO, R1, EAX, EBX, etc depending on the CPU`
-`Many CPUs can only perform math operations on registers which must be loaded from RAM first`
(x86 family can often perform math on registers quickly or RAM slowly)
-instead of having to grab data from RAM across mother board wires, if data already on registers 
^addor mult nums ops stays on registers, side of register is size of cpu word

CPU INSTRUCTIONS
-Also stored in RAM wih other data
-Are actually just numbers (that has corresponding instruction such as add or multiply implied with that number)
-`CPU DECIDES INSTRUCTION BASED ON VALUE IT JUST GOT OUT OF RAM` 
-Humans often use mnemonics to refer to the instruction in a human-readable way
-The CPU keeps track of the addrss of the currently-exectuing instruction in RAM & performs diff actions based ont he instruction found there
-The `address /index into memory array of the currently-executing instruction  `is held in a special register called the program counter (PC)
ex/ 
-go into ram
-pull instructions from RAM at the address given by the (PC), loop & repeat
-CPUS usually have a significant number of instructions around 50-2,000  (math, changing etc , which instructions dpeend on CPU) 

CPU CLOCK
-the clock in a modern CPU triggers a few billion times per second
-Clock cycle rate is measured in Hz, KHz, MHz, GHz (billions of cycles per second)
-Each instruction takes one or more clock cycles to execute 
-`The faster the clock, the more instructions can execute per second ` 2.5GHZ, MACHINE ETC, 
DECIDES ON FAST CLOCK CYCLES

CONCURRENCY:
`How the CPU does more than 1 thing at once`
-Each hardware component can only do one thing at once
-Dpulicate the hardware components!
-Multi-core CPUs 
-Pipelining
-Timesharing `faking concurrency`:
    -CPU does something for awhile, skips to new, goes back to first, switch every few milliseconds, looks like
    its multi tasking, but only do diff tasks for a few seconds & switching

-everything in CPU connected by electric wires, but can only transmit 1 signal or transaction at once
-unless add more  -ALU- logic unit that does math (can do 2x if have 2)
- dupblicate entire CPU! 4 cores of CPU replicated 4 times etc 4 cores in 1 cpu (multi core, running totally independent.) Can share RAM but the core themslves perform instructions independently & be parallel

SYSTEM BUS
How data is passed from the CPU to RAM, from the CPU to peripherals
-`Address Bus`: carries the address in RAM we're interested in , or the peripheral ID we're interested in
-`Data Bus`: carries data to be transmitted to or from RAM or peripherals 
-`Control Bus`: controls whether or not the CPU is talking to RAM or a peripheral! & which periph.
-The size or width of the bus is typically the number of "bits"a computer is advertised as having
 A 64 bit CPU: `has a 64-bit wide data bus` and `usually a 64bit wide address bus`  

CACHING

-lives on CPU, speeds up access to RAM
    -interested in data at address 10 in memory
    if dont have = cache miss
    if have  = cache hit
    -also grabs 2kb of data starting at the address you want, to store for the future
    -gives CPU address 10 data
    -gets seq data quickly bc it grabs & stored extra data of nearby address when it goes to grab the origal request 
    - can write code that delib causes cache hits/miss, in c programming 2d array (can iterate quickly over
        columnx row, versus slow for rowxcolumn iteration based on how cpu works)
-Access to RAM is relative slow
-Access to Registers is fast
-`Middle ground? === Cache`
-Closer to the CPU
-Usually arranged in a level hierarchy
- Cache Miss means you're trying to access memory that's not yet in the cache
-Cache Hit means the meory you want is in the cache already 


Numbers & values
valuex exist regardless of how written
12 apples (decimal)
1100 binary
c (hexadecmial)

Number Bases-How many individual digits that num system has
-Decimal has 10 digits (0,1,2,3,4...10) base 10
-Binary has 2 digits (0,1) (binary digit called bit for short)
-Hexadecimal/hex -16 digits (0,1,2,3,4,5,6,7,8,9, A,B,C,D,E,F) base 16 color scheme
-Octal has 8 digits (0,1,2,3,4,5,6,7) so its base 8 (not frequently used)

-binary can convert to hex b/c bases to power of 2

Terms:

Byte- 8 binary digits/ bits, set all  bits to 1=> Max Value : 255 dec , FF (largest it gets) hex, Min value 0 
    -red green blue values stored in 1 byte each 
Nibble: 4 bits, Max value 15 dec, F hex, Min value 0
Octet: synonmous for byte
Decimal-a base-10 numbering system, the one you already know
Hexadecimal or hex: A base-16 number system
Binary - A base-2 numbering system
Octal - A rarely used base8 numbering system  , decimal value 10 012 leading zero in front of dec num

can leave off leading zero for binary 



+=========128s place
|+========64s place
||+=======32s place
|||+======16s place
||||+=====8s place
|||||+====4s place
||||||+===2s place
|||||||+==1s place
||||||||
01010110
    1100

`add up the places where the 1s exist`

  1010110 binary (leave off leading 0, examplbe bove) => 61+16+6=86 decimal

1111 binary ==>  8+4+2+1 = 15 decimal 


67 dec in binary: => 
1) which prime, biggest factorial combo gets 67:
2) 64 + 2 + 1 => only put a 1 where 64th, 2th & 1st place is!
              =>  1000011
3) 33 ==>  32 place+ 1 place 
        => 100001


`binary to hex` have bases that are powers of 2
nibble 4 -bits half a biye 

10100011 1 byte number, 8 bits long
split half (2 nibbles, each can be converted to hex):

1010 0011

Right nibble:  0011
Convert to decimal:  has 1 in 1 place, 1 in 2 place  = 1+2 == 3 (*hint ANY NUM UNDER 10 IS SAME IN HEX & DEC)

Left nibble: 1010
Convert to decimal, has 1 in 2 place, 1 in 8 lace = 8+2 ==10
10 in hex ==  A  (1-9 is digit, run out of digits then A-F)


1010 0011
 A    3  => A3 in hex == 10100011

c7 hex ==? binary

1-9, 10-A, 11-B, 12 dec == C
12 dec = 1100 binary (1 in 8 place, 1 in 4 place)

7 dec =7 hex
7 dec = 0111 binary (1 in 1, 1 in 2, 1 in 4) #WHEN DO WE KNOW TO ADD LEADING ZERO?

C       7 = 11000111


Binary is layer of abstraction over electricity, transistors
Transistor holding charge, holding voltage thats a 1

Highlevel lang like javascript are abstractios over binary, binary abstractions over transistors 
if foundation is strong can have better backbone to build on highlevel understanding how PC works



CS26 LECTURE:
IN Memory is long array, 1D , of 1 & 0 #ONLY , software is what interprets which is opcode or argument
^ long list of 1's & 0's , opcode, argument, opcode opcode argument, diff 1's diff 0's treated as opcode or argument
