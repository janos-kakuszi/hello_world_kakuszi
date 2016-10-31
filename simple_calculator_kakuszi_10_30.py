import sys

def main():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    try:
        num1 = float(input("Enter a number or a letter to exit"))
    except ValueError:
        print("Bye")
        sys.exit()

    choice = input("Enter an operation")

    try:
        num2 = float(input("Enter second number or a letter to exit"))
    except ValueError:
        print("Bye")
        sys.exit()

    if choice == '+':
            print("Result:",num1,"+",num2,"=",add(num1,num2))

    elif choice == '-':
            print("Result:",num1,"-",num2,"=",subtract(num1,num2))

    elif choice == '*':
            print("Result:",num1,"*",num2,"=",multiply(num1,num2))

    elif choice == '/':
            print("Result:",num1,"/",num2,"=",divide(num1, num2))

    else:
        print("Input operation failure")
        sys.exit()

    main()

main()
