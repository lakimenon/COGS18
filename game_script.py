""" Module containing calls to the functions required to run the game. """

import pygame
import functions_only

pygame.init()	#initializing pygame

functions_only.game_intro()	#displays the intro screen
functions_only.game_loop()	#game_loop continues to loop until the player quits

pygame.quit()
quit()
