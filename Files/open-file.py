file_handler = open("open-file-tmp.txt", "r")
str = input("Enter text: ")
file_handler.write(str)
file_handler.close()