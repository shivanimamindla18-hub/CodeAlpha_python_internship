# CodeAlpha Python Programming Internship Projects

A collection of beginner-friendly Python console projects completed as part of the **CodeAlpha Python Programming Internship**: a Hangman game, a Stock Portfolio Tracker, and a Rule-Based Chatbot.

## Project Description

This repository contains three small Python programs that run entirely in the terminal and use only Python's standard library. Each program focuses on core Python concepts such as loops, conditionals, functions, dictionaries, lists and file handling.

## Objectives

- Practice core Python concepts: variables, strings, lists, dictionaries, loops, conditionals and functions.
- Build simple console applications that take user input and produce clear output.
- Write clean, readable and well-commented code.
- Learn to organise a project and publish it on GitHub.

## Features

### Task 1: Hangman Game (`hangman.py`)
- Picks a random word from a list of 5 predefined words.
- Player guesses one letter at a time.
- Maximum of 6 incorrect guesses.
- Rejects invalid input and repeated guesses.
- Option to play again.

### Task 2: Stock Portfolio Tracker (`portfolio.py`)
- Uses a hardcoded dictionary of stock prices.
- User enters stock names and quantities.
- Displays a table of holdings and the total investment value.
- Optionally saves the result to `portfolio.txt`.

### Task 4: Basic Chatbot (`chatbot.py`)
- Predefined replies for greetings, asking its name, asking how it is, thanking, and goodbye.
- Handles unknown messages politely.
- Ignores letter case and trailing punctuation (`Hello`, `HELLO`, `what is your name?`).
- Exits with `bye`, `exit` or `quit`.

## Technologies Used

- Python 3 (standard library only)
- VS Code (code editor)
- Git and GitHub (version control)

## Installation Instructions

1. Install **Python 3.8 or higher** from [python.org](https://www.python.org/downloads/). During installation on Windows, tick **"Add Python to PATH"**.
2. Check that Python is installed:
   ```
   python --version
   ```
3. Download or clone this repository:
   ```
   git clone https://github.com/<your-username>/codealpha-python-internship.git
   cd codealpha-python-internship
   ```
4. No extra packages need to be installed (see `requirements.txt`).

## How to Run the Project in VS Code

1. Open VS Code and choose **File > Open Folder...**, then select the project folder.
2. Install the **Python** extension from the Extensions panel if you haven't already.
3. Open the file you want to run (`hangman.py`, `portfolio.py` or `chatbot.py`).
4. Click the **Run** button (▶) at the top right, or open the terminal (**Terminal > New Terminal**) and run:
   ```
   python chatbot.py
   ```
   Use `python hangman.py` or `python portfolio.py` for the other tasks. On macOS/Linux, use `python3` instead of `python` if needed.

## Sample Input and Output

Running `python chatbot.py`:

```
PyBot: Hello! I'm PyBot. Type 'bye', 'exit' or 'quit' to leave.
You: Hello
PyBot: Hi! Nice to meet you.
You: What is your name?
PyBot: I'm PyBot, a simple chatbot built with Python.
You: how are you
PyBot: I'm fine, thanks! How about you?
You: what is the weather
PyBot: Sorry, I don't understand that. Try saying hello or asking how I am.
You: thank you
PyBot: You're welcome!
You: Bye
PyBot: Goodbye! Have a great day!
```

The same output is saved in `sample_output.txt`.

## Project Structure

```
codealpha-python-internship/
├── chatbot.py          # Task 4: rule-based chatbot
├── hangman.py          # Task 1: Hangman game
├── portfolio.py        # Task 2: stock portfolio tracker
├── sample_output.txt   # Sample chatbot terminal output
├── requirements.txt    # Dependencies (none needed)
├── .gitignore          # Files Git should ignore
└── README.md           # Project documentation
```

## Author

**Mamindla Shivani**

## Internship

CodeAlpha Python Programming Internship
