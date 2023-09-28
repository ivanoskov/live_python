import pygame, random, math
from settings import *


pygame.init()
screen = pygame.display.set_mode((WINDOW.x, WINDOW.y))
screen.fill(GREY)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(GREY)

    # drawing

    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pygame.display.flip()
