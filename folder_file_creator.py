import os

path = os.path.join(os.path.join(os.environ['USERPROFILE']),
                    'Python', 'python-intro-file-management', 'directory')
# finds the directory path by desktop

name = "TestFolder"  # folder name

os.mkdir(os.path.join(path, name))
# creates a folder called 'TestFolder' at file path

folderPath = os.path.join(path, 'TestFolder')
print('Creating folder, ' + name + ", at, " + folderPath + "\nFolder Created")
# prints folder path

fileName = "test"  # determines name of file created
fileType = '.txt'  # determines type of file created

filePath = os.path.join(folderPath, fileName + fileType)
# finds directory the new file will be created at

test_file = open(filePath, "w")  # creates the file at the specified location
print('Creating file, ' + fileName + fileType + ', at ' + path + '\ ' + name)
print('File created')

fileInformation = "testing. . ."  # uses this text to write to the test file
test_file.write(fileInformation)  # writes to the test file

print('\n ~~~ Directory Sucessfully Created ~~~')
