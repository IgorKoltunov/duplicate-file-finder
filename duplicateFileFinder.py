""" Program outputs a list of duplicate files recursively searching
    down through given directory.
"""

import os
import filecmp


def create_file_paths_list(rootDir):
    """Create a list of full file paths."""
    filePathsList = []
    for dirPath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            if fileName:
                filePathsList.append(os.path.join(dirPath, fileName))
    return filePathsList

def duplicates_in_list(filePathsList):
    """Compare every file to every other file and list duplicates"""

    comparedList = []
    duplicatesList = []

    for file in filePathsList:
        for fileOther in filePathsList:
            isDifferent = filecmp.cmp(file, fileOther, shallow=False)
            if isDifferent and file != fileOther and file not in comparedList:
                duplicatesList.append([file, fileOther])
                comparedList.append(fileOther)
    return duplicatesList

def main():

    filePathsList = create_file_paths_list('/Users/igor/Documents/Projects/python/examples')
    duplicatesList = duplicates_in_list(filePathsList)

    for x, y in duplicatesList:
        print(x, y, sep=',')

main()
