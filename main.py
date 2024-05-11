# System packages
import random
import cowsay
import os.path

# Imports of our own functions
from visual_elements import hang_start, hang_a, hang_b, hang_c, hang_d, hang_end, gameover_message, looser_message, winner_message, hang_pre
from into import  welcome_message  # Needed to separate this as it didn't work within the file.

from Wordlist import word_list  # Secret word list

# External packages
from colored import Fore, Back, Style  # this will allow for colors to the background of the game header.


#  List of words that the program will run through.
def choose_word():
    return random.choice(word_list).upper()  #  this list will be organized randomly to ensure that the game is interesting.


#  setting hang_stages function connected to the visual elements.
#  Should be shown in order that they have been displayed.
hang_stages = [hang_start, hang_a, hang_b, hang_c, hang_d, hang_end]


#  Letter guessing
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter  #  setting parameters if the letter guessed is correct using the plus equals operator
        else:
            display += "_"  #  setting parameters if the letter guessed is incorrect
    return display


def main():
    while True:

        word = choose_word()
        guessed_letters = set()
        tries = 9  #  tries correspond to the hangman graphics

        print(welcome_message)# this is an alternative to the above as I incurred some issues regarding the color
        print (f"{Fore.white}{Back.yellow}               \033[1mPress 1 to EXIT game.              \033[0m {Style.reset}")
        print (hang_pre)

        print(display_word(word, guessed_letters))

        while not all(letter in guessed_letters for letter in word) and tries > 0:
            guess = input('\033[1mPlease guess a LETTER: \033[0m').upper()

            if not guess.isalpha() or len(guess) != 1:
                if guess == "1":
                    print("Exiting game.")
                    print(f"{Fore.white}{Back.red}    Thank you for using the Hangman application.    {Style.reset}")
                    return
                print(f"{Fore.white}{Back.blue}    ERROR! Please enter a single letter.  {Style.reset}") # this allows for error handling when errors are incurred form numbers or multiple letters being entered.
                print(f"{Fore.white}{Back.yellow} Press 1 to EXIT game. {Style.reset}")

                continue
            if len(guess) == 1:
                if guess in guessed_letters:
                    print(f"{Fore.white}{Back.blue}     You've already guessed that letter.     {Style.reset}")
                    print(f"{Fore.white}{Back.yellow} Press 1 to EXIT game. {Style.reset}")
                elif guess in word:
                    print(f"{Fore.white}{Back.green}                  Good guess!                  {Style.reset}")
                    guessed_letters.add(guess)
                    for stage in hang_stages[9 - tries:]:  # Iterate through stages from current to end
                        print(stage)
                else:
                    print(f"{Fore.white}{Back.blue}          Wrong guess! Good try!             {Style.reset}")
                    tries -= 1
                    for stage in hang_stages[9 - tries:]:  # Iterate through stages from current to end
                        print(stage)
            print(display_word(word, guessed_letters))
            print(f"Tries left: {tries}")

        if all(letter in guessed_letters for letter in word):
            print(f"{Fore.white}{Back.green}             You guessed the word!             {Style.reset}") 
            print(winner_message)
        else:
            print(f"Sorry, you lost! The word was: {word}") 
            print(looser_message)  # this will be shown if the user did not guess correctly

        print(gameover_message)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"{Fore.white}{Back.red}    Thank you for using the Hangman application.    {Style.reset}") 
            break  # to break the loop this text has been entered.


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






