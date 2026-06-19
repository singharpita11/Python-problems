def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return(a*b)
def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed."
    return (a/b)

def main():
    print ("Simple calculator")
    print("Select operations: add, subtract, multiply, divide")
 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
 
    operation = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()
 
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation.")
        return
 
    print(f"Result: {result}")
 
 
if __name__ == "__main__":
    main()