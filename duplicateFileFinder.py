""" Program outputs a list of duplicate files recursively searching
    down through given directory.
"""

import os
import filecmp


rootDir = '/kunden/homepages/11/d251762937/htdocs/proj/python/examples'
filePathList = []
comparedList = [] 

# Create a list of full file paths.
for dirName, subdirList, fileList in os.walk(rootDir):
    for file in fileList:
        if file:
            filePathList.append(dirName + '/' + file)

# Compare every file to every other file.            
for file in filePathList:
    for fileOther in filePathList:
        isDifferent = filecmp.cmp(file, fileOther, shallow=False)
        if isDifferent and file != fileOther and file not in comparedList:
            print(file, fileOther, sep=',')
            comparedList.append(fileOther)
