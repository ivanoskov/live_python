import pygame, random, math
from settings import *
from entity import Entity
from food import Food
from utils import generate_new_food

pygame.init()
screen = pygame.display.set_mode((WINDOW.x, WINDOW.y))
screen.fill(GREY_34)
clock = pygame.time.Clock()

entities = []

for i in range(enities_num):
    position = pygame.Vector2(random.randint(0, WINDOW.x), random.randint(0, WINDOW.y))
    radius = WINDOW.y // 130
    color = GREEN
    entities.append(
        Entity(
            position=position, radius=radius, color=color, health=random.randint(15, 25)
        )
    )

foods = []

for i in range(foods_num):
    foods.append(generate_new_food())


while True:
    delta = clock.tick(FPS)
    screen.fill(GREY_34)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    # drawing

    for entity in entities:
        entity.update(delta, foods, entities)
        entity.draw(screen)

    for food in foods:
        food.draw(screen)

    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    pygame.display.flip()
