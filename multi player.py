import random

def generate_target_number():
    return random.randint(1, 100)

def play_number_guessing_multiplayer():
    print("Welcome to Number Guessing - Multiplayer Edition!")
    print("Two players will take turns guessing a number between 1 and 100.")
    print("The first player to guess the correct number wins!")

    target_number = generate_target_number()
    player_turn = 1

    while True:
        guess = int(input(f"Player {player_turn}, enter your guess: "))

        if guess == target_number:
            print(f"Congratulations! Player {player_turn} guessed the correct number: {target_number}")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        player_turn = 3 - player_turn  # Switch players (1 -> 2, 2 -> 1)

if __name__ == "__main__":
    play_number_guessing_multiplayer()
