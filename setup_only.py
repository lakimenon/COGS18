import classes_only
import pygame

display_width = 800
display_height = 600
high_score = 0

black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bg_color = (53, 115, 255)

play_button = classes_only.Button(150, 450, 50, 100, bright_green, green, "Play Again", game_loop)
quit_button = classes_only.Button(550, 450, 50, 100, bright_red, red, "Quit", quitgame)
go_button = classes_only.Button(150, 450, 50, 100, bright_green, green, "Go!", game_loop)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's Play!")
clock = pygame.time.Clock()
gameIcon = pygame.image.load('present.png')
pygame.display.set_icon(gameIcon)