import pygame, random
from settings import *
from food import Food
from utils import (
    circles_intersect,
    generate_new_food,
    generate_walk_target,
    circle_point_intersect,
)


class Entity:
    def __init__(
        self,
        position: pygame.Vector2,
        radius: float,
        color: pygame.Color,
        health: float,
    ) -> None:
        self.position: pygame.Vector2 = position
        self.radius: float = radius
        self.color: pygame.Color = color
        self.selected_food: Food | None = None
        self.speed: float = 2
        self.vision_range: float = self.radius * 4
        self.walk_target: pygame.Vector2 | None = None
        self.health: float = health
        self.health_call = 0

    def update(self, delta, foods, entities) -> None:
        if not self.selected_food:
            self.find_food(foods=foods)
        else:
            if circles_intersect(
                self.position,
                self.radius,
                self.selected_food.position,
                self.selected_food.radius,
            ):
                if self.selected_food in foods:
                    foods.remove(self.selected_food)
                    foods.append(generate_new_food())
                    self.selected_food = None
                    self.health += 1
                else:
                    self.selected_food = None
            else:
                if not (self.selected_food in foods):
                    self.selected_food = None
                else:
                    self.go()
        if self.health_call >= health_time:
            self.health -= 1
            self.health_call = 0
            if self.health <= 0:
                entities.remove(self)
        else:
            self.health_call += delta + ((random.random() - 0.5) * (delta * 0.1))
        shaking = pygame.Vector2(
            random.randint(-1, 1) * 0.8, random.randint(-1, 1) * 0.8
        )
        self.position += shaking

    def find_food(self, foods) -> None:
        self.selected_food = foods[0]
        min_dist = self.position.distance_to(foods[0].position)
        for food in foods:
            distance = pygame.math.Vector2.distance_to(self.position, food.position)
            if (distance < min_dist) and (distance <= self.vision_range):
                min_dist = distance
                self.selected_food = food
                self.walk_target = None
        if min_dist > self.vision_range:
            self.selected_food = None
            self.walk()

    def go(self):
        self.position = self.position.move_towards(
            self.selected_food.position, self.speed
        )

    def walk(self):
        if not self.walk_target:
            self.walk_target = generate_walk_target(self.position, self.radius)
        else:
            if not circle_point_intersect(self.position, self.radius, self.walk_target):
                self.position = self.position.move_towards(self.walk_target, self.speed)
            else:
                self.walk_target = None

    def draw(self, screen: pygame.Surface) -> None:
        if self.selected_food:
            pygame.draw.line(screen, WHITE, self.position, self.selected_food.position)
        pygame.draw.circle(screen, GREY_37, self.position, self.vision_range)
        pygame.draw.circle(screen, self.color, self.position, self.radius)
