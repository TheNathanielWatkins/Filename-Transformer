# This Python file uses the following encoding: utf-8

# IPND Stage 3 Mini Project - Nathaniel Watkins

import os

def renameFiles():
    savedPath = os.getcwd()
    fileList = os.listdir(savedPath)
    print "Current Working Directory is: " + savedPath
    print "And the relevant file names are: " + str(fileList)
    os.chdir(savedPath)
    characters = raw_input("Type in all the characters that you'd like completely removed from the filenames: ")
    for fileName in fileList:
        print "Old Name - " + fileName
        print "New Name - " + fileName.translate(None, characters)
        os.rename(fileName, fileName.translate(None, characters))
    os.chdir(savedPath)

renameFiles()
