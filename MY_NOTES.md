# My Original Thinking

## App States

- Game start
- Waiting for player guess
- Correct guess
- Incorrect guess
- Win state
- Lose state
- Replay state

## App Variables

- secret_word
- guessed_letters
- guess
- lives
- incorrect_guesses
- masked_word

## App Rules and Invariants

- The secret word does not change during the game.
- A letter cannot reduce lives twice.
- Lives start at 6.
- The player wins when all letters are guessed.
- The player loses when lives reach 0.

## App Bugs

Possible bugs:

- Repeated guesses
- Non-letter input
- Upper/lowercase issues
- Empty input
- Game not stopping when word is completed

---

# CoPilot Suggestions

CoPilot suggested similar states and variables but sometimes over-complicated the solution with extra structures.

Useful suggestions included:

- separating logic from UI
- keeping guessed letters in a list
- tracking incorrect guesses separately