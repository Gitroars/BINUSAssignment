import os

# os.chdir("")

# myFile = open("info.txt","r")
# fileContents=myFile.read() #returns a string
# print("FileContents: ",fileContents," ",myFile.tell())
# print()
# myFile.close()
# myFile = open("info.txt","r")
# fileContents2=myFile.read()
# print("FileContents2: ",fileContents2," ",myFile.tell())

# myFile = open("info.txt","r")
# # line=myFile.readline()
# lineList = myFile.readlines()
# # print(line)
# # for line in lineList:
# #     print(line,sep="",end="")
# for line in myFile:
#     print(line, sep="", end="")

outputFile = open("info.txt","w")
a=1
b="this"
c=[13,4.5]
d=(1,2,3,4,5)
#choose one of two methods
outputFile.write("{}{}{}\n".format(a,b,c,d))
print(a,b,c,d,file=outputFile)
#close
outputFile.close()

out1=open("out1.txt","w")
out2=open("out2.txt","w")

v1=["one","two","three"]
v2=("one\n","two\n","three\n")

out1.writelines(v1)
out2.writelines(v2)
out1.close()
out2.close()

