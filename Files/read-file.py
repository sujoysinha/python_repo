file_handler = open("open-file-tmp.txt", "r")
str = file_handler.read()
print(str)
file_handler.close()