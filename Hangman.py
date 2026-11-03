import random

WORDS = ["python", "banana", "guitar", "planet", "window"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong_guesses = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG:
        print(display_word(word, guessed))
        print(f"Guessed letters: {' '.join(sorted(guessed)) or 'none'}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print("Wrong!\n")

        # Win check
        if all(letter in guessed for letter in word):
            print(display_word(word, guessed))
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()