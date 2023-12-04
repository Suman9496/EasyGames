import random


def generate_cryptogram():
    phrases = [
        "HELLO WORLD",
        "PYTHON IS FUN",
        "CODE BREAKER",
        "CRYPTOGRAM PUZZLE",
        "ENCRYPTED MESSAGE"
    ]

    phrase = random.choice(phrases).upper()
    cipher_mapping = {letter: random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for letter in set(phrase) if letter.isalpha()}

    encrypted_phrase = "".join(cipher_mapping.get(letter, letter) for letter in phrase)

    return encrypted_phrase, cipher_mapping


def play_cryptogram():
    encrypted_phrase, cipher_mapping = generate_cryptogram()

    print("Welcome to Cryptogram!")
    print("Decipher the encrypted phrase.")

    while True:
        print("Encrypted phrase:", encrypted_phrase)
        guess_mapping = {input("Enter a letter to replace: ").upper(): input("Enter the replacement letter: ").upper()}

        decrypted_phrase = "".join(guess_mapping.get(letter, letter) for letter in encrypted_phrase)

        print("Decrypted phrase:", decrypted_phrase)

        if decrypted_phrase.isalpha():
            if input("Is this your final guess? (yes/no): ").lower() == "yes":
                if decrypted_phrase == "".join(cipher_mapping.get(letter, letter) for letter in encrypted_phrase):
                    print("Congratulations! You deciphered the cryptogram.")
                else:
                    print("Sorry, that's not correct. Keep trying!")
                break
        else:
            print("Invalid input. Please enter letters only.")


if __name__ == "__main__":
    play_cryptogram()
