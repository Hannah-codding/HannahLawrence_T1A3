# System packages
import os.path
import random


# Imports of our own functions
from visual_elements import hang_a, hang_b, hang_c, hang_d, hang_end, hang_start, gameover_message, looser_message, winner_message
#from hangman_functions import add_hangman, remove_hangman, mark_hangman, view_hangman 


# External packages
# from colored import Fore, Back, Style





def choose_word():
    word_list = ["plant", "happy", "hello", "whale", "silly"]
    return random.choice(word_list).upper()
#  list of words that the program will run. the user will hopefully not see this so that they can guess the answers. 



#  Stages of hangman visual, this should be run in order by the script
hang_stages = [hang_start, hang_a, hang_b, hang_c, hang_d, hang_end]



#  Letter guessing 
def display_word(word, guessed_letters): # setting peramitors for the letter guessing 
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_" 
    return display


def main():
    word = choose_word() # this will be sourced from the word list on line 20. Set to be random to make the game more difficult
    guessed_letters = set()
    tries = 6    # amount of tries the player gets before the correct word. this aligns to the hangma graphic.  


    # print(f"{Fore.pink}{Back.pink} Welcome to the HANGMAN application {Style.reset}")
    print("Welcome to the HANGMAN application") # styling applied to the first line
 #####  alternative script---= print(f"{Fore.black}{Back.white}Welcome to the HANGMAN application!\n\n")
    print(display_word(word, guessed_letters))

    while not all(letter in guessed_letters for letter in word) and tries > 0:
        guess = input('Please guess a letter or word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.") # shown when the user has already guessed a letter
            elif guess in word:
                print("Good guess!") 
                guessed_letters.add(guess)
                print(hang_stages[6 - tries])
            else:
                print("Wrong guess! Good try!")
                tries -= 1
                print(hang_stages[6 - tries])
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("Congratulations! You guessed the word!")
                print (winner_message)
                  #break
            else:
                print("Wrong guess! Good try!")
                tries -= 1
                print(gameover_message)
        else:
            print('Not a valid guess.')

        print(display_word(word, guessed_letters))
        print(f"Tries left: {tries}")

    if all(letter in guessed_letters for letter in word):
        print("You guessed the word!")
        print(winner_message)

    else:
        print(f"Sorry, you lost! The word was: {word}")
        print (looser_message)
        
    print(gameover_message)   #final message at the end of the above script.












