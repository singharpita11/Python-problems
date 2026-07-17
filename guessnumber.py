import random

def number_guess():
    secret_number=random.randint(1,50)
    attempts = 0

    print("Welcome to the Guess Number Game!")
    print("Choose a number between 1 and 50")
    print("-" * 30)

    while True:
      try:
          guess = int(input("Guess a number:"))
      except ValueError:
         print("Invalid number! Try again.\n")
         continue

      attempts += 1

      if guess < secret_number:
           print("Too low! \n")
      elif guess > secret_number:
            print(" Too high! \n")
      else:
            print(f"\n  Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            break

if __name__ == "__main__":
          number_guess()



