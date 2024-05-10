# System packages
import random
import cowsay
# import os.path


# Imports of our own functions
from visual_elements import hang_start, hang_a, hang_b, hang_c, hang_d, hang_end, gameover_message, looser_message, winner_message, hang_pre
from colourfiles import welcome_message # Needed to sepreate this as it didnt work within the file. 

# External packages
from colored import Fore, Back, Style  # this will allow for colours to the background of the game header. 
# from colored import colored


#  list of words that the program will run through.
def choose_word():
    word_list = ["true", "happy" "hello" "yellow", "silly", "dog", "frog", "cat", "purple"]
    return random.choice(word_list).upper() #  this list will be organised randomly to ensure that the game is intresting.


#  setting hang_stages function connected to the visual elements. Should be shown in order that they have been displayed. 
hang_stages = [hang_pre, hang_start, hang_a, hang_b, hang_c, hang_d, hang_end, ]


#  Letter guessing 
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#  Menu for the game
def display_menu():
    print(welcome_message)
    print("1. Start Game")
    print("2. See List of Words")
    print("3. Exit")


def main():
    while True:
        word = choose_word()
        guessed_letters = set()
        tries = 9 #  trys corrispond to the hangman graphics 
        

        print(welcome_message) # this is an alternative to the above as i encurred some issues regarding the colour
       # cowsay. ('WELCOME') # this is to embed a style into the prgram 
        # print(f"{Fore.pink}{Back.pink} Welcome to the HANGMAN application {Style.reset}")
        # print(colored("Welcome to the HANGMAN application", fore="pink", back="pink"))

        #print(f"{Fore.PINK}{Back.PINK} Welcome to the HANGMAN application {Style.RESET}")
        print(display_word(word, guessed_letters))

        while not all(letter in guessed_letters for letter in word) and tries > 0:
            guess = input('Please guess a letter or word: ').upper()
            
            if not guess.isalpha() or len(guess) != 1:
                print("ERROR! Please enter a single letter.")  # this allows for error handeling when errors are incurred form a single number or multipule letters being entred. 
                continue
            
            if len(guess) == 1: 
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                elif guess in word:
                    print("Good guess!")
                    guessed_letters.add(guess)
                    print(hang_stages[min(tries, len(hang_stages) - 1)])
                else:
                    print("Wrong guess! Good try!")
                    tries -= 1
                    print(hang_stages[min(tries, len(hang_stages) - 1)])
            elif len(guess) == len(word):
                if guess == word:
                    print("Congratulations! You guessed the word!")
                    print(winner_message)
                else:
                    print("Wrong guess! Good try!")
                    tries -= 1
     #       else:
      #          print('Not a valid guess.') #this was removed as the error handeling was updated to be inlcuded above. this message was not working evertime within the code

            print(display_word(word, guessed_letters))
            print(f"Tries left: {tries}") 

        if all(letter in guessed_letters for letter in word):
            print("You guessed the word!")
            print(winner_message)
        else:
            print(f"Sorry, you lost! The word was: {word}")
            print(looser_message)         #this will be shown if the user did not guess correctly



        print(gameover_message)
        play_again = input("Do you want to play again? (yes/no): ")()
        if play_again != "yes":
            print("Thank you for using the Hangman application.")   #final message at the end of the above script.
            break   #to break the loop this text has been entred. 

if __name__ == "__main__":
    main()






