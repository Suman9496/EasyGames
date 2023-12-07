import random

def generate_maze(size):
    maze = [[' ' for _ in range(size)] for _ in range(size)]

    # Place obstacles randomly
    for _ in range(size):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        maze[row][col] = 'X'

    # Place exit at a random position
    exit_row = random.randint(0, size - 1)
    exit_col = random.randint(0, size - 1)
    maze[exit_row][exit_col] = 'E'

    # Place player at the starting position
    player_row = random.randint(0, size - 1)
    player_col = random.randint(0, size - 1)
    maze[player_row][player_col] = 'P'

    return maze, (player_row, player_col), (exit_row, exit_col)

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
        print("-" * (2 * len(row) - 1))

def play_maze_runner(size):
    maze, player_position, exit_position = generate_maze(size)

    print("Welcome to Maze Runner!")
    print("Navigate through the maze to reach the exit (E). Avoid obstacles (X).")

    while True:
        print_maze(maze)
        direction = input("Enter direction (W/A/S/D): ").upper()

        new_position = player_position

        if direction == 'W' and player_position[0] > 0:
            new_position = (player_position[0] - 1, player_position[1])
        elif direction == 'A' and player_position[1] > 0:
            new_position = (player_position[0], player_position[1] - 1)
        elif direction == 'S' and player_position[0] < size - 1:
            new_position = (player_position[0] + 1, player_position[1])
        elif direction == 'D' and player_position[1] < size - 1:
            new_position = (player_position[0], player_position[1] + 1)
        else:
            print("Invalid move. Try again.")

        if maze[new_position[0]][new_position[1]] == 'X':
            print("Oops! You hit an obstacle. Game over.")
            break
        elif new_position == exit_position:
            print_maze(maze)
            print("Congratulations! You reached the exit. You win!")
            break
        else:
            maze[player_position[0]][player_position[1]] = ' '
            maze[new_position[0]][new_position[1]] = 'P'
            player_position = new_position

if __name__ == "__main__":
    maze_size = 5  # You can adjust the size of the maze
    play_maze_runner(maze_size)
