from glob import glob
import os
from random import choice, random

"""
This program chooses a line at random suitable for tweeting:
greater than zero characters, less than 140 characters, etc.
"""
def isSuitable(line):
    return ( line is not '%' and line is not '' and len(line) <= 140)


def chooseFile(directory, filetype = "*.txt"):
    files = glob(os.path.join(directory, filetype))
    return choice(files)
    

def chooseLine(chosenFile, filetype = "*.txt"):
    if os.path.isdir(chosenFile):
        chosenFile = chooseFile(chosenFile, filetype)
    
    f = open(chosenFile)
    
    index = 1.0
    chosenLine = ''
    for line in f.readlines():
        line = line.strip()
        if isSuitable(line):
            if random() < 1 / index:
                chosenLine = line
            index += 1.0
            
            
    return chosenLine
