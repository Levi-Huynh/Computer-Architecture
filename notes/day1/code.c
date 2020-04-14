#include <stdio.h>
#include <stdlib.h>

// int main(void)
// {
//     int x = 100; /*default is dec value is 100 decimal*/

//     int h = 0x100; //value is 256 decimal, or 100 hex

//     int b =0b100; // binary. value is 4 decimal

//     int y = 0x47F; // add 0x in front to tell its hex

//     if (b==4){

//     }

//     return 0;

// }

// int main(void)
// {
//     int x = 0b11000101;
//     printf("%d decimal\n", x);
//     printf("%x hex\n", x);
//     printf("%X hex\n", x); //letters cap

//     return 0;
// }


// int main(void)
// {
//     int y = 255;
//     char s[20];
//     sprintf(s, "%X", y); //converts to string
//     printf("%s\n", s);



//     return 0;

// }


int main(void)
{

    char * s= "110011";
    long v = strtol(s, NULL, 2);

    printf("%ld\n", v); //l decimal 


    char *s2 = "F8"; //hex
    long v2 = strtol(s2, NULL,16) //hex is base 186
    printf("%d\n", v2) //248 decimal //printf values to string to print out 

    return 0;

}