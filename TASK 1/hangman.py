import random

def choose_word():
    words = ["python", "programming", "hangman", "gaming", "challenge", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(incorrect_attempts):
    hangman_parts = [
        "  -----  \n |     | \n |       \n |       \n |       \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |       \n |       \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |     | \n |       \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |    /| \n |       \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |    /|\\ \n |       \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |    /|\\ \n |    /  \n |       \n-+-      \n",
        "  -----  \n |     | \n |     O \n |    /|\\ \n |    / \\ \n |       \n-+-      \n"
    ]

    return hangman_parts[incorrect_attempts]

def hangman_game():
    print("Welcome to Hangman!")
    
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = len(draw_hangman(0)) - 1

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent Word:", current_display)
        print(draw_hangman(incorrect_attempts))
        print("Guessed Letters:", guessed_letters)

        if "_" not in current_display:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
            else:
                print("Incorrect guess. Try again.")
                incorrect_attempts += 1
            guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        if incorrect_attempts == max_attempts:
            print("\nGame over! You ran out of attempts. The correct word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman_game()
