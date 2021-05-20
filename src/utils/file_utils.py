# **************************************************
#  * file_utils.py
#  *
#  * Author:    Ileana Streinu
#  * Author:    TODO: add Your name here - only if you contributed to this file
#  * 
#  * Date:
#  * Created:          03/09/21  Ileana
#  * Last modified:    03/31/21  Ileana
#  * Last modified:    03/31/21  TODO: add the date you modified this file
#  *
#  * Library of file-related utilities for the 
#  * CSC334 python midterm project
#  **************************************************

import os,sys
from pathlib import Path

#----------------
#
# Ileana
#
#----------------

#----------------
# Paths and names
#----------------
def getFileName(filePath):
    return os.path.basename(filePath)    
def fixFolderPath(folderPath):
    if folderPath[-1] != '/':
        folderPath+= '/'
    return folderPath
    
# Example: path = "Data/Cif/1za7.cif" --> extracted = "1za7"    
def extractFileName(input_file):
    newFileName = input_file.split("/")[-1].split(".")[0]

    return newFileName
    
def makeOutputFileNameAndPath(inputFilePath,folderPath,suffix):      
    name = Path(inputFilePath).stem
    # print("name = " + name)
    ext = Path(inputFilePath).suffixes[0]
    # print("ext = " + ext)
    newFileName = name + "_" + suffix + ext
    outputFilePath = os.path.join(folderPath, newFileName)
    # print("outputFilePath = " + outputFilePath)
    
    return outputFilePath     
def makeNewFileNameAndPath(inputFilePath,folderPath,suffix,newExt):      
    name = Path(inputFilePath).stem
    # print("name = " + name)
    ext = Path(inputFilePath).suffixes[0]
    # print("ext = " + ext)
    if suffix == "":
        newFileName = name + newExt
    else:
        newFileName = name + "_" + suffix + newExt
        
    outputFilePath = os.path.join(folderPath, newFileName)
    # print("outputFilePath = " + outputFilePath)
    
    return outputFilePath   

#----------------
# Extensions for file names
# Used for processed cif files
# e.g. a cif file w/o water molecule gets the suffix _wow (w/o water)
#
# TODO: add here similar functions that will make new file names 
#       for your processed files
#----------------

def makeWoWaterFilePath(inputFilePath,folderPath):
    woWaterFilePath = makeOutputFileNameAndPath(inputFilePath,folderPath,"wow")
    return woWaterFilePath

    
#----------------
# Create folder
#----------------     
# General utility to create a folder if not present 
# also make sure output path ends with a '/'   
def createFolderIfNotPresentOrQuit(folderPath):
    if os.path.exists(folderPath):
        if not os.path.isdir(folderPath):
            print("folderPath="+folderPath+" exists but is not a folder")
            quit()
    else: 
        try:
            os.mkdir(folderPath) 
        except IOError:
            print("Folder folderPath="+folderPath+" cannot be created")
            sys.exit(-1)
    # make sure output path ends with a '/'
    return fixFolderPath(folderPath) 
