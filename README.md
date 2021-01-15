# python-intro-file-management

This is a simplistic exploration of the python file directory. My goal was to learn how to use python to edit, retrieve, remove and add files/ folders in an unknown directory.
The code that is run throughout this repository is only going to be helpful as a reference. It has all been done before and is not something new but I hope if anyone stumbles
across this it could be helpful for whatever they are looking for.

The directory is specified through the os.environ path. Importing os is crucial to this working. That path is opened as, "c:\\Users\ CURRENT USER NAME \" further specifications
to the file path are given after the environ call. The theory behind this is that if someone downloadeds your code the file will be in "c:\\Users\ CURRENT USER NAME \ downloads"
and if you can access the file from this directory you can create/ move files to the desktop, or virtually anywhere you'd like.
