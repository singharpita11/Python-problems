def check_even_odd(num):
    if num % 2 == 0:
        return"even"
    else:
        return"odd"
    
    def main():
        try:
            num =int(input("Enter a number:"))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return
        
        result = check_even_odd(num)
        printf(f"The number {num} is {result}.")

    if __name__ == "__main__":
        main()