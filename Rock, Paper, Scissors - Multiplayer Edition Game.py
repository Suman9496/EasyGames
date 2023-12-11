def play_rps_multiplayer():
    print("Welcome to Rock, Paper, Scissors - Multiplayer Edition!")
    print("Two players will take turns choosing between rock, paper, and scissors.")
    print("The winner will be determined based on the rules of the game.")

    while True:
        player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
        player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

        if player1_choice in ["rock", "paper", "scissors"] and player2_choice in ["rock", "paper", "scissors"]:
            if player1_choice == player2_choice:
                print("It's a tie! Play again.")
            elif (player1_choice == "rock" and player2_choice == "scissors") or \
                 (player1_choice == "paper" and player2_choice == "rock") or \
                 (player1_choice == "scissors" and player2_choice == "paper"):
                print("Player 1 wins!")
                break
            else:
                print("Player 2 wins!")
                break
        else:
            print("Invalid choices. Please enter rock, paper, or scissors.")

if __name__ == "__main__":
    play_rps_multiplayer()
