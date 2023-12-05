import random


def choose_movie():
    movies = [
        "The Shaw shank Redemption",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Forrest Gump",
        "Schindler's List",
        "The Lord of the Rings",
        "Inception",
        "The Matrix",
        "Titanic"
    ]
    return random.choice(movies).upper()


def display_movie(movie, guessed_letters):
    display = ""
    for letter in movie:
        if letter.isalpha() and letter.upper() in guessed_letters:
            display += letter
        elif letter.isspace():
            display += " "
        else:
            display += "_"
    return display


def play_hangman_movie_edition():
    movie_to_guess = choose_movie()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman Movie Edition!")

    while incorrect_guesses < max_attempts:
        print("\nAttempts left:", max_attempts - incorrect_guesses)
        display = display_movie(movie_to_guess, guessed_letters)
        print(display)

        guess = input("Guess a letter: ").upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in movie_to_guess:
                print("Correct!")
                guessed_letters.add(guess)
            else:
                print("Incorrect!")
                incorrect_guesses += 1
        else:
            print("Please enter a valid single letter.")

        if all(letter.isalpha() and letter.upper() in guessed_letters for letter in movie_to_guess):
            print("Congratulations! You guessed the movie:", movie_to_guess)
            break

    if not all(letter.isalpha() and letter.upper() in guessed_letters for letter in movie_to_guess):
        print("Sorry, you ran out of attempts. The movie was:", movie_to_guess)


if __name__ == "__main__":
    play_hangman_movie_edition()
