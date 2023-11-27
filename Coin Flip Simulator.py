import random

def coin_flip():
    return random.choice(["Heads", "Tails"])

def play_coin_flip_simulator():
    print("Welcome to Coin Flip Simulator!")

    while True:
        input("Press Enter to flip the coin (or 'quit' to exit): ")
        result = coin_flip()
        print(f"The coin landed on: {result}")

        play_again = input("Flip again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for using the Coin Flip Simulator. Goodbye!")
            break

if __name__ == "__main__":
    play_coin_flip_simulator()
