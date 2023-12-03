import random

def generate_numbers(size):
    return [random.randint(1, 9) for _ in range(size)]

def print_numbers(numbers, current_position):
    for i, num in enumerate(numbers):
        if i == current_position:
            print(f"[{num}]", end=" ")
        else:
            print(num, end=" ")
    print()

def play_number_jumper():
    numbers = generate_numbers(10)
    current_position = 0

    print("Welcome to Number Jumper!")
    print("Jump between numbers to reach the target number.")

    target_number = random.choice(numbers)
    print(f"The target number is: {target_number}")

    while True:
        print_numbers(numbers, current_position)

        if numbers[current_position] == target_number:
            print("Congratulations! You reached the target number.")
            break

        jump_size = int(input("Enter the number of positions to jump: "))

        if 0 <= current_position + jump_size < len(numbers):
            current_position += jump_size
        else:
            print("Invalid jump. Try again.")

if __name__ == "__main__":
    play_number_jumper()
