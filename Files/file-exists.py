import os, sys

fname = input("Enter your file name: ")

if os.path.isfile(fname):
    f = open(fname, "r")
else:
    print(fname, "File name does not exist!")
    sys.exit()
print("File content is: ")
print(f.read())
f.close()