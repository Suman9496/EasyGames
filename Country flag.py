import random

def get_random_flag():
    # A simple list of countries and their flags for demonstration purposes
    flags = {
        "Italy": "🇮🇹",
        "France": "🇫🇷",
        "Germany": "🇩🇪",
        "Spain": "🇪🇸",
        "United States": "🇺🇸",
        "United Kingdom": "🇬🇧",
        "Canada": "🇨🇦",
        "Japan": "🇯🇵",
        "Australia": "🇦🇺",
        "Brazil": "🇧🇷"
    }

    country = random.choice(list(flags.keys()))
    return country, flags[country]

def play_guess_the_flag():
    print("Welcome to Guess the Country Flag!")
    print("Try to guess the country associated with the displayed flag.")

    correct_guesses = 0
    max_rounds = 5

    for _ in range(max_rounds):
        country, flag = get_random_flag()

        print(f"\n{flag}")
        user_guess = input("Enter your guess: ").strip().title()

        if user_guess == country:
            print("Correct! Well done.")
            correct_guesses += 1
        else:
            print(f"Sorry, the correct answer is {country}.")

    print(f"\nGame over! You got {correct_guesses} out of {max_rounds} correct.")

if __name__ == "__main__":
    play_guess_the_flag()
