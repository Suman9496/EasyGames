import random

def generate_maze(size):
    maze = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
    maze[0][0] = 0  # Starting point
    maze[size-1][size-1] = 0  # Ending point
    return maze

def print_maze(maze):
    for row in maze:
        print(" | ".join(str(cell) for cell in row))
        print("-" * (4 * len(row) - 1))

def play_number_maze(size):
    maze = generate_maze(size)
    current_position = [0, 0]

    print("Welcome to the Number Maze!")
    print("You start at the top-left corner. Your goal is to reach the bottom-right corner.")

    while True:
        print_maze(maze)
        print(f"You are currently at position ({current_position[0]}, {current_position[1]}).")

        choices = []

        # Determine available choices based on adjacent numbers
        if current_position[0] > 0:
            choices.append(maze[current_position[0] - 1][current_position[1]])
        if current_position[0] < size - 1:
            choices.append(maze[current_position[0] + 1][current_position[1]])
        if current_position[1] > 0:
            choices.append(maze[current_position[0]][current_position[1] - 1])
        if current_position[1] < size - 1:
            choices.append(maze[current_position[0]][current_position[1] + 1])

        print("Choose your next move:")
        print(", ".join(str(choice) for choice in choices))

        user_choice = int(input("Enter your choice: "))

        if user_choice in choices:
            current_position[0] = maze[current_position[0]].index(user_choice)
            current_position[1] = maze[current_position[0]].index(user_choice)
        else:
            print("Invalid choice. Try again.")

        if current_position == [size - 1, size - 1]:
            print("Congratulations! You reached the end of the maze.")
            break

if __name__ == "__main__":
    maze_size = 4  # You can adjust the size of the maze
    play_number_maze(maze_size)
