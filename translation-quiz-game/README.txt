# TranslationGame

## Description
`TranslationGame` is a simple console-based game that tests your knowledge of English translations for Indonesian words. It generates random translation questions and evaluates if your answers are correct. The game keeps track of your score and provides feedback after each guess.

## Features
- Randomly selects Indonesian words and asks for their English translations.
- Provides one correct answer and one incorrect answer for each question.
- Allows players to guess if the provided translation is correct or not.
- Keeps track of the player's score.
- Offers an option to play again or exit the game.

## Requirements
- Python 3.x
- pandas library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/username/repo-name.git
    ```
2. Navigate to the project directory:
    ```bash
    cd repo-name
    ```
3. Install the required Python library:
    ```bash
    pip install pandas
    ```

## Usage
1. Prepare a CSV file named `300wordlist.csv` with two columns: `INDONESIA` and `ENGLISH`, containing Indonesian words and their English translations, respectively.
2. Run the game script:
    ```bash
    python translation_game.py
    ```

## How It Works
1. The game loads a CSV file containing a list of Indonesian words and their English translations.
2. It randomly selects an Indonesian word and presents a question with one correct and one incorrect translation.
3. The player guesses whether the provided translation is correct or not.
4. The game updates the score based on the player's answers and provides feedback.
5. The player can choose to play again or exit the game.

## Example
```plaintext
Translate 'kucing' in English is 'cat'
Is the translation correct? (yes/no): yes
Your answer is correct
Your Score : 1
Do you want to play the game again? Click ENTER for next and Type 'no' for break: 