import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("\n---NUMBER GUESSING GAME---")
while is_running:
    guess = (input(f"Guess a number between {lowest_num} and {highest_num}: "))

    if guess.isdigit():
        guess = int(guess)

        if guess > highest_num or guess < lowest_num:
            print(f"Please enter a number between {lowest_num} and {highest_num}.")
        elif guess == answer:
            guesses += 1
            print(f"Congratulations! The number {answer} is the correct answer!")
            print(f"I")
            is_running = False
        elif guess < answer:
            guesses += 1
            print(f"{guess} is too low!")
        elif guess > answer:
            guesses += 1
            print(f"{guess} is too high!")
        else:
            print("Please type a number.")