# take input of string and display length without using len()
s = input("Enter a string: ")
count = 0
for i in s:
    count += 1
print("Length of the string is:", count)

# count no of vowels consonants digits space and special characters in a string
s=input("Enter a string: ")
vowels=0    
consonants=0
digit=0
space=0
special_char=0
for i in s:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        special_char += 1


# reverse string without using built-in functions
s = input("Enter a string: ")
reversed_string = ""
for i in range(len(s)-1, -1, -1):
    reversed_string += s[i]

# palindrome check without using built-in functions
s = input("Enter a string: ")
cleaned_string = ""
for i in s:
    if i.isalnum():
        cleaned_string += i.lower()

# uppercase and lowercase count
uppercase = 0
lowercase = 0
for i in s:     
    
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1

# replace charcters
s = input("Enter a string: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
modified_string = ""
for i in s:
    if i == old_char:
        modified_string += new_char
    else:
        modified_string += i

# remove spaces
s = input("Enter a string: ")
no_space_string = ""
for i in s:
    if not i.isspace():
        no_space_string += i

# frequency of char
s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency of", ch, "=", count)


# first and last char
s = input("Enter a string: ")

print("First Character:", s[0])
print("Last Character:", s[-1])


# ascii values
s = input("Enter a string: ")

for i in s:
    print(i, "=", ord(i))


# word count 
s = input("Enter a string: ")
words = s.split()
print("Number of words:", len(words))


# longest word
s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for i in words:
    if len(i) > len(longest):
        longest = i
print("Longest Word =", longest)

# shorstest word    
s=input("enter sentence:")
words=s.spilt()
shorstesr=words[0]
for i in words:
    if len(i)<len(shorstesr):
        shorstesr=i
print("Shortest Word =",shorstesr)


# tile case
s = input("Enter a sentence: ")

print("Title Case:", s.title())

# duplicate characters
s = input("Enter a string: ")

printed = ""

for i in s:
    if s.count(i) > 1 and i not in printed:
        print(i)
        printed += i


# character frequency
s = input("Enter a string: ")

printed = ""

for i in s:
    if i not in printed:
        print(i, "=", s.count(i))
        printed += i