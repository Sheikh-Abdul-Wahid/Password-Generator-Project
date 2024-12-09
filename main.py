import string
import random

# Prepare character set
s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.punctuation
s4 = string.digits

s = []
s.extend(list(s1) + list(s2) + list(s3) + list(s4))
random.shuffle(s)

# Maximum allowable length
max_length = len(s)

# Input validation loop
while True:
    passlen = input("Enter the length of your password: ")
    if not passlen.isdigit():
        print("Invalid Input. Please enter a positive integer!")
        continue
    passlen = int(passlen)
    if passlen <= 0:
        print("Invalid Input. Length cannot be negative. Please try again!")
        continue
    if passlen > max_length:
        print(f"Password length exceeds the maximum limit ({max_length}). Please try again!")
        continue
    break

# Password generation
print("Your Generated Password:")
print("".join(s[0:passlen]))      
        