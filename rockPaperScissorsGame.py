import random

options = ("rock", "paper", "scissors")
score_cpu = 0
score_player = 0
is_running = True

print("\n----ROCK, PAPER, SCISSORS----")

while is_running:

    player = None
    cpu = random.choice(options)

    while player not in options:
        player = input(f"Choose your play. Rock, paper, or scissors?: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {cpu}")

    if player == cpu:
        print("Tie.")
    elif player == "rock" and cpu == "scissors":
        score_player += 1
        print(f"Player wins!")
    elif player == "paper" and cpu == "rock":
        score_player += 1
        print(f"Player wins!")
    elif player == "scissors" and cpu == "paper":
        score_player += 1
        print(f"Player wins!")
    else:
        score_cpu += 1
        print(f"Computer wins!")

    if not input("Play again? (y/n): ").lower() == "y":
        is_running = False

print("\n----SCORE----")
print(f"Player: {score_player}")
print(f"Computer: {score_cpu}")
print("\nThanks for playing!")