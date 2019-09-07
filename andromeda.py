#!/usr/bin/env python3

import os
from copy import deepcopy
from random import shuffle
from string import *

def main():
    numberOfSerials = int(input("Serial number amount: "))
    lengthOfSerial  = int(input("Serial number length: "))
    useNumber    = ("y" == input("Enter 'y' to use numbers: "))
    useUppercase = ("y" == input("Enter 'y' to use uppercase letters: "))
    useLowercase = ("y" == input("Enter 'y' to use lowercase letters: "))
    useSymbols   = ("y" == input("Enter 'y' to use symbols: "))

    generateSerialNumbers(numberOfSerials, lengthOfSerial, useNumber,
                          useUppercase, useLowercase, useSymbols)

def generateSerialNumbers(numberOfSerials, lengthOfSerial, useNumber,
                          useUppercase, useLowercase, useSymbols):
    characters = createCharacterList(useNumber, useUppercase, useLowercase, useSymbols)
    listOfCharacterLists = []

    for i in range(0, lengthOfSerial):
        shuffle(characters)
        listOfCharacterLists.append(deepcopy(characters))

    totalPossibleSerialNumbers = len(characters) ** lengthOfSerial

    if (totalPossibleSerialNumbers < numberOfSerials):
        print("Requested serial number amount: {}".format(numberOfSerials))
        print("Total possible serial numbers given current inputs: {}".format(totalPossibleSerialNumbers))
        print("Try one or more of the following:")
        print("- Increasing the length of the serial numbers")
        print("- Allowing more types of symbols to be used")
        print("- Decreasing the amount of serial numbers to be generated")

    else:
        fileName = str(numberOfSerials) + "_unique_serials.txt"

        printSerialNumbersToFile(fileName, numberOfSerials, lengthOfSerial,
                                 listOfCharacterLists, totalPossibleSerialNumbers)
        print()
        printPathToTerminal(fileName)
        printStatsToTerminal(numberOfSerials, totalPossibleSerialNumbers)

def createCharacterList(useNumber, useUppercase, useLowercase, useSymbols):
    characaters = []

    if useNumber:
        characaters += digits

    if useUppercase:
        characaters += ascii_uppercase

    if useLowercase:
        characaters += ascii_lowercase

    if useSymbols:
        characaters += punctuation

    return characaters

def printSerialNumbersToFile(fileName, numberOfSerials, lengthOfSerial,
                             listOfCharacterLists, totalPossibleSerialNumbers):

    serialFile = open(fileName, "w")

    singleSerialNumberString = ""
    indexList = [0] * lengthOfSerial
    distanceBetweenSerialNumbers = int(totalPossibleSerialNumbers / numberOfSerials)

    for _ in range(0, numberOfSerials):
        for y in range(0, lengthOfSerial):
            singleSerialNumberString += listOfCharacterLists[y][indexList[y]]

        # Write single serial number to file
        singleSerialNumberString += "\n"
        serialFile.write(singleSerialNumberString)

        singleSerialNumberString = ""

        # printIndexList(indexList)

        increaseIndexVectorBy(indexList, len(listOfCharacterLists[0]), distanceBetweenSerialNumbers)

    serialFile.close()

def printIndexList(indexList):
    for index in indexList:
        print(str(index).rjust(3), end = '')

    print();

def increaseIndexVectorBy(indexVctor, rolloverNumber, distanceBetweenSerialNumbers):
    increaseValueAtIndexXBy = 0

    for x in reversed(range(0, len(indexVctor))):
        increaseValueAtIndexXBy = distanceBetweenSerialNumbers % rolloverNumber
        indexVctor[x] += increaseValueAtIndexXBy

        if (indexVctor[x] >= rolloverNumber):
            indexVctor[x] -= rolloverNumber

            if (x > 0):
                indexVctor[x - 1] += 1

        distanceBetweenSerialNumbers = int(distanceBetweenSerialNumbers / rolloverNumber)

def printPathToTerminal(fileName):
    filePath = os.path.dirname(os.path.realpath(__file__)) + "/" + fileName
    print("File path: {}".format(filePath))

def printStatsToTerminal(numberOfSerials, totalPossibleSerialNumbers):
    print("Requested serial number amount: {}".format(numberOfSerials))
    print("Total possible serial numbers given current inputs: {}".format(totalPossibleSerialNumbers))
    print("The printed licenses cover {}% of the total license pool".format((numberOfSerials / totalPossibleSerialNumbers) * 100.0))

main()
