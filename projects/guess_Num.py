import random

n = random.randint(1, 100)
guesses = 0

while True:
    a = int(input("Guess the number: "))
    guesses += 1

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"You have guessed the number {n} correctly in {guesses} attempts")
        break
