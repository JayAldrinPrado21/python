print("Hello, World!")


def add(a, b):
    return float(a) + float(b)

def multiply(a, b):
    return float(a) * float(b)



while True:
    print("1. Addition")
    print("2. Multiplication")
    print("3. exit")
    operation = input("Enter the operation number (1, 2, or 3): ")

    if operation == "1":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        sum = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {sum}")
    elif operation == "2":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        product = multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {product}")
    elif operation == "3":
        print("Exiting...")
        break
    else:
        print("Invalid operation selected.")







