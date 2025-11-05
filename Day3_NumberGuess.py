import random

print("🎯 Welcome to the Number Guessing Game!")
number = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 50 (or 'q' to quit): ")
    if guess.lower() == 'q':
        print(f"You quit! The number was {number}.")
        break
    if not guess.isdigit():
        print("Enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
