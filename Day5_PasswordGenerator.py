# Day5_PasswordGenerator.py
import string
import random

print("🔐 Password Generator")

length = int(input("Enter password length: "))

if length < 4:
    print("Password too short! Try at least 4 characters.")
else:
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    print(f"Your generated password: {password}")
