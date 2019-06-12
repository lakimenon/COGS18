""" Module containing all the functions and setup variables used for the game """

import random
import pygame
from game_module import classes

def display_scores(message, score, x_location, y_location):
    """ Function to display current and high scores at the top of the window

    Parameters:
    -----------
    message : str
        Label for the score (Eg: 'current score', 'high score', etc)

    score : int
        Value of the score

    x_location : int
        x-coordinate of the message on the screen

    y_location : int
        y-coordinate of the message on the screen
    """
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render(message + str(score), True, BLACK)
    GAME_DISPLAY.blit(text, (x_location, y_location))

def display_objects(item):
    """ Function to display an object on the screen

    Parameters:
    -----------
    item : ScreenObjects instance
        Object to be displayed
    """
    GAME_DISPLAY.blit(item.icon, (item.x, item.y))

def text_objects(text, font):
    """ Function to create a rectangle containing text 
        (This function was adapted from online resource, see notebook for link)

    Parameters:
    -----------
    text : str
        Text to be displayed

    font : str
        Font in which the text is to be displayed
    """
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()

def display_button(button):
    """ Function to display buttons on the screen
    (This function was adapted from online resource, see notebook for link)

    Parameters:
    -----------
    button : Button instance
        Button to be displayed
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_bound = button.x + button.width > mouse[0] > button.x
    y_bound = button.y + button.height > mouse[1] > button.y
    button_dimensions = (button.x, button.y, button.width, button.height)

    #Changing the color of the button if mouse hovers over it
    if x_bound and y_bound:
        pygame.draw.rect(GAME_DISPLAY, button.active_color, button_dimensions)
        if click[0] == 1 and button.action != None:
            button.action()
    else:
        pygame.draw.rect(GAME_DISPLAY, button.inactive_color, button_dimensions)

    #Displaying the message on the button
    small_text = pygame.font.SysFont("freesansbold.ttf", 25)
    text_surf, text_rect = text_objects(button.msg, small_text)
    text_rect.center = ((button.x + (button.width/2)), (button.y + (button.height/2)))
    GAME_DISPLAY.blit(text_surf, text_rect)

def reset_location(object_name):
    """ Function to make an object fall from the top of the screen

    Parameters:
    -----------
    object_name : ScreenObjects instance (Rock or Present)
        Object which is to fall
    """
    object_name.y = 0 - object_name.height
    object_name.x = random.randrange(0, int(DISPLAY_WIDTH-object_name.width))

def overlap(player, item):
    """ Function to check whether the player icon overlaps or touches another object

    Parameters:
    -----------
    player: Player object
        Represents the player's icon on the screen
    item : ScreenObjects instance (Rock or Present)
        Item with which overlap is being checked

    Returns:
    --------
    overlapped : boolean
        True if there is an overlap between player and item, else False
    """
    overlapped = False
    if player.y <= item.y + item.height:
        left_overlap = item.x <= player.x <= item.x + item.width
        right_overlap = item.x <= player.x + player.width <= item.x + item.width
        middle_overlap = player.x < item.x and player. x + player.width > item.x + item.width
        overlapped = left_overlap or right_overlap or middle_overlap
    return overlapped

def rock_collected():
    """ Function to display game over screen when player loses
    (This function was adapted from online resource, see notebook for link)
    """
    #Display message indicating that player has lost
    med_text2 = pygame.font.SysFont("freesansbold.ttf", 80)
    text_surf, text_rect = text_objects("You Collected A Rock :(", med_text2)
    text_rect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3))
    GAME_DISPLAY.blit(text_surf, text_rect)

    #Display options to play again or quit the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_button(PLAY_BUTTON)
        display_button(QUIT_BUTTON)

        pygame.display.update()
        CLOCK.tick(15)

def quitgame():
    """ Function to end the game and close the window
    (This function was adapted from online resource, see notebook for link)
    """
    pygame.quit()
    quit()

def game_intro():
    """ Function to display the intro screen
    (This function was adapted from online resource, see notebook for link)
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        GAME_DISPLAY.fill(WHITE)

        #Displaying game instructions- each line requires its own text surface and location
        large_text = pygame.font.SysFont("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("Let's Play!", large_text)
        text_rect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3))

        word_height1 = text_surf.get_size()[1]

        med_text = pygame.font.SysFont("freesansbold.ttf", 40)
        description_line1 = "Collect presents and avoid rocks."
        text_surf2, text_rect2 = text_objects(description_line1, med_text)
        text_rect2.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3 + word_height1))

        word_height2 = text_surf2.get_size()[1]

        description_line2 = "Use the left and right arrow keys to move. Good luck!"
        text_surf3, text_rect3 = text_objects(description_line2, med_text)
        text_rect3.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3 + word_height1 + word_height2))

        GAME_DISPLAY.blit(text_surf, text_rect)
        GAME_DISPLAY.blit(text_surf2, text_rect2)
        GAME_DISPLAY.blit(text_surf3, text_rect3)

        #Display buttons to play or quit the game
        display_button(GO_BUTTON)
        display_button(QUIT_BUTTON)

        pygame.display.update()
        CLOCK.tick(15)

def game_loop():
    """ Main function to play the game, which continues to loop until the game is ended.
        This function contains calls to other functions as needed.
        (This function was adapted from online resource, see notebook for link)
     """

    #High score is made global to ensure that it does not reset to 0 when a new game is started
    global HIGH_SCORE

    #Placing player icon at the center bottom part of the screen
    x_coordinate = (DISPLAY_WIDTH * 0.45)
    y_coordinate = (DISPLAY_HEIGHT - 94)   #94 pixels is the height of the icon
    startx = random.randrange(0, DISPLAY_WIDTH)

    #Defining screen objects- numbers represent the dimensions (in px) of the respective icons
    player = classes.Player('./icons/basket.png', x_coordinate, y_coordinate, 94, 139, 0)
    rock = classes.Rock('./icons/rock.png', startx, -600, 48, 69, 4)
    present = classes.Present('./icons/present.png', startx, -100, 98, 82, 10)

    present_count = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -10
                if event.key == pygame.K_RIGHT:
                    player.x_change = 10

            if event.type == pygame.KEYUP:
                player.x_change = 0 #to make the basket stop moving once key is released

        player.x += player.x_change
        GAME_DISPLAY.fill(BG_COLOR)

        #Displaying all screen objects and scores
        display_objects(rock)
        display_objects(present)
        display_objects(player)

        display_scores("Presents Collected: ", present_count, 0, 0)
        display_scores("High Score: ", HIGH_SCORE, 0, 25)

        #Ensuring that the basket is within screen bounds
        if player.x > DISPLAY_WIDTH - player.width:
            player.x = DISPLAY_WIDTH - player.width

        if player.x < 0:
            player.x = 0

        #Making the rock drop again once it moves past the bottom of the screen
        if rock.y > DISPLAY_HEIGHT:
            reset_location(rock)
            rock.speed += 1 #Speed of the rock is increased each time it falls

        if present.y > DISPLAY_HEIGHT:
            reset_location(present)

        #When present is collected
        if overlap(player, present):
            reset_location(present)
            present_count += 1

        #When rock is collected
        if overlap(player, rock):
            if present_count > HIGH_SCORE:
                HIGH_SCORE = present_count
            rock_collected()

        #Making the rock and present move down the screen
        rock.y += rock.speed
        present.y += present.speed

        pygame.display.update()
        CLOCK.tick(60)

#SETUP: The following blocks of code define variables and objects used throughout the functions

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
HIGH_SCORE = 0

#Assigning RGB value of each color to a variable having that color name
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BG_COLOR = (53, 115, 255)

#Defining different buttons to be displayed
PLAY_BUTTON = classes.Button(150, 450, 50, 100, BRIGHT_GREEN, GREEN, "Play Again", game_loop)
QUIT_BUTTON = classes.Button(550, 450, 50, 100, BRIGHT_RED, RED, "Quit", quitgame)
GO_BUTTON = classes.Button(150, 450, 50, 100, BRIGHT_GREEN, GREEN, "Go!", game_loop)

#Setting up properties of the display window
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Let's Play!")   #Game name to be displayed in the title bar
GAME_ICON = pygame.image.load('./icons/present.png')    #Game icon to be displayed in the title bar
pygame.display.set_icon(GAME_ICON)
CLOCK = pygame.time.Clock()
