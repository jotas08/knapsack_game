import pygame, random
from pygame.locals import *
from colisao import collision, on_grid_random
from mochila import Mochila
from itens import Itens
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3




if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("KnapsackInventory")
    num_itens = 15
    active_box = None
    boxes = []
    

    for i in range(num_itens):
        x = random.randint(50, 700)
        y = random.randint(50, 500)
        width = random.randint(25, 65)
        height = random.randint(15, 105)
        box = Itens(x, y, width, height,"yellow")
        boxes.append(box)

    
    knacksack = Mochila(300,300,250,250,"white")

    # obj = [(200,200), (210,200), (220,200)]

    # skin = pygame.Surface((10,10))
    # skin.fill((255,255,255))

    # block_pos = on_grid_random()
    # block = pygame.Surface((10,10))
    # block.fill((255,0,0))

    # my_direction = LEFT

    clock = pygame.time.Clock()
    counter = 60
    text = str(counter).center(25)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Consolas", 50)

    running = True
    while running:
        clock.tick(20)
        screen.fill("purple")

        Mochila.draw(knacksack,screen)

        for box in boxes:
            box.draw(screen)
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).center(20) if counter > 0 else "boom!"
                if text =='boom!':
                    
                    running = False
                    
            for box in boxes:
                box.move_item(event)
                box.update()   

         
        """if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num 

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_box = None

            if event.type == pygame.MOUSEMOTION:
                if active_box != None:
                    boxes[active_box].move_ip(event.rel)"""

        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)

        # if event.type == KEYDOWN:
        #     if event.key == K_UP:
        #         my_direction = UP
        #     if event.key == K_DOWN:
        #         my_direction = DOWN
        #     if event.key == K_LEFT:
        #         my_direction = LEFT
        #     if event.key == K_RIGHT:
        #         my_direction = RIGHT
        # if event.type == MOUSEBUTTONDOWN:
        #     if event.key

        # if collision(obj[0], block_pos):
        #     block_pos = on_grid_random()
        #     obj.append((0,0))

        # for i in range(len(obj) -1,0,-1):
        #     obj[i] = (obj[i-1][0], obj[i-1][1])

        # if my_direction == UP:
        #     obj[0] = (obj[0][0], obj[0][1] - 10)

        # if my_direction == DOWN:
        #     obj[0] = (obj[0][0], obj[0][1] + 10)

        # if my_direction == RIGHT:
        #     obj[0] = (obj[0][0] + 10, obj[0][1])

        # if my_direction == LEFT:
        #     obj[0] = (obj[0][0] - 10, obj[0][1])

        # screen.fill((0,0,0))
        # screen.blit(block, block_pos)

        # for pos in obj:
        #     screen.blit(skin,pos)
        pygame.display.update()

    pygame.quit()
