""" Module containing calls to the functions required to run the game. """

import pygame
import functions_only

pygame.init()
functions_only.game_intro()

#game_loop contains all the function calls necessary to run the game
#game_loop continues to loop until the player decides to quit the game
functions_only.game_loop()	

pygame.quit()
quit() 