#!/usr/bin/env python3

import os
from random import shuffle
from string import *

def generate(number_of_serials, length_of_serial, use_numbers="y", use_uppercase="y", use_lowercase="y", use_symbols="y"):
    if use_numbers == False:
        use_numbers = ""
    if use_uppercase == False:
        use_uppercase = ""
    if use_lowercase == False:
        use_lowercase = ""
    if use_symbols == False:
        use_symbols = ""

    listOfCharacterLists = createListOfCharacterLists(length_of_serial, use_numbers, use_uppercase,
                                                      use_lowercase, use_symbols)
    totalPossibleSerialNumbers = len(listOfCharacterLists[0]) ** length_of_serial

    if (totalPossibleSerialNumbers < number_of_serials):
        printErrorMessage(number_of_serials, totalPossibleSerialNumbers)
        return

    generateSerialNumbers(number_of_serials, length_of_serial, listOfCharacterLists, totalPossibleSerialNumbers)

def createListOfCharacterLists(length_of_serial, use_numbers, use_uppercase, use_lowercase, use_symbols):
    characterList = createCharacterList(use_numbers, use_uppercase, use_lowercase, use_symbols)
    listOfCharacterLists = []

    for i in range(length_of_serial):
        shuffle(characterList)
        listOfCharacterLists.append(characterList.copy())

    return listOfCharacterLists

def createCharacterList(use_numbers, use_uppercase, use_lowercase, use_symbols):
    characterList = []

    if use_numbers:
        characterList += digits

    if use_uppercase:
        characterList += ascii_uppercase

    if use_lowercase:
        characterList += ascii_lowercase

    if use_symbols:
        characterList += punctuation

    return characterList

def generateSerialNumbers(number_of_serials, length_of_serial, listOfCharacterLists, totalPossibleSerialNumbers):
    fileName = str(number_of_serials) + "_unique_serials.txt"
    addSerialsToArray(number_of_serials, length_of_serial,
                             listOfCharacterLists, totalPossibleSerialNumbers)

def addSerialsToArray(number_of_serials, length_of_serial, listOfCharacterLists, totalPossibleSerialNumbers):
    global serial_array
    serial_array = []

    singleSerialNumberString = ""
    indexList = [0] * length_of_serial
    distanceBetweenSerialNumbers = int(totalPossibleSerialNumbers / number_of_serials)

    for _ in range(number_of_serials):
        for y in range(length_of_serial):
            singleSerialNumberString += listOfCharacterLists[y][indexList[y]]

        serial_array.append(singleSerialNumberString)
        singleSerialNumberString = ""

        # printIndexList(indexList)

        increaseIndexVectorBy(indexList, len(listOfCharacterLists[0]), distanceBetweenSerialNumbers)


def printIndexList(indexList):
    for index in indexList:
        print(str(index).rjust(3), end = '')

    print()

def increaseIndexVectorBy(indexVctor, rolloverNumber, distanceBetweenSerialNumbers):
    increaseValueAtIndexXBy = 0

    for x in reversed(range(len(indexVctor))):
        increaseValueAtIndexXBy = distanceBetweenSerialNumbers % rolloverNumber
        indexVctor[x] += increaseValueAtIndexXBy

        if (indexVctor[x] >= rolloverNumber):
            indexVctor[x] -= rolloverNumber

            if (x > 0):
                indexVctor[x - 1] += 1

        distanceBetweenSerialNumbers = int(distanceBetweenSerialNumbers / rolloverNumber)
def get_serials():
    return serial_array