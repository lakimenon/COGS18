""" Module containing all the classes used. """

import pygame

class ScreenObjects:
    """ Super class for all objects displayed on the screen."""   
    
    def __init__(self, x, y, height, width):
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

class Button(ScreenObjects):
    """ Subclass for the buttons on the screen """
    
    def __init__(self, x, y, height, width, active_color, inactive_color, msg, action):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x, y, height, width: As defined in superclass ScreenObjects

        active_color : tuple
            RGB coordinates for the color of the button when the mouse is over it

        inactive_color : tuple
            RGB coordinates for the color of the button when the mouse is not over it

        msg : string
            Message displayed on the button

        action : function name
            Name of the function to be executed when the button is clicked
        """ 
        super().__init__(x, y, height, width)
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.msg = msg
        self.action = action
    
class Player(ScreenObjects):
    """ Subclass for the player icon """
    
    def __init__(self, icon, x, y, height, width, x_change):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x, y, height, width: As defined in superclass ScreenObjects

        icon: string
            Filename of the image to be used to represent the object on the screen

        x_change : float
            Change in x value when arrow keys are pressed
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon)
        self.x_change = x_change

class Present(ScreenObjects):
    """ Subclass for the presents """
    
    def __init__(self, icon, x, y, height, width, speed):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x, y, height, width: As defined in superclass ScreenObjects

        icon: string
            Filename of the image to be used to represent the object on the screen

        speed : float
            Speed at which the present falls
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon)
        self.speed = speed

class Rock(ScreenObjects):
    """ Subclass for the rocks """

    def __init__(self, icon, x, y, height, width, speed):
        """ Function to initialize the object and its attributes 

        Parameters:
        -----------
        x, y, height, width: As defined in superclass ScreenObjects

        icon: string
            Filename of the image to be used to represent the object on the screen

        speed : float
            Speed at which the rock falls
        """ 
        super().__init__(x, y, height, width)
        self.icon = pygame.image.load(icon)
        self.speed = speed
