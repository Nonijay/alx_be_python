# Creating an arithmetic operations 

def perform_operation(num1, num2, operation):
    op = operation.strip().lower()

    if op == 'add':
        return (num1 + num2)

    elif op == 'subtract':
        return (num1 - num2)

    elif op == 'multiply':
        return (num1 * num2)

    elif op == 'divide':
        num2 == 0
        print("Error: cannot be divided by 0")
        return (num1 / num2)

    else:
        print(f"Error: Enter a valid {perform_operation}")

print(f"Arithmetic operations success")
