import random

WORDS = ["python", "galaxy", "jungle", "bridge", "castle"]

HANGMAN_STAGES = [
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""
]

MAX_WRONG = 6


def display_state(word, guessed, wrong_count):
    print(HANGMAN_STAGES[wrong_count])
    print("\nWord: ", " ".join(ch if ch in guessed else "_" for ch in word))
    print(f"Wrong guesses ({wrong_count}/{MAX_WRONG}):", " ".join(sorted(guessed - set(word))) or "-")


remaining_words = []

def get_next_word():
    global remaining_words
    if not remaining_words:
        remaining_words = random.sample(WORDS, len(WORDS))
    return remaining_words.pop()

def play():
    word = get_next_word()
    guessed = set()
    wrong_count = 0

    print("\n=============================")
    print("       HANGMAN GAME")
    print("=============================")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG} incorrect guesses.\n")

    while wrong_count < MAX_WRONG:
        display_state(word, guessed, wrong_count)

        # Check win
        if all(ch in guessed for ch in word):
            print(f"\n🎉 You won! The word was: {word.upper()}")
            break

        # Get input
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single letter.")
            continue
        if guess in guessed:
            print("⚠  You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"✅  '{guess}' is in the word!")
        else:
            wrong_count += 1
            remaining = MAX_WRONG - wrong_count
            print(f"❌  '{guess}' is not in the word. {remaining} guess(es) left.")
    else:
        display_state(word, guessed, wrong_count)
        print(f"\n💀 Game over! The word was: {word.upper()}")

    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play()
    else:
        print("\nThanks for playing! Goodbye 👋")


if __name__ == "__main__":
    play()
