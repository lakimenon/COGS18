#IMPORTS###########################################################################

import pygame
import time
import random

#CLASSES############################################################################

class ScreenObjects:
    """ Super class for all objects displayed on the screen."""

   
    
    def __init__(self, x, y, height, width, icon = None):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x : float
            The x coordinate of the object's position

        y : float
            The y coordinate of the object's position

        height : float
            The height of the object

        width : float
            The width of the object
        """    

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.icon = icon

class Button(ScreenObjects):
    """ Subclass for the buttons on the screen """
    
    def __init__(self, x, y, height, width, active_color, inactive_color, msg, action):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x : float
            The x coordinate of the object's position

        y : float
            The y coordinate of the object's position

        height : float
            The height of the object

        width : float
            The width of the object

        active_color : tuple
            RGB coordinates for the color of the button when the mouse is over it

        inactive_color : tuple
            RGB coordinates for the color of the button when the mouse is not over it

        msg : string
            Message on the button
        """ 
        super().__init__(x, y, height, width)
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.msg = msg
        self.action = action
    
class Player(ScreenObjects):
    """ Subclass for the player icon """
    
    def __init__(self, icon_name, x, y, height, width, x_change):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        icon_name: string
            Filename of the object icon

        x : float
            The x coordinate of the object's position

        y : float
            The y coordinate of the object's position

        height : float
            The height of the object

        width : float
            The width of the object

        x_change : float
            Change in x value when arrow keys are pressed
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon_name)
        self.x_change = x_change

class Present(ScreenObjects):
    """ Subclass for the presents """
    
    def __init__(self, icon_name, x, y, height, width, speed):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        icon_name: string
            Filename of the object icon

        x : float
            The x coordinate of the object's position

        y : float
            The y coordinate of the object's position

        height : float
            The height of the object

        width : float
            The width of the object

        speed : float
            Speed at which the present falls
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon_name)
        self.speed = speed

class Rock(ScreenObjects):
    """ Subclass for the rocks """

    def __init__(self, icon_name, x, y, height, width, speed):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        icon_name: string
            Filename of the object icon

        x : float
            The x coordinate of the object's position

        y : float
            The y coordinate of the object's position

        height : float
            The height of the object

        width : float
            The width of the object

        speed : float
            Speed at which the rock falls
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon_name)
        self.speed = speed

#FUNCTIONS#########################################################################

def display_scores(message, score, x_location, y_location):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render(message + str(score), True, black)
    gameDisplay.blit(text,(x_location, y_location))    

def display_objects(item):
    gameDisplay.blit(item.icon, (item.x, item.y))   

def display_button(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button.x + button.width > mouse[0] > button.x and button.y + button.height > mouse[1] > button.y:
        pygame.draw.rect(gameDisplay, button.active_color, (button.x, button.y, button.width, button.height))
        if click[0] == 1 and button.action != None:
            button.action()         
    else:
        pygame.draw.rect(gameDisplay, button.inactive_color, (button.x, button.y, button.width, button.height))
            
    smallText = pygame.font.SysFont("freesansbold.ttf",25)
    textSurf, textRect = text_objects(button.msg, smallText)
    textRect.center = ( (button.x+(button.width/2)), (button.y+(button.height/2)) )
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def reset_location(object_name):
    object_name.y = 0 - object_name.height
    object_name.x = random.randrange(0,int(display_width-object_name.width))

def overlap(player, item):
    if player.y < item.y + item.height:
        left_overlap = player.x > item.x and player.x < item.x + item.width
        right_overlap = player.x + player.width > item.x and player.x + player.width < item.x + item.width 
        middle_overlap = player.x < item.x and player. x + player.width > item.x + item.width
        overlapped = left_overlap or right_overlap or middle_overlap
        return overlapped  
 
def rock_collected():
    medText2 = pygame.font.SysFont("freesansbold.ttf",80)
    TextSurf, TextRect = text_objects("You Collected A Rock :(", medText2)
    TextRect.center = ((display_width/2),(display_height/3))
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

        largeText = pygame.font.SysFont("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Let's Play!", largeText)
        TextRect.center = ((display_width/2),(display_height/3))

        word_width1, word_height1 = TextSurf.get_size()

        medText = pygame.font.SysFont("freesansbold.ttf",40)
        description_line1 = "Collect presents and avoid rocks."
        TextSurf2, TextRect2 = text_objects(description_line1, medText)
        TextRect2.center = ((display_width/2),(display_height/3 + word_height1))

        word_width2, word_height2 = TextSurf2.get_size()

        description_line2= "Use the left and right arrow keys to move. Good luck!"
        TextSurf3, TextRect3 = text_objects(description_line2, medText)
        TextRect3.center = ((display_width/2),(display_height/3 + word_height1 + word_height2))
        
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)

        display_button(go_button)
        display_button(quit_button)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    
    global high_score

    x = (display_width * 0.45)
    y = (display_height - 94)
    startx = random.randrange(0, display_width) 

    player = Player('basket.png', x, y, 94, 139, 0)
    rock = Rock('rock.png', startx, -600, 48, 69, 4)
    present = Present('present.png', startx, -100, 98, 82, 10)

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
                player.x_change = 0
 
        player.x += player.x_change
        gameDisplay.fill(bg_color)
 
        display_objects(rock)
        display_objects(present)
        display_objects(player)

        display_scores("Presents Collected: ", present_count, 0, 0)
        display_scores("High Score: ", high_score, 0, 25)
 
        if player.x > display_width - player.width:
            player.x = display_width - player.width

        if player.x < 0:
            player.x = 0
 
        if rock.y > display_height:
            reset_location(rock)
            rock.speed += 1

        if present.y > display_height:
            reset_location(present)

        if overlap(player, present):
            reset_location(present)
            present_count += 1
        
        if overlap(player, rock):
            if present_count > high_score:
                high_score = present_count
            rock_collected()

        rock.y += rock.speed
        present.y += present.speed
        
        pygame.display.update()
        clock.tick(60)

#SETUP#############################################################################

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

play_button = Button(150, 450, 50, 100, bright_green, green, "Play Again", game_loop)
quit_button = Button(550, 450, 50, 100, bright_red, red, "Quit", quitgame)
go_button = Button(150, 450, 50, 100, bright_green, green, "Go!", game_loop)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's Play!")
clock = pygame.time.Clock()
gameIcon = pygame.image.load('present.png')
pygame.display.set_icon(gameIcon)


###################################################################################
###################################################################################