from pathlib import Path
import os
import shutil

dir_to_scan = Path("./")  # sets directory to scan to be current file location
p = Path(dir_to_scan)  # sets p to directory

print(list(p.rglob('**/*.*')))  # print a WindowsPath of full directory
# print(list(p.rglob('*.txt'))) # will print a WindowsPath of only text files in
# directory

# for a more sleek presentaiton of data the os.scandir will work
# however, only do this if you want to return the items as DirEntry objects

folders = []
files = []

for entry in os.scandir(p):  # callback to p to get directory
    if entry.is_dir():
        folders.append(entry)  # grabs folder
    elif entry.is_file():
        files.append(entry)  # grabs files
print("Folders - {}".format(folders))
print("Files - {}".format(files))
# sorts the folders and files and prints on seperate lines

# to parse through all subdirectories use os.walk

for dirName, subdirList, fileList in os.walk(p):
    print('Found directory: %s' % dirName)  # retrieves directory and returns name
    for fname in fileList:  # retrieves files and returns name
        print('\t%s' % fname)
# the print function here returns a str instad of a Path object again
