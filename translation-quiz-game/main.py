import pandas as pd
import random
import os

class TranslationGame:
    def __init__(self, csv_file):
        self.wordlist = pd.read_csv(csv_file)
        self.score = 0

    def generate_question(self):
        find_task = self.wordlist.sample(n=1).iloc[0]  # Sample one random row
        task1 = find_task['INDONESIA']
        correct_answer = find_task['ENGLISH']
        
        # Choose a wrong answer that is different from the correct answer
        wrong_answers = self.wordlist[self.wordlist['ENGLISH'] != correct_answer]['ENGLISH']
        wrong_answer = random.choice(wrong_answers)
        
        # Choose an answer to display
        answer = random.choice([correct_answer, wrong_answer])
        print(f"Translate '{task1}' in English is '{answer}'")

        correct_translation = (answer == correct_answer)
        return correct_translation

    def clear_screen(self):
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_game(self):
        while True:
            self.clear_screen()
            correct_answer = self.generate_question()
            guess = input("Is the translation correct? (yes/no): ").strip().lower()
            if guess == 'yes' and correct_answer:
                self.score += 1
                print('Your answer is correct')
            elif guess == 'no' and not correct_answer:
                self.score += 1
                print('Your answer is correct')
            else:
                print('Your answer is wrong')
            print(f'Your Score : {self.score}')

            continue_game = input("Do you want to play the game again? Click ENTER for next and Type 'no' for break: ").strip().lower()
            if continue_game == 'no':
                print(f'Your final Score is : {self.score}')
                break

# Create an instance of TranslationGame and start the game
game = TranslationGame("300wordlist.csv")
game.play_game()
