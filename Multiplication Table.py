def print_table(n):
    for i in range(1,11):
      print(f"{n} x {i} = {n*i}")

def main():
   try:
      num = int(input("Enter a number:"))
   except ValueError:
      print("Invalid Output: Please enter a valid integer")
      return 
   
   print_table(num)


if __name__ == "__main__":
    main()