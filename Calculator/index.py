def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Select the operation you want: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

x = "yes"
while x == "yes":
    choice = input("Enter operation choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    x = input("Enter yes to continue to do again operation: ")
    if x.lower() != "yes":
        break
