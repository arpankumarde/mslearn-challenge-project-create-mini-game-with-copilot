# Make a rock, paper, scissor game based on the given instructions:
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The mini game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        opponent_choice = random.choice(options)

        print(f"Player chooses: {player_choice}")
        print(f"Opponent chooses: {opponent_choice}")

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'paper' and opponent_choice == 'rock') or \
             (player_choice == 'scissors' and opponent_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            opponent_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Opponent score: {opponent_score}")

play_game()
