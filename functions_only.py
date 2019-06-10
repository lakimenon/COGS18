""" Module containing all the functions and setup variables used for the game """

import random
import pygame
import classes_only

def display_scores(message, score, x_location, y_location):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render(message + str(score), True, black)
    gameDisplay.blit(text, (x_location, y_location))

def display_objects(item):
    gameDisplay.blit(item.icon, (item.x, item.y))

def display_button(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_bound = button.x + button.width > mouse[0] > button.x
    y_bound = button.y + button.height > mouse[1] > button.y
    button_dimensions = (button.x, button.y, button.width, button.height)

    if x_bound and y_bound:
        pygame.draw.rect(gameDisplay, button.active_color, button_dimensions)
        if click[0] == 1 and button.action != None:
            button.action()
    else:
        pygame.draw.rect(gameDisplay, button.inactive_color, button_dimensions)

    smallText = pygame.font.SysFont("freesansbold.ttf", 25)
    textSurf, textRect = text_objects(button.msg, smallText)
    textRect.center = ((button.x + (button.width/2)), (button.y + (button.height/2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def reset_location(object_name):
    object_name.y = 0 - object_name.height
    object_name.x = random.randrange(0, int(display_width-object_name.width))

def overlap(player, item):
    if player.y < item.y + item.height:
        left_overlap = item.x < player.x < item.x + item.width
        right_overlap = item.x < player.x + player.width < item.x + item.width
        middle_overlap = player.x < item.x and player. x + player.width > item.x + item.width
        overlapped = left_overlap or right_overlap or middle_overlap
        return overlapped

def rock_collected():
    medText2 = pygame.font.SysFont("freesansbold.ttf", 80)
    TextSurf, TextRect = text_objects("You Collected A Rock :(", medText2)
    TextRect.center = ((display_width/2), (display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_button(play_button)
        display_button(quit_button)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.SysFont("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("Let's Play!", largeText)
        TextRect.center = ((display_width/2), (display_height/3))

        word_width1, word_height1 = TextSurf.get_size()

        medText = pygame.font.SysFont("freesansbold.ttf", 40)
        description_line1 = "Collect presents and avoid rocks."
        TextSurf2, TextRect2 = text_objects(description_line1, medText)
        TextRect2.center = ((display_width/2), (display_height/3 + word_height1))

        word_width2, word_height2 = TextSurf2.get_size()

        description_line2 = "Use the left and right arrow keys to move. Good luck!"
        TextSurf3, TextRect3 = text_objects(description_line2, medText)
        TextRect3.center = ((display_width/2), (display_height/3 + word_height1 + word_height2))

        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)

        display_button(go_button)
        display_button(quit_button)

        pygame.display.update()
        clock.tick(15)

def game_loop():

    #high score is made global to ensure that it does not reset to 0 when a new game is started
    global high_score

    #placing player icon at the center bottom part of the screen
    x = (display_width * 0.45)
    y = (display_height - 94)   #94 pixels is the height of the icon
    startx = random.randrange(0, display_width)

    #Defining screen objects- numbers represent the dimensions (in px) of the respective icons
    player = classes_only.Player('basket.png', x, y, 94, 139, 0)
    rock = classes_only.Rock('rock.png', startx, -600, 48, 69, 4)
    present = classes_only.Present('present.png', startx, -100, 98, 82, 10)

    present_count = 0

    gameExit = False
    while not gameExit:

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
        gameDisplay.fill(bg_color)

        #Displaying all screen objects and scores
        display_objects(rock)
        display_objects(present)
        display_objects(player)

        display_scores("Presents Collected: ", present_count, 0, 0)
        display_scores("High Score: ", high_score, 0, 25)

        #Ensuring that the basket is within screen bounds
        if player.x > display_width - player.width:
            player.x = display_width - player.width

        if player.x < 0:
            player.x = 0

        #Making the rock drop again once it moves past the bottom of the screen
        if rock.y > display_height:
            reset_location(rock)
            rock.speed += 1 #Speed of the rock is increased each time it falls

        if present.y > display_height:
            reset_location(present)

        #When present is collected
        if overlap(player, present):
            reset_location(present)
            present_count += 1

        #When rock is collected
        if overlap(player, rock):
            if present_count > high_score:
                high_score = present_count
            rock_collected()

        #Making the rock and present move down the screen
        rock.y += rock.speed
        present.y += present.speed

        pygame.display.update()
        clock.tick(60)

#SETUP: The following blocks of code define variables and objects used throughout the functions

display_width = 800
display_height = 600
high_score = 0

#Assigning RGB value of each color to a variable having that color name
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bg_color = (53, 115, 255)

#Defining different buttons to be displayed
play_button = classes_only.Button(150, 450, 50, 100, bright_green, green, "Play Again", game_loop)
quit_button = classes_only.Button(550, 450, 50, 100, bright_red, red, "Quit", quitgame)
go_button = classes_only.Button(150, 450, 50, 100, bright_green, green, "Go!", game_loop)

#Setting up properties of the display window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's Play!")   #Game name to be displayed in the title bar
game_icon = pygame.image.load('present.png')    #Game icon to be displayed in the title bar
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
