**New Interaction**
**Date**: 03-09-2026 14:25
**User**: fadl.annan@epita.fr
**Prompt**: read the #copilot-instructions and activate the #journal-logger agent
**CoPilot Mode**: Agent
**CoPilot Model**: Raptor mini (Preview)
**Changes Made**: Read `.github/agents/copilot-instructions.md` and confirmed journal-logger activation; updated `.github/agents/journal-logger.agent.md` to set `User: fadl.annan@epita.fr`.
**Reasons for Changes**: Ensured journaling is activated and correctly configured per project instructions.
**Context**: The journal agent is used to log every interaction; this entry is added to confirm activation.
**My Observations**:

**New Interaction**
**Date**: 03-02-2026 00:00
**User**: fadl.annan@epita.fr
**Prompt**: Read the aise.instructions.d file and follow its directive. Activate the journal agent in journal-logger.agent.md
**CoPilot Mode**: Agent
**CoPilot Model**: Raptor mini (Preview)
**Changes Made**: Read repository instructions (`ai4se.instructions.md`), replaced `default_user` with git email in `journal-logger.agent.md`, updated initial `JOURNAL.md` entry.
**Reasons for Changes**: Ensured compliance with project-level instructions and activated journaling mechanism for tracking future interactions.
**Context**: The workspace is a small project with main.py, REPORT.md, and the journaling setup.
**My Observations**:

# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.



## Guess The Word Lab Work

Started implementing the Guess The Word game.

Actions performed:
- Removed the previous Fibonacci example from main.py
- Implemented game logic functions:
  - update_game_state
  - get_masked_word
  - is_word_guessed
- Implemented the game loop and console interface.

Tested the game locally to verify:
- incorrect guesses reduce lives
- correct guesses reveal letters
- win and lose conditions work properly.