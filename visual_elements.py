#  The below is the hangman visual 

hang_start = r'''
		  ____   
		 I    I  
		 I       
		 I       
		 I       
		_I_________    
		
'''


hang_a = r'''
		  ____   
		 I    I  
		 I    O   
		 I       
		 I       
		_I_________    
		
'''
hang_b = r'''
		  ____   
		 I    I  
		 I   _O_  
		 I       
		 I       
		_I_________    
		
'''

hang_c = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0 
		 I       
		_I_________   
		
'''

hang_d = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0 
		 I   /    
		_I_________    
		
'''

hang_end = r'''
		  ____   
		 I    I  
		 I   _O_ 
		 I    0
		 I   ⅃ L   
		_I_________    

'''

gameover_message = r'''

                                       ⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀ ⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 
'''
looser_message = r'''

            ⣿⣿                 ⣿⣿
             ⣿⣿⣿⣶  ▄▄▄▄▄▄▄  ⣶⣿⣿⣿
               ⠛⠛⣿▄█████████▄⣿⠛⠛
                 █████████████
                 ██▀▀▀███▀▀▀██
                 ██   ███   ██
                 █████▀▄▀█████
                  ███████████
              ⣶⣶⣿⣿  █▀█▀█  ⣿⣿⣶⣶
              ▀▀█⣿           ⣿█▀▀
                ▀▀           ▀▀

'''
winner_message = r'''

             ___________
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⠹⣿⣿WINNER!⣿⡟
             ⣿⣿⣿⣿⣿⣿⣿⣿ 
              ⠹⣿⣿⣿⣿⣿⡟
               ⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿
                  ⣿
               ███████
              `"""""""`
            
'''


error_message = r'''

ERROR!PLEASE TYPE A VALID LETTER

'''


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