# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment

## Initial Thoughts
The assignment required implementing a simple "Guess the Word" (Hangman-style) game as a Python console application. The core idea is that the computer selects a random word and the player guesses letters within a limited number of turns. The program must keep track of guessed letters, remaining lives, and display the partially revealed word.

## Assumptions Made
I assumed that the game should:
- Use a predefined list of possible words.
- Start with a default number of lives (6).
- Accept one letter at a time from the user.
- End when the word is guessed or the player runs out of lives.

## Points Needing Clarification
Some points that required attention while reading the instructions:
- The function `update_game_state` must be pure and not use global variables.
- The program should separate the game logic from the user interface.
- Certain shortcuts like `while True` loops and string replacement functions should not be used.

# Key Learnings

## Computer Science Concepts and Technical Skills
Working on this project reinforced several programming concepts:
- Managing application state using variables and function parameters.
- Designing pure functions that do not modify global state.
- Separating logic from the user interface to keep the code organized.
- Working with lists and strings to track guessed letters and display the masked word.

## Insights about Using CoPilot Effectively
CoPilot was useful for:
- Suggesting possible function implementations.
- Generating documentation comments.
- Helping think about edge cases and potential bugs.

However, it sometimes suggested solutions that did not follow the project constraints, so reviewing its output carefully was important.

## New Concepts or Tools Encountered
This project emphasized the importance of documenting development through files such as:
- `README.md`
- `JOURNAL.md`
- `REPORT.md`

It also reinforced using Git and GitHub to manage and submit projects.

# Report on CoPilot Prompting Experience

### Types of prompts that worked well
Prompts that clearly described the task worked best. For example:
- Asking CoPilot to review a specific function.
- Asking for suggestions for tests for a given function.
- Requesting documentation for existing code.

### Types of prompts that did not work well or failed
Prompts that were too vague sometimes produced overly complex or irrelevant answers. In some cases, CoPilot suggested solutions that used features not allowed by the assignment instructions.

# Limitations, Hallucinations and Failures

## Examples of Hallucinations or Failures or Misleading Information
Examples included:
- Suggesting the use of string replacement functions even though they were not allowed.
- Proposing unnecessary abstractions or complex data structures for a simple problem.
- Generating code that used loops or patterns that did not follow the assignment constraints.

## Analysis of Why These Issues Occurred
These issues likely occurred because CoPilot tries to generate generally correct programming solutions without always considering the specific rules of the assignment.

## Impact on the Project
This meant that all AI-generated suggestions had to be reviewed carefully before being used. It required understanding the code rather than blindly accepting suggestions.

# AI Trust

## When did I trust the AI?
I trusted the AI when it helped with explanations, documentation, or simple structural suggestions.

## When did I stop trusting it?
I was more cautious when it generated complex code or solutions that did not strictly follow the assignment instructions.

## What signals indicated low reliability?
Signs included:
- Code that did not follow the project constraints
- Overly complicated implementations
- Suggestions unrelated to the task

# What I Learned

## What did you learn about software development?
This project highlighted the importance of:
- designing clear program structure
- separating logic and UI
- thinking about edge cases and bugs before implementing features

## What did you learn about using AI tools?
AI can be very helpful for brainstorming ideas and generating drafts, but it should always be reviewed carefully.

## When should you trust AI? When should you double-check it?
AI suggestions are useful as a starting point, but they should always be verified, especially when specific constraints or correctness requirements exist.

# Reflection

## Did AI make you faster? Why or why not?
AI helped speed up some parts of development, such as generating documentation and suggesting possible implementations.

## Did you feel in control of the code?
Yes. The final decisions about the structure and implementation were made manually after reviewing suggestions.

## Would you use AI the same way next time? What would you change?
Yes, but I would focus on using AI more for explanations and brainstorming rather than directly copying generated code.