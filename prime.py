def is_prime(n):

    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) +1):
      if n % i == 0:
         return False
      
      return True 
    
def main():
   try:
      num = int (input("Enter a number:"))
   except ValueError:
        print("Invalid Input: Please enter a valid integer")
        return
   
   if is_prime(num):
       print(f"{num} is a prime number.")
   else:
       print(f"{num} is not a prime number.")


if __name__ == "__main__":
    main()

       