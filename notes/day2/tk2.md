

# NOT 

NOT operator is `~` (tilde)

#changes value from 1 to 0 or 0 to 1:

```c
        a=1
        ~a == 0

```

#AND IS SINGLE `&` FOR Numbers `&&` for Boolean

#OR IS SINGLE `|` FOR Numbers `||` for Boolean

#NAND is `~` and `$`



a=0
b=0

~(a&b) ==1


#NOR 

#XOR -> only true if one or the other, NOT BOTH is true

#MULTI BIT NUMS

    11101011
&   10011101
--------------
    10001001
COLUMN BY COLUMN CHeck the `&` cases for each column is true(1) or false(0)

`&` has interesting problem:
-mask, allows you to extract individual bits from another num
while preservering some & removing others
wherever thers 1 , values on top preserved
wherever 0, values on top eliminated 


L/R shift operators

            1111
<<1        11110

            1111
>>1          111

            01011000 >>4
            00000101 (eliminate 4 values on the right,  )

            01011000 <<2
            01100000 (elim 2 values to left,  )


take opcode 

0b01101001 >>6 (bitshift right 6, will give you, the number of arguments in decs)

#HARVARDCS50

index 0 to 356 is b/c our register is 8 byte register, only inex from 0 to 255 which is 256 values
giong above we would never be able to point at it

transistor = like a switch/gate 

#NAND GATES WIKI

single bit addition, 

full adder  (has our carry)

full adder to multi bit addition(3 bits)

      111     #when number 1+1 and 2, carry 1 for 01, WHEN 1+1+1 is 3, 11 = binary, 1 is carry 
    01010101
+   10011100
------------
    11110001
how many trans in 64 bit chip to do 64 bit addition? 

64 x 18 transitors per digit: 1152 transistors to do 64 bit addition

moore's law every year, trans on chips will double 
10 million trans on chip currently 

max values you can represent in a bit 

