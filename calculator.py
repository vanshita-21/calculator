def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice between (1/2/3/4/5): ")

    if choice == '5':
        print("Exit the calculator.")
        break

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(n1, "+", n2, "=", add(n1, n2))
    elif choice == '2':
        print(n1, "-", n2, "=", subtract(n1, n2))
    elif choice == '3':
        print(n1, "*", n2, "=", multiply(n1, n2))
    elif choice == '4':
        print(n1, "/", n2, "=", divide(n1, n2))
    else:
        print("Invalid input")

    m = input("Do you want to perform another operation? (yes/no): ")
    if m.lower() != 'yes':
        print("Exit the calculator.")
        break
