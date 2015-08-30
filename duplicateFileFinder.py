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
                fullPath = os.path.join(dirPath, fileName)
                if not os.path.islink(fullPath):
                    filePathsList.append(fullPath)
    return filePathsList


def duplicates_in_list(filePathsList):
    """Compare every file to every other file and list duplicates"""

    comparedList = []
    duplicatesList = []
    numFiles = len(filePathsList) - 1
    for index, file in enumerate(filePathsList):
        for fileOther in filePathsList:
            isDifferent = filecmp.cmp(file, fileOther, shallow=True)
            if isDifferent and file != fileOther and file not in comparedList:
                duplicatesList.append([file, fileOther])
                comparedList.append(fileOther)
        print('\r' + 'Now comparing file', index, 'of', numFiles, end='')
    print('')
    return duplicatesList


def main():

    if os.path.isfile('results.csv'):
        return print('Error: results.csv is already present. Delete or rename first')

    filePathsList = create_file_paths_list('/Volumes/MANUAL BKUP/FreeAgentComprehensiveBackup')
    duplicatesList = duplicates_in_list(filePathsList)

    resultsFile = open('results.csv', 'w')

    for file, fileOther in duplicatesList:
        print(file, fileOther, sep=',', file=resultsFile)

main()
