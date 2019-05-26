#IMPORTS###########################################################################
import pygame
import time
import random

#CLASSES############################################################################


class ScreenObjects:
    
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
class Button(ScreenObjects):
    
    def __init__(self, x, y, height, width, active_color, inactive_color, msg):
        super().__init__(x, y, height, width)
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.msg = msg
    
class Player(ScreenObjects):
    
    def __init__(self, x, y, height, width, x_change):
        super().__init__(x, y, height, width)
        self.x_change = x_change

class Present(ScreenObjects):
    
    def __init__(self, x, y, height, width, speed):
        super().__init__(x, y, height, width)
        self.speed = speed

class Rock(ScreenObjects):
    
    def __init__(self, x, y, height, width, speed):
        super().__init__(x, y, height, width)
        self.speed = speed

#FUNCTIONS#########################################################################
    
def presents_collected(count):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render("Presents: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def display_high_score(score):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render("High Score: "+str(score), True, black)
    gameDisplay.blit(text,(0, 25))

def display_presents(x,y):
    gameDisplay.blit(presentIcon,(x,y))

def display_rocks(x,y):
    gameDisplay.blit(rockIcon,(x,y))    

def display_player(x,y):
    gameDisplay.blit(playerIcon,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def rock_collected():
    largeText = pygame.font.SysFont("freesansbold.ttf",80)
    TextSurf, TextRect = text_objects("You Collected A Rock :(", largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button(play_button, game_loop)
        button(quit_button, quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(button, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button.x + button.width > mouse[0] > button.x and button.y + button.height > mouse[1] > button.y:
        pygame.draw.rect(gameDisplay, button.active_color, (button.x, button.y, button.width, button.height))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, button.inactive_color, (button.x, button.y, button.width, button.height))
        
    smallText = pygame.font.SysFont("freesansbold.ttf",25)
    textSurf, textRect = text_objects(button.msg, smallText)
    textRect.center = ( (button.x+(button.width/2)), (button.y+(button.height/2)) )
    gameDisplay.blit(textSurf, textRect)
    

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
        description_line1 = "Collect presents and avoid rocks!"
        TextSurf2, TextRect2 = text_objects(description_line1, medText)
        TextRect2.center = ((display_width/2),(display_height/3 + word_height1))

        word_width2, word_height2 = TextSurf2.get_size()

        description_line2= "Use the left and right arrow keys to move. Good luck!"
        TextSurf3, TextRect3 = text_objects(description_line2, medText)
        TextRect3.center = ((display_width/2),(display_height/3 + word_height1 + word_height2))
        
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)


        button(go_button, game_loop)
        button(quit_button, quitgame)

        pygame.display.update()
        clock.tick(15)

def overlap(player, item):
    if player.y < item.y + item.height:
        left_overlap = player.x > item.x and player.x < item.x + item.width
        right_overlap = player.x + player.width > item.x and player.x + player.width < item.x + item.width 
        middle_overlap = player.x < item.x and player. x + player.width > item.x + item.width
        overlapped = left_overlap or right_overlap or middle_overlap
        return overlapped  

def game_loop():
    
    global high_score

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    player = Player(x, y, 94, 139, 0)
 
    startx = random.randrange(0, display_width) 

    rock = Rock(startx, -600, 48, 69, 4)
    present = Present(startx, -100, 98, 82, 10)

    present_count = 0

 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -7
                if event.key == pygame.K_RIGHT:
                    player.x_change = 7                   
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_change = 0
 
        player.x += player.x_change
        gameDisplay.fill(bg_color)
 

        display_rocks(rock.x, rock.y)
        display_presents(present.x, present.y)


        display_player(player.x, player.y)
        presents_collected(present_count)
        display_high_score(high_score)
 
        if player.x > display_width - player.width:
            player.x = display_width - player.width

        if player.x < 0:
            player.x = 0
 
        if rock.y > display_height:
            rock.y = 0 - rock.height
            rock.x = random.randrange(0,int(display_width-rock.width))
            rock.speed += 1

        if overlap(player, present):
            present_count += 1
            present.y = 0 - present.height
            present.x = random.randrange(0,int(display_width-present.width))
 
        if present.y > display_height:
            present.y = 0 - present.height
            present.x = random.randrange(0,int(display_width-present.width))
        
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

black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bg_color = (53, 115, 255)

high_score = 0

play_button = Button(150, 450, 50, 100, bright_green, green, "Play Again")
quit_button = Button(550, 450, 50, 100, bright_red, red, "Quit")
go_button = Button(150, 450, 50, 100, bright_green, green, "Go!")

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's Play!")
clock = pygame.time.Clock()

playerIcon = pygame.image.load('basket.png')
presentIcon = pygame.image.load('present.png')
rockIcon = pygame.image.load('rock.png')

###################################################################################
###################################################################################