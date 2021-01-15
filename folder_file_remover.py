import os
import shutil

folderName = 'TestFolder'
path = os.path.join(os.path.join(os.environ['USERPROFILE']),
                    'Python', 'python-intro-file-management', 'directory', folderName)
fileName = 'test'
fileType = '.txt'
file = fileName + fileType

filePath = os.path.join(path, file)
print(filePath)
os.remove(filePath)

shutil.rmtree(path)
