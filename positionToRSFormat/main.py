#! usr/env/bin python3

import sys
import re
#replace chromosome positions with RS nums if available

tsvOuput = sys.argv[1]
printList = []
numList = []
mappingDict = {}

def getPosition(line):
    newLine = line.split('\t')
    chromPos = newLine[0]
    return chromPos

def getRS(line):
    newLine = line.split('\t')
    rsNum = newLine[1]
    return rsNum

def getChromNum(line):
    locationLine = line.split(":")
    chromNum = locationLine[0]
    return chromNum


with open(tsvOuput) as input:
    for line in input:
        line = line.strip()
        if '\t' in line:
            chromNum = getChromNum(line)
            #if chromNum not in numList:
                #numList.append(chromNum)
            rsNum = getRS(line)
            #if none of the files contained chromosome positions use this line
            file = "schizophrenia_chromosome_%s.txt" % chromNum
            with open(file, 'a') as fOutput:
                fOutput.write('\n' + rsNum)
            #chromPos = getPosition(line)
            #mappingDict[chromPos] = rsNum
outString = ""
for num in numList:
    outString = ""
    file = "schizophrenia_chromosome_%s.txt" % num
    with open(file, 'r') as fInput:
        for item in fInput:
            item = item.strip()
            if item[0] == 'r':
                outString += item + '\n'

            #schizophrenia file has no chromosome numbers in specific files, all chromosome numbers went to unknown file
            #use this elif statement when chromosome numbers are within files already
            #elif item in mappingDict:
                #outString += mappingDict[item] + '\n'


for num in numList:
    file = "schizophrenia_chromosome_%s.txt" % num
    with open(file, 'w') as fOutput:
        fOutput.write(outString.strip())







