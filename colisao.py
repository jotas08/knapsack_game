import random

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def on_grid_random():
    x = random.randint(0,580)
    y = random.randint(0,580)
    return (x//10 * 10, y//10 * 10)