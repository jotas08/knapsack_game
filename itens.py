import pygame
from pygame.locals import *


class Itens (Rect):

    def __init__(self, x, y, width, height,color):
        super()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.dragging = False
     


    def draw(self, screen):
        item = pygame.Rect(self.x,self.y,self.width,self.height) 
        pygame.draw.rect(screen, self.color, item)

    def update(self):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y
  

    def move_item(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = mouse_x - self.x
                self.offset_y = mouse_y - self.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

