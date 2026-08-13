# anagram check 
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if sortes(s1)==sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# remove duplicate characters
s=input("Enter a string: ")
result = ""
for char in s:
    if char not in result:
        result += char
print("String after removing duplicates:", result)

# substring search
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")


# Count Occurrences of a Word
s = input("Enter a sentence: ")
word = input("Enter word: ")

count = s.split().count(word)

print("Count =", count)


# Password Validator
password = input("Enter password: ")

upper = lower = digit = special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")


# 22. Run-Length Encoding
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)


# 23. String Compression
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

if len(result) < len(s):
    print(result)
else:
    print(s)


# 24. Most Frequent Character
s = input("Enter string: ")

max_char = s[0]
max_count = s.count(s[0])

for ch in s:
    if s.count(ch) > max_count:
        max_char = ch
        max_count = s.count(ch)

print("Most Frequent Character:", max_char)


# 25. Second Most Frequent Character
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Second Most Frequent:", items[1][0])


# 26. Caesar Cipher (Encryption)
text = input("Enter text: ")
shift = 3

result = ""

for ch in text:
    if ch.isalpha():
        result += chr(ord(ch) + shift)
    else:
        result += ch

print("Encrypted:", result)


# 27. Email Validator
email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
# 
# 
# 28. Word Frequency Dictionary
s = input("Enter paragraph: ")

words = s.split()

for word in words:
    print(word, "=", words.count(word))

    
# 29. Sentence Reversal
s = input("Enter sentence: ")

words = s.split()

print("Reversed:", " ".join(words[::-1]))


# 30. String Rotation
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Rotation")
else:
    print("Not Rotation")