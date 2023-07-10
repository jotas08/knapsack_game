import pygame 


class Mochila:

    def __init__(self, x,y,width,height,color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.screen = screen
        

    
    def draw(self,screen):  
        mochila = pygame.Rect(self.x, self.y, self.width, self.height)      
        pygame.draw.rect(screen, self.color, mochila)



