#! usr/env/bin python3

import sys
#categorize each line by location in list

readFile = sys.argv[1]
unknownList = list()
chromosomeList = list()

def createList(list):
    i = 0
    while i < 24:
        list.append([])
        i = i+1
createList(chromosomeList)

def trimRS(string):
    #trim off the nucleotide at the end
    string = string.strip()
    if (string[0] == 'c'):
        string = string[3:]
    string = string.split("-")
    return str(string[0])

def findLocation(string):
    string = string.strip()
    if (string[0] == 'c'):
        string = string[3:]
    if(string[0] == 'X'):
        return 'X'
    string = string.split(":")
    return int(string[0])

def printList(item):
    printString = ""
    for number in item:
        printString += str(number) + "\n"
    return printString.strip()

def printUnknown(list):
    printString = "Mapping Not Available" + "\n"
    for item in list:
        printString += (trimRS(str(item[0])) + "\n")
    return printString.strip()

with open(readFile) as input:

    for line in input:
        line = line.split(",")
        rsSnip = str(line[0])
        location = str(line[1])

        if location[0].isnumeric() or location[0] == 'c' or location[0] == 'X':
            rs_String = trimRS(rsSnip)
            chromosome_num = findLocation(line[1])
            i = 0
            for chromosome in chromosomeList:
                if i == chromosome_num:
                    chromosomeList[chromosome_num-1].append(rs_String)

                if chromosome_num == 'X' and i == len(chromosomeList)-1:
                    #print(rs_String)
                    chromosomeList[len(chromosomeList)-1].append(rs_String)
                i = i + 1



        else:
            unknownList.append(line)


    j = 0
    while j < len(chromosomeList)-1:
        j = j + 1
        f = open("schizophrenia_chromosome_%s.txt"%j, 'w')
        f.write(printList(chromosomeList[j-1]))
        f.close()
    f = open("schizophrenia_chromosome_X.txt", 'w')
    f.write(printList(chromosomeList[len(chromosomeList)-1]))
    f.close()




    g = open("unknownLocation.txt", 'w')
    g.write(printUnknown(unknownList))
    g.close()
