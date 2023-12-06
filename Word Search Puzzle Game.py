import random
import string

def generate_word_search(size, words):
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Place words in random positions
    for word in words:
        direction = random.choice(["horizontal", "vertical", "diagonal"])
        if direction == "horizontal":
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
            for i in range(len(word)):
                grid[row][col + i] = word[i]
        elif direction == "vertical":
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)
            for i in range(len(word)):
                grid[row + i][col] = word[i]
        else:  # diagonal
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - len(word))
            for i in range(len(word)):
                grid[row + i][col + i] = word[i]

    # Fill remaining spaces with random letters
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(string.ascii_uppercase)

    return grid

def print_word_search(grid):
    for row in grid:
        print(" ".join(row))

def play_word_search_puzzle():
    words_to_find = ["PYTHON", "JAVA", "C", "HTML", "CSS"]
    word_search_grid = generate_word_search(10, words_to_find)
    found_words = set()

    print("Welcome to Word Search Puzzle!")
    print("Find the following words in the grid:")

    while found_words != set(words_to_find):
        print_word_search(word_search_grid)

        user_guess = input("Enter a word guess: ").upper()

        if user_guess in words_to_find and user_guess not in found_words:
            print(f"Good job! You found the word: {user_guess}\n")
            found_words.add(user_guess)
        else:
            print("Incorrect. Keep searching!\n")

    print("Congratulations! You found all the words.")

if __name__ == "__main__":
    play_word_search_puzzle()
