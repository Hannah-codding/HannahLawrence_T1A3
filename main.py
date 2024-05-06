# System packages
import os.path

# External packages
from colored import Fore, Back, Style

# Imports of our own functions
from hangman_functions import add_hangman, remove_hangman, mark_hangman, view_hangman

print(f"{Fore.red}{Back.purple} Welcome to the HANGMAN application {Style.reset}")
#  alternative script- print(f"{Fore.black}{Back.white}Welcome to the HANGMAN application!\n\n")

#  Subheading:
print("Choose the first letter for the hangman!")

def create_menu():
    user_choice = input       ("Enter your letter: ")
    return user_choice


>>> alien.start = r'''
   _________________________________________________
 /                                                  \
| WELCOME TO MY TERMINAL GAME!                       |
| THIS HAS BEEN CREATED USING PYTHON! HOPE YOU CAN   |
| GUESS THE WORD INTIME. USE THE CLUES FOR HELP!     | 
 \                                                  /
  =================================================
                                                 \
                                                  \
                                                    ^__^
                                                    (oo)
                                                   <(__)>
                                                    |  |
'''


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



#  The below is the hangman visual 

void printHangman

hang_start = r'''
		  ____   
		 I    I  
		 I       
		 I       
		 I       
		_I_________    
		
'''


hang_one = r'''
		  ____   
		 I    I  
		 I    O   
		 I       
		 I       
		_I_________    
		
'''
hang_two = r'''
		  ____   
		 I    I  
		 I   _O_  
		 I       
		 I       
		_I_________    
		
'''

hang_three = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0 
		 I       
		_I_________   
		
'''

hang_four = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0 
		 I   /    
		_I_________    
		
'''

hang_five = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0
		 I   ⅃ L   
		_I_________    

'''

gameover_message = r'''


██████████      ████████     ████        ████   █████████⣿
██             ██      ██    ██ ██      ██ ██   ██
██            ██        ██   ██  ██    ██  ██   ██
██            ██        ██   ██   ██  ██   ██   ██
██    ████    ████████████   ██     ██     ██   ████████
██      ██    ██        ██   ██            ██   ██
██████████    ██        ██   ██            ██   █████████⣿

 ⠀              ⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀       ⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀       ⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀       ⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀       ⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀       ⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀       ⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀       ⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''
looser_message = r'''

               ██               ██
             ████▄  ▄▄▄▄▄▄▄  ▄████
               ▀▀█▄█████████▄█▀▀
                 █████████████
                 ██▀▀▀███▀▀▀██
                 ██⣿⣿███⣿⣿██
                 █████▀▄▀█████
                  ███████████
              ▄▄▄██  █▀█▀█  ██▄▄▄
              ▀▀██           ██▀▀
                ▀▀           ▀▀

'''
winner_message = = r'''

             ___________
             ███████████
             ██WINNER!██
             ███████████ 
              █████████
              █████████
                 ) (
                 ███ 
               ███████
              `"""""""`
            
'''


error_message = r'''

ERROR!PLEASE TYPE A VALID LETTER

'''


file_name = "list.csv"


