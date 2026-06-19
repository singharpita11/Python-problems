def factorial(n):
    if n< 0:
        return None
    
    result = 1
    for i in range(1 , n+1):
        result = 1
    for i in range(1, n+1):
        result = result *1
        print(f"i={1}, result={result}")
        return result
    
def main():
    try:
        num = int (input("Enter a number: "))
    except ValueError:
        print("Invalid Input: Please enter a valid interger")
        return
    
    result = factorial(num)
    if result is None:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {result}")
        print(f"Type of result: {type(result).__name__}")  # confirms it's an int
        print(f"Number of digits in the result: {len(str(result))}")
        
if __name__ == "__main__":
    main()
