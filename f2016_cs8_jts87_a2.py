#Jacob Soto
#CS0008
#Prof. Max Novelli
#Assignment 2

#step one: define 2 functions
#one function counts number of lines and distance ran in file
#second function creates format to display totals for files in format similar to-

#File to be read: file_1.csv
#Partial Total # of lines : x1
#Partial distance run     : y1

#File to be read: file_2.csv
#Partial Total # of lines : x2
#Partial distance run     : y2

#File to be read: quit
#Totals
#Total # of lines   : x1 + x2
#Total distance run : y1 + y2
#define processfile function. Count number of lines and keep running total of distance run
def processfile():
        #define variables for later use
        numlines = 0
        distance = 0
        file_contents = fopen.readline()
        #split comma separated values with split
        file_contents = file_contents.split(',')
        for line in fopen:
            line = line.rstrip("\n")
            temp = line.split(',')
            numlines += 1
            rtotal = float(temp[1])
            distance += rtotal
            print(numlines,distance)
        return numlines,distance
#define printKV, format data output for user
def printKV(key, value, klen=0):
    KL = max(len(key), klen)
    if isinstance(value,str):
        FS = '20s'
    elif isinstance(value,float):
        FS = '10.3f'
    elif isinstance(value,int):
        FS = '10.3f'
    print(format(key,str(KL)+'s'))
    format(value,FS)
#define variables for later use
totaldistance = 0
totallines = 0
file = input('file to be read:',)
#inputs to tell the program to stop reading files
while file != '' and file != 'quit' and file != 'q':
    fopen = open(file, 'r')
    numlines,distance = processfile()
    printKV(int,numlines)
    printKV(float, distance)
    totaldistance += distance
    totallines += numlines
    file = input('next file')















