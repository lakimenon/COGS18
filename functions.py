import pygame
import time
import random

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
    
class Coin(ScreenObjects):
    
    def __init__(self, x, y, height, width, speed, color):
        super().__init__(x, y, height, width)
        self.speed = speed
        self.color = color

class Obstacle(ScreenObjects):
    
    def __init__(self, x, y, height, width, speed, color):
        super().__init__(x, y, height, width)
        self.speed = speed
        self.color = color


def coins_collected(count):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render("Coins: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def display_high_score(score):
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text = font.render("High Score: "+str(score), True, black)
    gameDisplay.blit(text,(0, 25))

def display_obstacles(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def display_coins(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def display_player(x,y):
    gameDisplay.blit(playerIcon,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def crash():
    largeText = pygame.font.SysFont("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
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
        
    smallText = pygame.font.SysFont("freesansbold.ttf",20)
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
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

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

display_width = 800
display_height = 600


black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
obstacle_color = (53, 115, 255)
coin_color = (156, 200, 120)

play_button = Button(150, 450, 50, 100, bright_green, green, "Play Again")
quit_button = Button(550, 450, 50, 100, bright_red, red, "Quit")
go_button = Button(150, 450, 50, 100, bright_green, green, "Go!")

high_score = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
playerIcon = pygame.image.load('racecar.png')




def game_loop():
    
    global high_score

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    player = Player(x, y, 100, 80, 0)
 
    startx = random.randrange(0, display_width) 
    obstacle = Obstacle(startx, -600, 100, 100, 4, obstacle_color)
    coin = Coin(startx, -100, 50, 50, 10, coin_color)

 
    coin_count = 0

 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -5
                if event.key == pygame.K_RIGHT:
                    player.x_change = 5                   
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_change = 0
 
        player.x += player.x_change
        gameDisplay.fill(white)
 
        display_obstacles(obstacle.x, obstacle.y, obstacle.width, obstacle.height, obstacle.color)
        display_coins(coin.x, coin.y, coin.width, coin.height, coin.color)
 
        obstacle.y += obstacle.speed
        coin.y += coin.speed

        display_player(player.x, player.y)
        coins_collected(coin_count)
        display_high_score(high_score)
 
        if player.x > display_width - player.width or player.x < 0:
            if coin_count > high_score:
                high_score = coin_count
            crash()
 
        if obstacle.y > display_height:
            obstacle.y = 0 - obstacle.height
            obstacle.x = random.randrange(0,int(display_width-obstacle.width))
            obstacle.speed += 1
            obstacle.width = random.randint(70, 100)
            obstacle.height = obstacle.width

        if overlap(player, coin):
            coin_count += 1
            coin.y = 0 - coin.height
            coin.x = random.randrange(0,int(display_width-coin.width))
 
        if coin.y > display_height:
            coin.y = 0 - coin.height
            coin.x = random.randrange(0,int(display_width-coin.width))
        
        if overlap(player, obstacle):
            if coin_count > high_score:
                high_score = coin_count
            crash()


        
        pygame.display.update()
        clock.tick(60)

