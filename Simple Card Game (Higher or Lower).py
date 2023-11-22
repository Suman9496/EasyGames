import random


def card_game():
    print("Welcome to the Higher or Lower Card Game!")

    user_card = random.randint(1, 10)
    computer_card = random.randint(1, 10)

    print(f"Your card is: {user_card}")

    while True:
        guess = input("Do you think the next card will be higher or lower? (h/l): ").lower()

        next_card = random.randint(1, 10)
        print(f"The next card is: {next_card}")

        if next_card == user_card:
            print("It's a draw! Try again.")
        elif (next_card > user_card and guess == 'h') or (next_card < user_card and guess == 'l'):
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Sorry, you guessed wrong. Game over.")
            break


if __name__ == "__main__":
    card_game()
