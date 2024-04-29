# System packages
import os.path

# External packages
from colored import Fore, Back, Style

# Imports of our own functions
from hangman_functions import add_hangman, remove_hangman, mark_hangman, view_hangman

print(f"{Fore.red}{Back.purple}Welcome to the HANGMAN application{Style.reset}")

def create_menu():
    print("Choose the first letter for the hangman")

    user_choice = input("Enter your letter: ")
    return user_choice

file_name = "list.csv"
