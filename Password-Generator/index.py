import random
def generate_password(length, complexity):
    if complexity == "low":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif complexity == "medium":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif complexity == "high":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?~"
    else:
        print("Invalid complexity level. Defaulting to low complexity.")
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("PASSWORD GENERATOR")
    print("-------------------")
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a valid length greater than zero.")
        return
    
    complexity = input("Enter complexity level (low/medium/high): ").lower()
    password = generate_password(length, complexity)
    print("Generated Password:", password)

main()
