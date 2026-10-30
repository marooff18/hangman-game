
import random

# List of words
words = ["python", "computer", "program", "coding", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    # Take a guess
    guess = input("Guess a letter: ").lower()

    # Check the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts remaining:", attempts)

# Game over
else:
    print("\nGame over!")
    print("The correct word was:", secret_word)
