import os
import shutil

folderName = 'TestFolder'  # Establishes a folder name for directory
path = os.path.join(os.path.join(os.environ['USERPROFILE']),
                    'Python', 'python-intro-file-management', 'directory', folderName)
# Taps into the users default profile directory with os.environ
print('Target path found. . .', path)

fileName = 'test'
fileType = '.txt'
file = fileName + fileType
# Specifies the file name for locating the file path
# File and folder name are known as they are created earlier in repository
print('Found file,', file)

filePath = os.path.join(path, file)  # Finds the file by directory
os.remove(filePath)  # Deletes file from within folder
print('Removing file,', file, "from directory", filePath)

shutil.rmtree(path)  # Deletes folder
print('Removing folder,', folderName, "from", path)
print('\n~~~ All files and folders removed sucessfully. ~~~')

# The deletion of the folder must be executed last otherwise,
# 'error: folder is not empty' error occurs.
