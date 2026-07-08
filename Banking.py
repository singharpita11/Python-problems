account = {
    "name": None,
    "balance": 0,
    "created": False
}
def create_account():
    if account["created"]:
        print("Account created")
        return
    name = input("Enter your name: ")
    i_deposit = float(input("Enter initial deposit amount: ₹"))
    account["name"] = name
    account["balance"] = i_deposit
    account["created"] = True
    print(f"Account created for {name}! Balance: ₹{i_deposit}")

def deposit():
    if not account["created"]:
        print("No account found. Create one first.")
        return
    amount = float(input("Enter amount to deposit: ₹"))
    account["balance"] += amount
    print(f"Deposited ₹{amount}. New balance: ₹{account['balance']}")


def withdraw():
    if not account["created"]:
        print("No account found. Create one first.")
        return
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > account["balance"]:
        print("Insufficient balance!")
    else:
        account["balance"] -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{account['balance']}")
def check_balance():
    if not account["created"]:
        print("No account found. Create one first.")
        return
    print(f"Account Holder: {account['name']}")
    print(f"Balance: ₹{account['balance']}")

def menu():
    print(" \n Welcome to the Mini Banking System")
    print(" 1. Create an account")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Check Balance")
    print(" 5. Exit")

def main():
    while True:
        menu()
        choice =input("Enter your choice: ")

        if choice == '1':
            create_account()
        if choice == '2':
            deposit()
        if choice == '3':
            withdraw()
        if choice == '4':
            check_balance()
        if choice == '5':
            print("Thanks for using mini banking system")
            break
        else:
            print("Invalid choice! Please enter a valid choice ")
main()