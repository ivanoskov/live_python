import pygame
from settings import *


class Food:
    def __init__(self, position: pygame.Vector2 = pygame.Vector2(10, 10), radius: int = 10, color: pygame.Color = WHITE) -> None:
        self.position = position
        self.radius = radius
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius)
