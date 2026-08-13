# read the file 
# with open("data.txt","r") as file:
#     content=file.read()
#     print(content)



# write file
# with open("data.text","w") as file:
#     file.write("hello world ")

# append file
# with open("data.text","a") as file:
#     file.write("\n welcome")


# # r+
# f = open("data.txt", "r+")

# # w+
# f = open("data.txt", "w+")

# # a+
# f = open("data.txt", "a+")

# rb
# with open("data.text","rb") as file:
#     data=file.read()
#     print(data)

# wb
# data=b"good morning"
# with open("data.bin", "wb") as file:
#     file.write(data)

# # ab
# data=b"\nheyy"
# with open("data.text","ab") as file:
#     file.write(data)

# rb+
# with open("data.bin", "rb+") as file:
#     data = file.read()
#     print(data)

#     file.write(b"\nPython")

# wb+
# with open("data.bin", "wb+") as file:
#     file.write(b"Hello Python")

#     file.seek(0)       
#     data = file.read()

#     print(data) 


# ab+
# with open("data.bin", "ab+") as file:
#     file.write(b"\nHello")

#     file.seek(0)       
#     data = file.read()

#     print(data)


# x
try:
    with open("newfile.txt", "x") as file:
        file.write("Hello Python")
except FileExistsError:
    print("File already exists")