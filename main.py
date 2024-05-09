import random
import os.path

from visual_elements import hang_a, hang_b, hang_c, hang_d, hang_end, hang_start, gameover_message, looser_message, winner_message
from colored import Fore, Back, Style

def choose_word():
    word_list = ["plant", "happy", "hello", "yellow", "silly", "dog", "frog", "cat", "purple"]
    return random.choice(word_list).upper()

hang_stages = [hang_start, hang_a, hang_b, hang_c, hang_d, hang_end]

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    while True:
        word = choose_word()
        guessed_letters = set()
        tries = 8

        print("Welcome to the HANGMAN application")

        print(display_word(word, guessed_letters))

        while not all(letter in guessed_letters for letter in word) and tries > 0:
            guess = input('Please guess a letter or word: ').upper()

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                elif guess in word:
                    print("Good guess!")
                    guessed_letters.add(guess)
                    print(hang_stages[6 - tries])
                else:
                    print("Wrong guess! Good try!")
                    tries -= 1
                    print(hang_stages[6 - tries])
            elif len(guess) == len(word):
                if guess == word:
                    print("Congratulations! You guessed the word!")
                    print(winner_message)
                else:
                    print("Wrong guess! Good try!")
                    tries -= 1
            else:
                print('Not a valid guess.')

            print(display_word(word, guessed_letters))
            print(f"Tries left: {tries}")

        if all(letter in guessed_letters for letter in word):
            print("You guessed the word!")
            print(winner_message)
        else:
            print(f"Sorry, you lost! The word was: {word}")
            print(looser_message)

        print(gameover_message)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for using the Hangman application.")
            break

if __name__ == "__main__":
    main()
    
    





