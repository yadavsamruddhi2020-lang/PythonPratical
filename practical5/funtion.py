# factorial

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print (factorial(5))

# prime no
# def prime(n):
#     if n>2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# num=int(input("enter num:"))
# if prime(num):
#     print("prime no")
# else:
#     print("not prime ")


# reverse string
# def reverse(s):
#     return s[::-1]
# print(reverse("python"))


# palindrome
# def palindrome(n):
#     original = n
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10
#     return original == reverse
# num = int(input("Enter a number: "))
# if palindrome(num):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# count number
def count_num(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
num=int(input("enter num:"))
print(count_num(num))