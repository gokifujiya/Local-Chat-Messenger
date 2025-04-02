import random

n = int(input("Enter the minimum number (n): "))
m = int(input("Enter the maximum number (m): "))

if n > m:
    print("Invalid range.")
else:
    answer = random.randint(n, m)
    attempts = 0
    max_attempts = 5

print(f"\nI have picked a number between {n} and {m}. You have {max_attempts} tries!")

while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == answer:
        print(f"Correct! You guessed the number in {attempts} tries.")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
if guess != answer:
    print(f"Game Over! The number was {answer}.")
    