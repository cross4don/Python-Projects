''' A simple command-line calculator that takes two numbers and an operator(+,-,*,/) from the user and displays the result. '''

def calculator():
    print("=== Command Line Calculator ===")
    print("Operators: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        userInput = input("Enter operator (+, -, *, /) or 'exit' : ").strip()
        if userInput.lower() == 'exit':
            print("Goodbye!")
            break

        if userInput not in ('+', '-', '*', '/'):
            print("Invalid Input! Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number: Try again.\n")
            continue

        if userInput == '+':
            result = num1 + num2
        elif userInput == '-':
            result = num1 - num2
        elif userInput == '*':
            result = num1 * num2
        else:
            if num2 == 0:
                print("Error: Division by zero!\n")
                continue
            result = num1 / num2

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

    