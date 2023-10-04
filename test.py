# import
import pygame
import matplotlib.pyplot as plt
import numpy as np
import time

import matplotlib.animation as animation

from threading import Thread


def game():
    # initialize pygame
    pygame.init()

    # frame rate variables
    FPS = 120
    clock = pygame.time.Clock()

    # game variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    # colors
    BLUE = (0, 0, 255)

    # activate screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bonker")

    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            # init the sprite class
            pygame.sprite.Sprite.__init__(self)
            self.rect = pygame.Rect(0, 0, 40, 40)
            self.rect.x = x
            self.rect.y = y
            self.radius = 20
            self.destination = None
            self.moving = False
            self.dx = 0
            self.dy = 0

        def set_destination(self, pos):
            self.destination = pos
            # delta x and delta y
            self.dx = self.destination[0] - self.rect.centerx
            self.dy = self.destination[1] - self.rect.centery

            self.moving = True

        def move(self):
            if self.rect.centerx != self.destination[0]:
                if self.dx > 0:
                    self.rect.centerx += 1
                elif self.dx < 0:
                    self.rect.centerx -= 1

            if self.rect.centery != self.destination[1]:
                if self.dy > 0:
                    self.rect.centery += 1
                elif self.dy < 0:
                    self.rect.centery -= 1
            elif self.rect.center == self.destination:
                self.moving = False

        def draw(self):
            # draw the circle
            pygame.draw.circle(screen, BLUE, self.rect.center, self.radius)

    # create instances
    # player instance
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    player.draw()

    # main loop
    run = True
    movetime = 100
    move = False

    while run:
        # run frame rate
        dt = clock.tick(FPS)
        movetime -= dt
        if movetime <= 0:
            move = True
            movetime = 400

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player.set_destination(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        if player.moving:
            player.move()

        screen.fill((0, 0, 0))
        player.draw()
        pygame.display.update()

    pygame.quit()


def graphic():
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    
    def animate(i):
        data = open('stock.txt', 'r').read()
        lines = data.split('\n')
    
        xs = []
        ys = []
    
        for line in lines:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    
        ax.clear()
        ax.plot(xs, ys)
    
        plt.xlabel('Название')
        plt.ylabel('Цена')
        plt.title('График обновляемый в режиме реального времени')


    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()


if __name__ == "__main__":  
    Thread(target=graphic).start()
