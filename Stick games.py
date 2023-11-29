import random

def start_game():
    # Initialize the number of sticks
    sticks = 21

    # Start the game loop
    while sticks > 0:
        # Player's turn
        player_turn = True
        while player_turn:
            try:
                sticks_to_remove = int(input("Enter the number of sticks you want to remove (1, 2, or 3): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue

            if sticks_to_remove < 1 or sticks_to_remove > 3:
                print("Invalid number of sticks. Please enter a number between 1 and 3.")
            else:
                sticks -= sticks_to_remove
                print(f"You removed {sticks_to_remove} sticks.")
                player_turn = False

        # Check if the player has won
        if sticks == 0:
            print("Congratulations! You won the game!")
            return

        # Computer's turn
        computer_turn = True
        while computer_turn:
            # Generate a random number of sticks to remove
            computer_sticks_to_remove = random.randint(1, 3)

            sticks -= computer_sticks_to_remove
            print(f"The computer removed {computer_sticks_to_remove} sticks.")
            computer_turn = False

        # Check if the computer has won
        if sticks == 0:
            print("Sorry, you lost the game.")
            return

start_game()
