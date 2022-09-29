#Corbin Kiefner
#CSC 499
#Homework 1
#Sept. 14th, 2022

import fileinput, argparse

#Initialize variables
tracker = argparse.ArgumentParser(description= "Name sorter")
nameList = [];

#Implement arguments
tracker.add_argument("filename")
tracker.add_argument("-r", "--reverse",
                     help = "Optional variable. Enter input if you wish to reverse the sorted list.",
                     action = "store_true")
argument = tracker.parse_args()

#populate sorting array from the provided text file
for line in fileinput.input(argument.filename):
    nameList.append(line.rstrip())

#alphabetize the list of names
nameList.sort()

#if user wishes to sort the list in reverse order
if argument.reverse:

    #itterate through each name of the array
    for index in range(0, len(nameList)):
        placement = index
        currentName = nameList[index]

        #while loop to switch placement in the array depending on the length of the name at current index
        while placement >= 1 and len(nameList[placement - 1]) < len(currentName):
            nameList[placement] = nameList[placement - 1]
            placement = placement - 1
        nameList[placement] = currentName

#if user wishes to sort the list in normal order
else:

    #itterate through each name of the array
    for index in range(0, len(nameList)):
        placement = index
        currentName = nameList[index]

        #while loop to switch placement in the array depending on the length of the name at current index
        while placement >= 1 and len(nameList[placement - 1]) > len(currentName):
            nameList[placement] = nameList[placement - 1]
            placement = placement - 1
        nameList[placement] = currentName

#open a new text document
file = open("Sorted List.txt", "w")

#write the names in the sorted list, each on a new line
for name in nameList:
    file.write(name + "\n")

#end
file.close
