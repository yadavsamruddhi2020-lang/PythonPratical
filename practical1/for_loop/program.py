# print natural no upto n

# n = int(input("enter the number:"))
# for i in range(1,n+1) :
#     print(i)

# print even upto n

# n=int(input("enter num"))
# for i in range(0,n+1):
#     if i%2==0:
#         print(i)
        

# # print odd numbers
# n=int(input("enter num"))
# for i in range(0,n+1):
#     if i%2!=0:
#         print(i)


# print 4 16 36 64 100

# n=int(input("enter num:"))
# for i in range (1,n+1):
#     if i%2==0:
#         print(i*i)


# print 1 2 4 8 16 32 -----n^2

# n=int(input("enter num:"))
# for i in range (n):
#     print(2**i," ")

# A B C
# A B C
# A B C
# for i in range(3):
#     for j in range(3):
#         print(chr(65+j),end=" ")
#     print()


# A
# A B
# A B C
# A B C D
# A B C D E

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()


# A B C D
# A B C
# A B
# A
# n=int(input("enter n:"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# n =int(input("enter n:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 1 2 3
# 1 2
# 1
n=int(input("enter n:"))
for i in range (1,n+1):
    for j in range (i):
        print(i,end=" ")
    print()



