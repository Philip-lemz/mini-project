import random

def guess_the_number():
    number = random.randint(1, 50)
    guesses = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        guesses += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Congratulations! You guessed the number in {guesses} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
