import pygame
from pygame.locals import *
from colisao import collision, on_grid_random

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('KnapsackInventory')
    
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    obj = [(200,200), (210,200), (220,200)]
    
    skin = pygame.Surface((10,10))
    skin.fill((255,255,255))
    
    block_pos = on_grid_random()
    block = pygame.Surface((10,10))
    block.fill((255,0,0))
    
    my_direction = LEFT
    
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_RIGHT:
                    my_direction = RIGHT
                    
        if collision(obj[0], block_pos):
            block_pos = on_grid_random()
            obj.append((0,0))
            
        for i in range(len(obj) -1,0,-1):
            obj[i] = (obj[i-1][0], obj[i-1][1])
        
        if my_direction == UP:
            obj[0] = (obj[0][0], obj[0][1] - 10)
        
        if my_direction == DOWN:
            obj[0] = (obj[0][0], obj[0][1] + 10)
            
        if my_direction == RIGHT:
            obj[0] = (obj[0][0] + 10, obj[0][1])
            
        if my_direction == LEFT:
            obj[0] = (obj[0][0] - 10, obj[0][1])
            
        
                
        screen.fill((0,0,0))
        screen.blit(block, block_pos)
        
        for pos in obj:
            screen.blit(skin,pos)
        pygame.display.update()
        
    pygame.quit()