import random

options = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

for round_num in range(1, 6):
    print(f"\n Round {round_num} ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
2
    user_choice = input("Enter your choice (1-3): ")

    if user_choice == "1":
        user = "Rock"
    elif user_choice == "2":
        user = "Paper"
    elif user_choice == "3":
        user = "Scissors"
    else:
        print("Invalid choice! Skipping this round.")
        continue

    computer = random.choice(options)
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\n Final Result ")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print(" You are the overall winner!")
elif computer_score > user_score:
    print("Computer is the overall winner!")
else:
    print("It's an overall tie!")