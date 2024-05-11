# System packages
import random
import os.path



# Imports of our own functions
from visual_elements import hang_start, hang_a, hang_b, hang_c, hang_d, hang_f, hang_end, gameover_message, looser_message, winner_message, hang_pre
from into import  welcome_message  # Needed to separate this as it didn't work within the file.

from Wordlist import word_list  # Secret word list

# External packages
from colored import Fore, Back, Style  # this will allow for colors to the background of the game header.


#  List of words that the program will run through.
def choose_word():
    return random.choice(word_list).upper()  #  this list will be organized randomly to ensure that the game is interesting.


#  setting hang_stages function connected to the visual elements.
#  Should be shown in order that they have been displayed.
hang_stages = [hang_pre, hang_start, hang_a, hang_b, hang_c, hang_d, hang_f, hang_end]


#  Letter guessing
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter  #  setting parameters if the letter guessed is correct using the plus equals operator
        else:
            display += "_"  #  setting parameters if the letter guessed is incorrect
    return display

#  Menu for the game - will be great to add in the future iterations for further deail
#  def display_menu():
   #   print(welcome_message)
   #   print("1. Start Game")
   #   print("2. See List of Words")
   #   print("3. Exit")


def main_app():
    while True:
        word = choose_word()
        guessed_letters = set()
        tries = 7

        print(welcome_message)
        print(f"{Fore.white}{Back.yellow}              \033[1mType 'EXIT' to EXIT game.           \033[0m {Style.reset}")
        print(hang_pre)

        print(display_word(word, guessed_letters))

        while not all(letter in guessed_letters for letter in word) and tries > 0:
            guess = input('\033[1mPlease guess a LETTER: \033[0m').upper()


            if guess in guessed_letters:
                print(f"{Fore.white}{Back.blue}     You've already guessed that letter.     {Style.reset}")
                print(f"{Fore.white}{Back.yellow}               \033[1mType 'EXIT' to EXIT game.              \033[0m {Style.reset}")
            elif guess in word:
                print(f"{Fore.white}{Back.green}                  Good guess!                  {Style.reset}")
                guessed_letters.add(guess)
            else:
                print(f"{Fore.white}{Back.blue}          Wrong guess! Good try!             {Style.reset}")
                tries -= 1
                print(hang_stages[7 - tries])  # Display current hang_stage

            
            if not guess.isalpha() or len(guess) != 1:
                if guess == "EXIT":
                    print("Exiting game.")
                    print(f"{Fore.white}{Back.red}    Thank you for using the Hangman application.    {Style.reset}")
                    return
                print(f"{Fore.white}{Back.blue}    ERROR! Please enter a single letter.  {Style.reset}")
                print(f"{Fore.white}{Back.yellow}               \033[1mType 'EXIT' to EXIT game.              \033[0m {Style.reset}")

                

            print(display_word(word, guessed_letters))
            print(f"Tries left: {tries}")

        if all(letter in guessed_letters for letter in word):
            print(f"{Fore.white}{Back.green}             You guessed the word!             {Style.reset}")
            print(winner_message)
        else:
            print(looser_message)
            print(f"{Fore.white}{Back.red}YOU LOST! The word was:{Style.reset} {word}")


        print(f"{Fore.white}{Back.yellow}        \033[1mType ANYTHING OTHER THAN YES to EXIT game.      \033[0m {Style.reset}")
        print(f"{Fore.white}{Back.green}        \033[1mType 'YES' or 'Y' to keep playing game.         \033[0m {Style.reset}")
        play_again = input("DO YOU WANT TO PLAY AGAIN?: ").lower()
        if play_again != "yes" and play_again != "y":
            print(gameover_message)
            print(f"{Fore.white}{Back.red}    Thank you for using the Hangman application.    {Style.reset}") #final message at the end of the above script.
            break

main_app()
