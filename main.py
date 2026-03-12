import random


WORDS = [
    "python",
    "computer",
    "science",
    "hangman",
    "programming",
    "variable",
    "function"
]

MAX_LIVES = 6


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """
    Update the game state after a guess.

    Returns updated guessed_letters and lives.
    """

    if guess in guessed_letters:
        return guessed_letters, lives

    new_guessed_letters = guessed_letters + [guess]

    if guess in secret_word:
        return new_guessed_letters, lives
    else:
        return new_guessed_letters, lives - 1


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    """Return masked word display."""

    result = []

    for letter in secret_word:
        if letter in guessed_letters:
            result.append(letter.upper())
        else:
            result.append("_")

    return " ".join(result)


def is_word_guessed(secret_word: str, guessed_letters: list[str]) -> bool:
    """Check if player has guessed the word."""

    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def get_incorrect_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """Return list of incorrect guesses."""

    wrong = []

    for letter in guessed_letters:
        if letter not in secret_word:
            wrong.append(letter)

    return wrong



def display_game(secret_word, guessed_letters, lives):

    print("\nWord:", get_masked_word(secret_word, guessed_letters))

    wrong = get_incorrect_guesses(secret_word, guessed_letters)

    print("Incorrect guesses:", " ".join(wrong))
    print("Lives remaining:", lives)


def play_turn(secret_word, guessed_letters, lives):

    display_game(secret_word, guessed_letters, lives)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1:
        print("Please enter a single letter.")
        return guessed_letters, lives

    return update_game_state(secret_word, guessed_letters, guess, lives)



def play_game():

    secret_word = random.choice(WORDS)
    guessed_letters = []
    lives = MAX_LIVES

    while lives > 0 and not is_word_guessed(secret_word, guessed_letters):

        guessed_letters, lives = play_turn(
            secret_word,
            guessed_letters,
            lives
        )

    if is_word_guessed(secret_word, guessed_letters):
        print("\nYou win! The word was:", secret_word)
    else:
        print("\nYou lose! The word was:", secret_word)


def main():

    play_again = "y"

    while play_again == "y":

        play_game()

        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()