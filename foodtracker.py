expenses = []

print(" Expense Tracker ")
print("Enter expenses as: Category Amount ")
print("Type 'done' when  finished.\n")

while True:
    entry = input("Enter expense: ")

    if entry.lower() == "done":
        break

    parts = entry.split()

    if len(parts) != 2:
        print("Invalid format! Please enter like: Food 200")
        continue

    category = parts[0]
    amount = parts[1]

    if not amount.isdigit():
        print("Amount must be a number! Try again.")
        continue

    expenses.append((category, float(amount)))

# Calculate totals
total_expenses = 0
for category, amount in expenses:
    total_expenses += amount

num_expenses = len(expenses)

if num_expenses > 0:
    average_expense = total_expenses / num_expenses
else:
    average_expense = 0

# Display results
print("\n Expense Summary ")
for category, amount in expenses:
    print(f"{category}: ₹{amount}")

print(f"\nTotal Expenses: ₹{total_expenses}")
print(f"Number of Expenses: {num_expenses}")
print(f"Average Expense: ₹{average_expense:.2f}")