# System packages
import os.path


# Imports of our own functions
from visual_elements import hang_a, hang_b, hang_c, hang_d, hang_end, hang_start, gameover_message, looser_message, winner_message

# External packages
from colored import Fore, Back, Style

# Imports of our own functions
from hangman_functions import add_hangman, remove_hangman, mark_hangman, view_hangman






def choose_word():
    word_list = ["plant", "happy", "hello", "whale", "silly"]
    return random.choice(word_list).upper()
#  list of words that the program will run through


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word = choose_word()
    guessed_letters = set()
    tries = 6
    
    
    print(f"{Fore.red}{Back.purple} Welcome to the HANGMAN application {Style.reset}")
    #  alternative script- print(f"{Fore.black}{Back.white}Welcome to the HANGMAN application!\n\n")
    print(display_word(word, guessed_letters))

    while not all(letter in guessed_letters for letter in word) and tries > 0:
        guess = input('Please guess a letter or word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.add(guess)
            else:
                print("Wrong guess!")
                tries -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("Congratulations! You guessed the word!")
                break
            else:
                print("Wrong guess!")
                tries -= 1
        else:
            print('Not a valid guess.')

        print(display_word(word, guessed_letters))
        print(f"Tries left: {tries}")

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you lost! The word was: {word}")

if __name__ == "__main__":
    main()




















#  Subheading:
print("Choose the first letter for the hangman!")

def create_menu():
    user_choice = input       ("Enter your letter: ")
    return user_choice




while not gessed and tried > 0:
    guess = input('please guess a letter or wrd: ').upper()
   
    if len (guess) == 1 and guess.isalpha():
    
    elif len (guess) == len(word) and guess.isalpha()
   
    else: 
        print('Not a valid guess.')


#  Letter guessing 

print('WRONG! Try again!')

print('Correct! Excellet!').upper()

print('WINNER!') 

print('YOU LOOSE! Better luck next time!')






file_name = "list.csv"


print("Thank you for using the hangman application")




