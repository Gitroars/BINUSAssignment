import os
os.chdir("C:\Git Projects\BINUSAssignment\2021 , Odd Semester\Algorithm and Programming\November\Week2\info.txt")
myFile = open("info.txt","r")
fileContents = myFile.read()
print(fileContents)
