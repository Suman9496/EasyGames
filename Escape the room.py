import random

def generate_puzzles():
    puzzles = [
        "Solve a math problem: 2 + 2 = ?",
        "Find the key hidden under the chair.",
        "Decode the message: XCVI - XX = ? (Use Roman numerals)",
        "Arrange the numbers in ascending order: 5, 2, 8, 1, 3",
        "Locate a hidden switch behind the painting."
    ]
    return puzzles

def play_escape_the_room():
    puzzles = generate_puzzles()
    solved_puzzles = set()

    print("Welcome to Escape the Room!")
    print("You find yourself trapped in a mysterious room. Solve puzzles to escape!")

    while len(solved_puzzles) < len(puzzles):
        print("\nCurrent puzzles:")
        for i, puzzle in enumerate(puzzles):
            if puzzle not in solved_puzzles:
                print(f"{i + 1}. {puzzle}")

        choice = input("Enter the number of the puzzle you want to solve (or 'quit' to exit): ")

        if choice == 'quit':
            print("Thanks for playing Escape the Room. Goodbye!")
            break

        try:
            puzzle_index = int(choice) - 1
            if 0 <= puzzle_index < len(puzzles) and puzzles[puzzle_index] not in solved_puzzles:
                print("Solving puzzle:", puzzles[puzzle_index])
                solved_puzzles.add(puzzles[puzzle_index])
                print("Congratulations! Puzzle solved.")
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if len(solved_puzzles) == len(puzzles):
        print("Congratulations! You've successfully escaped the room.")

if __name__ == "__main__":
    play_escape_the_room()
