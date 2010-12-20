// Russell Miller - 2010
// breathalyzer.c
// Puzzle #4 - Facebook Puzzles

#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>


int openWrapper(char *filename)
{
    int returnVal = open(filename, O_RDONLY);
    if (returnVal == -1)
    {
        printf("%s\n", strerror(errno));
        exit(1);
    } else
        return returnVal;
}
   

int main(int argc, char *argv[])
{
    // force a program argument
    if (argc != 2)
    {
        printf("Please provide a filename.\n");
        exit(1);
    }
    // open the word list file
    int wordListFile = openWrapper("twl06.txt");
    // open the input file
    int inputFile = openWrapper(argv[1]);
//somehow find words in the list that are similar to an input word..
//find their levenstein values.. get the minimum.
//continue with rest of words, add up total.
    return 0;
}
