import random

# List of predefined words
words = ["python", "apple", "hangman", "program", "code"]

# Choose a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("You have 6 chances to guess the word.")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single valid letter.")
        continue

    if guess in used_letters:
        print("You already used that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n❌ You ran out of attempts. The word was:", word)


