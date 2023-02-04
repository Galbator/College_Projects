"""
    Python Version: 3.11.0

    Description: Converts a '.pf2' file to a '.csv'

    Output: Output '.csv' File will be in the Same 'Folder' / 'Directory' as the Original '.pf2' File

    Dependencies: 
        FileUtils.py - Must be in the same 'Folder' / 'Directory' as this file

    Author: 
        run.py - Mason Motschke

    Contributors:
        FileUtils.py - Tom Stokke
"""
from csv import DictWriter
from time import sleep
from FileUtils import selectOpenFile as SOF

def getFieldNames (fieldNameLine):  # Returns a List of the Column Headers / Field Names of the CSV

    fieldNameLine = fieldNameLine[7:-1].strip().split(', ')
    return fieldNameLine

def buildRow (headers, data):  # Returns a Dictionary Representing the Next Row to Print to the CSV File

    row = {}; i = 0
    for head in headers:
        row[head] = data[i]
        i += 1
    return row

def main ():
    try:
        try:
            fileName = SOF(msg='Choose a File: ', title='Files', default='*', filetypes='*.pf2')

            test = fileName.strip().split('.')
            if (test[-1] != 'pf2'): raise TypeError

            selectedFile = open(fileName)
        except TypeError:
            print("\n\n\n\n\n -- Error: Invalid File Extension\n\n\n      - Valid Extensions: '.pf2'\n\n\n -- File Conversion Canceled\n\n\n -- Closing Application...\n\n\n\n\n\n")
            sleep(5); return

        print("\n" * 5); print(" -- File Selected: " + str(fileName) + "\n\n"); sleep(3)

        temp = fileName.strip().split('.')
        temp.append('csv')
        temp.pop(-2)
        csvFileName = '.'.join(temp)

        print(" -- CSV File Name: " + str(csvFileName) + "\n\n\n -- Converting...\n\n"); sleep(3)

        data = []; i = 0;
        for line in selectedFile:
            if (line.startswith('Data:')):
                fieldNameLine = line.strip();
            if (line[0].isnumeric()):
                line = line.strip().split(', ')
                data.append(line)
                i += 1
        selectedFile.close()

        with open(csvFileName, 'w', newline='') as file:
            fieldNames = getFieldNames(fieldNameLine)
            writer = DictWriter(file, fieldnames=fieldNames)

            writer.writeheader()
            for j in range(0, i):
                writer.writerow(buildRow(fieldNames, data[j]))
        file.close()
        
        print(" -- Success: File Converted to '.csv'\n\n\n -- Closing Application...\n\n")
        sleep(5); return
    except:
        print(" -- Error: An Error has Occured!\n\n\n -- File Conversion Cancelled\n\n\n -- Closing Application...\n\n")
        sleep(5); return

main();
