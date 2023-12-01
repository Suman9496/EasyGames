import random

def generate_mystery():
    suspects = ["Professor Plum", "Miss Scarlet", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock"]
    weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Library", "Billiard Room", "Lounge", "Hall", "Study"]

    mystery = {
        "suspect": random.choice(suspects),
        "weapon": random.choice(weapons),
        "room": random.choice(rooms)
    }

    return mystery

def play_mystery_detective():
    mystery = generate_mystery()

    print("Welcome to Mystery Detective!")
    print("You are a detective trying to solve a mysterious crime.")
    print("There are three aspects to uncover: the suspect, the weapon, and the room.")

    for _ in range(3):
        player_guess = input("Enter your guess (suspect/weapon/room): ").lower()
        if player_guess in mystery:
            if player_guess == "room":
                print("You enter the", mystery[player_guess])
            else:
                print("You suspect", mystery[player_guess])

            if input("Is this your final accusation? (yes/no): ").lower() == "yes":
                if player_guess == mystery["room"]:
                    print("Congratulations! You solved the mystery!")
                else:
                    print("Sorry, that's not correct. The mystery remains unsolved.")
                break
        else:
            print("Invalid guess. Please enter 'suspect', 'weapon', or 'room'.")

if __name__ == "__main__":
    play_mystery_detective()
