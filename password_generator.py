import random

print("Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?0123456789"

number = input("Input amount of password to generate: ")

number = int(number)

length = input("input your password length: ")
length =int (length) 

print("\n Here are your passwords: ")

for pwd in range(number):
    passwords = ''
    for C in range(length):
        passwords += random.choice(characters)
        
    print(passwords)