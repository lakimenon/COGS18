""" Module containing calls to the functions required to run the game. """

import pygame
from game_module import functions

pygame.init()	#initializing pygame

functions.game_intro()	#displays the intro screen
functions.game_loop()	#game_loop continues to loop until the player quits

pygame.quit()
quit()
