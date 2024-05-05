# System packages
import os.path

# External packages
from colored import Fore, Back, Style

# Imports of our own functions
from hangman_functions import add_hangman, remove_hangman, mark_hangman, view_hangman

print(f"{Fore.red}{Back.purple}Welcome to the HANGMAN application{Style.reset}")
#  alternative script- print(f"{Fore.black}{Back.white}Welcome to the HANGMAN application!\n\n")

#  Subheading:
    print("Choose the first letter for the hangman!")

def create_menu():
    user_choice = input       ("Enter your letter: ")
    return user_choice

file_name = "list.csv"
