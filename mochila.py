import pygame 
from Observer import *
from Subject import *

class Mochila(Observer):

    def __init__(self, x,y,width,height,color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        

    
    def draw(self,screen):  
        mochila = pygame.Rect(self.x, self.y, self.width, self.height)      
        pygame.draw.rect(screen, self.color, mochila)


    def update(self, subject: Subject):
        if subject._state == True:
            return "You win"
