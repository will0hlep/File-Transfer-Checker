'''
Script for checking that all files in the origin folder have been successfully copied to the destination folder.
'''

import os #python standard library package for file and directory operations
import sys #python standard library package for system-specific parameters and functions

if len(sys.argv) != 3: #checks for the correct number of inputs
    print("Usage: python3 transfer_check.py <ORIGIN_PATH> <DESTINATION_PATH>") #prints a helpful hit if the wrong number of inputs is detected
    sys.exit(1) #exits the script with an error code: 1

ORIGIN_PATH = sys.argv[1] #retrieve origin folder path from the command
DESTINATION_PATH = sys.argv[2] #retrieve destination folder path from the command

files_checked = 0 #initialise a counter for the number of files checked
missing_files_and_warnings = [] #list of warnings and missing files
origin_files = list(os.walk(ORIGIN_PATH, onerror=lambda e: missing_files_and_warnings.append(e))) #retrieve a list of all files and folders in the origin folder and appends warnings to missing_files_and_warnings

for origin_dir, _, origin_files in origin_files: #loop through all directories listed in origin_files
    for origin_file in origin_files: #loop through all files in the current directory
        origin_file_path = os.path.join(origin_dir, origin_file) #construct the full path of the current file
        relative_path = os.path.relpath(origin_file_path, ORIGIN_PATH) #fines the file path relative to the origin path
        destination_file_path = os.path.join(DESTINATION_PATH, relative_path) #construct the corresponding path in the destination folder

        if not os.path.exists(destination_file_path): #check if the file exists in the destination folder
            missing_files_and_warnings.append(origin_file_path) #if the file does not exist, add it to the list of missing files

        files_checked += 1 #increment files_checked counter

if missing_files_and_warnings != []: #checks if any files are missing
    print('missing files detected') #prints warning to console
    with open(".\\report.txt", 'w', encoding="utf-8") as output: #open a text file to write the list of missing files
        for row in missing_files_and_warnings: #loop through the list of missing files
            output.write(str(row) + '\n') #write each warning or missing file path to the text file, followed by a newline character
else: print('all files transfered') #prints success message to console

print('total files checked: ' + str(files_checked)) #print the total number of files checked to the console
