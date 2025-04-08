file = open("java.text", "r")
data = file.read() 
print(data)
file = open("java.text", "w")
data = file.write("This is a java assignment file")
print(data)

file = input("filename: ")
try:
    with open("java.text", "r") as file:
        print("file opened")
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not Found. Please check file name.")