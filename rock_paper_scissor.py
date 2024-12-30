import random

print("Welcome to the Rock, Paper, and Scissors Game!")

# Define choices in a dictionary
choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

try:
    # Player makes a choice
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n "))
    if player not in choices:
        raise ValueError("Invalid choice. Please choose 0, 1, or 2.")

    # Computer makes a random choice
    computer = random.randint(0, 2)

    print(f"Player chose {choices[player]} and Computer chose {choices[computer]}")

    # Determine the winner
    if player == computer:
        print("It's a Tie!")
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("Player Wins!")
    else:
        print("Computer Wins!")

except ValueError as e:
    print(e)
