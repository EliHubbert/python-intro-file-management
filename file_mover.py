import shutil
from pathlib import Path
import os

source = os.path.join(os.path.join(
    os.environ['USERPROFILE']), 'Python', 'python-intro-file-management', 'directory')
# This gathers the source file, USERPROFILE allows me to reach the
# desktop's file path, could be used in applciatons and downloads too
destination = os.path.join(os.path.join(
    os.environ['USERPROFILE']), 'Python', 'python-intro-file-management', 'directory', 'sampledirectory')
# This locates the destination, a destination could be preexisting or
# created.

print("The source directory is: " + source)  # print source filepath
print("The desired destination is: " + destination)  # print destination filepath

for each_file in Path(source).glob('*.*'):
    # create a variable that stores each file in source
    print("Moving file . . .")
    print(each_file)
    # print 'moving file' and attach the variable determined above
    shutil.move(each_file, destination)
    # executes the transfer of files in source to destination folder

print("\nFile transfer complete!")  # print upon completion
