import random

# List of words
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard"
]

# Select a random word
word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Try to guess the hidden word!")
print("You have 6 incorrect guesses.")
print()

# Main game loop
while incorrect_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Check if player has won
    if all(letter in guessed_letters for letter in word):
        print()
        print("Congratulations! 🎉")
        print("You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower().strip()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        print()
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    # Save the guess
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct! ✅")
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")

    print()

# Player loses
if incorrect_guesses == max_guesses:
    print()
    print("Game Over! 💀")
    print("The correct word was:", word)

print()
print("Thanks for playing!")
