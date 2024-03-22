import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?~"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("PASSWORD GENERATOR")
    print("-------------------")
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a valid length greater than zero.")
        return
    password = generate_password(length)
    print("Generated Password:", password)

main()
