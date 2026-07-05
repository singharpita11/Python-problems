balance = 10000

def atm_simulation():
      global balance
      print("Welcome to the ATM")

      while True:
            print("MENU: /n")
            print("1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")

            choice = int(input("Enter your choice(1-4): "))

            if choice == 1:
               print(f"Your balance is ₹{balance}")
            elif choice == 2:
               amount = float(input("Enter the amount you want to deposit: ₹"))
               balance += amount
               print(f"Deposited ₹{amount}. New Balance: ₹{balance}")
            elif choice == 3:
                amount = float(input("Enter the amount you want to withdraw: "))
                if amount > balance:
                   print("Insufficient Balance!")
                else:
                  balance -= amount
                  print(f"Withdraw ₹{amount}.New Balance:₹{balance}")

            elif choice == 4:
               print("Thank you for using ATM. Goodbye!")
               break
            else:
                 print("Invalid Choice")

atm_simulation()

