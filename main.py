import pygame, random
from pygame.locals import *
from colisao import collision, on_grid_random
from mochila import Mochila

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

"""Dividir as partes do código main em classes, ui pra interface gráfica por exemplo, 
usar o observer pra colocar para os eventos de caixa entra na mochila, mochila cheia, fim do tempo,
pontuação total
Deixa a main responsável apenas por desenhar os objetos e gerenciar
o tempo do jogo (main loop e update)
Talvez no fim tenha 4 classes: mochila, objetos, UI, Observer
e a função main. 
Talvez seja legal ter uma tela de inicio também

Mochila responsável pela colisão ???? """


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("KnapsackInventory")

    active_box = None
    boxes = []
    

    for i in range(5):
        x = random.randint(50, 700)
        y = random.randint(50, 500)
        width = random.randint(35, 65)
        height = random.randint(35, 65)
        box = pygame.Rect(x, y, width, height)
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
    counter, text = 10, "10".rjust(25)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Consolas", 50)

    running = True
    while running:
        clock.tick(20)
        screen.fill("purple")

        Mochila.draw(knacksack,screen)

       #pygame.draw.rect(screen, "black",knacksack,
        #                border_top_right_radius=10,border_top_left_radius=10 ) */

        for box in boxes:
            pygame.draw.rect(screen, "yellow", box)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(20) if counter > 0 else "boom!"
                #if counter == 0:
                 #   running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_box = None

            if event.type == pygame.MOUSEMOTION:
                if active_box != None:
                    boxes[active_box].move_ip(event.rel)

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
