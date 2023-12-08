import random

def print_intro():
    print("Welcome to RPG Adventure!")
    print("You find yourself in a magical land with many challenges and choices.")
    print("Make decisions wisely and see where the adventure takes you!")

def make_choice(options):
    print("\nChoose an option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("Enter the number of your choice: ")

    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(options):
            return options[choice_index]
        else:
            print("Invalid choice. Try again.")
            return make_choice(options)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return make_choice(options)

def play_rpg_adventure():
    print_intro()

    player_health = 100
    player_gold = 0

    while player_health > 0:
        print(f"\nYour stats: Health - {player_health}, Gold - {player_gold}")

        encounter_options = [
            "Explore the forest",
            "Visit the town",
            "Enter the dark cave",
            "Quit the adventure"
        ]

        encounter_choice = make_choice(encounter_options)

        if encounter_choice == "Explore the forest":
            print("You find a mysterious potion. Do you want to drink it?")
            potion_options = ["Yes", "No"]
            potion_choice = make_choice(potion_options)

            if potion_choice == "Yes":
                print("The potion restores your health!")
                player_health += random.randint(20, 40)
            else:
                print("You decide not to drink the potion.")

        elif encounter_choice == "Visit the town":
            print("In the town, you find a merchant selling magical items.")
            buy_options = ["Buy a health potion (10 gold)", "Leave the shop"]
            buy_choice = make_choice(buy_options)

            if buy_choice == "Buy a health potion (10 gold)":
                if player_gold >= 10:
                    print("You buy a health potion and feel stronger!")
                    player_health += random.randint(10, 20)
                    player_gold -= 10
                else:
                    print("You don't have enough gold to buy the potion.")

            else:
                print("You decide to leave the shop.")

        elif encounter_choice == "Enter the dark cave":
            print("You enter the dark cave and encounter a fierce dragon!")
            fight_options = ["Fight the dragon", "Run away"]
            fight_choice = make_choice(fight_options)

            if fight_choice == "Fight the dragon":
                dragon_health = random.randint(50, 100)
                while dragon_health > 0 and player_health > 0:
                    player_attack = random.randint(10, 20)
                    dragon_health -= player_attack
                    print(f"You attack the dragon and deal {player_attack} damage. Dragon's health: {dragon_health}")

                    if dragon_health > 0:
                        dragon_attack = random.randint(5, 15)
                        player_health -= dragon_attack
                        print(f"The dragon counterattacks and deals {dragon_attack} damage. Your health: {player_health}")

                if player_health > 0:
                    print("You defeated the dragon and find a treasure chest!")
                    player_gold += random.randint(20, 50)
                else:
                    print("Unfortunately, the dragon was too strong. Game over.")

            else:
                print("You run away from the dragon. A wise decision.")

        elif encounter_choice == "Quit the adventure":
            print("Thanks for playing RPG Adventure. Goodbye!")
            break

    if player_health <= 0:
        print("Your adventure has come to an end. Better luck next time!")

if __name__ == "__main__":
    play_rpg_adventure()
