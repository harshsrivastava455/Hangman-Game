import random

# List of predefined words
words = ["python", "apple", "school", "computer", "garden"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=== Welcome to Hangman ===")

while incorrect_guesses < max_incorrect:

    # Display the current word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the word
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_incorrect - incorrect_guesses)

# Game over if attempts are finished
if incorrect_guesses == max_incorrect:
    print("\nGame Over!")
    print("The correct word was:", word)
