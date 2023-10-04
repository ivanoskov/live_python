import pygame, random
from food import Food
from settings import *
import pymunk.pygame_util


def circles_intersect(
    position_a: pygame.Vector2, r_a: float, position_b: pygame.Vector2, r_b: float
) -> bool:
    distance_scr = (position_b.x - position_a.x) ** 2 + (
        position_b.y - position_a.y
    ) ** 2
    return distance_scr <= (r_a + r_b) ** 2


def circle_point_intersect(
    circle_position: pygame.Vector2, r: float, point: pygame.Vector2
) -> bool:
    distance_scr = (circle_position.x - point.x) ** 2 + (
        circle_position.y - point.y
    ) ** 2
    return distance_scr <= r**2


def generate_new_food() -> Food:
    position = pygame.Vector2(random.randint(0, WINDOW.x), random.randint(0, WINDOW.y))
    radius = radius = WINDOW.y // 150
    return Food(position=position, radius=radius, color=YELLOW)


def generate_walk_target(
    position: pygame.math.Vector2, radius: float
) -> pygame.Vector2:
    target = pygame.Vector2(-1, -1)
    while not (
        target.x >= 0
        and target.x <= WINDOW.x
        and target.y >= 0
        and target.y <= WINDOW.y
    ):
        target = pygame.Vector2(
            random.randint(
                int(position.x - radius * 10),
                int(position.x + radius * 10),
            ),
            random.randint(
                int(position.y - radius * 10),
                int(position.y + radius * 10),
            ),
        )
    return target


def generate_physic_frame(space: pymunk.Space):
    segment_shape = pymunk.Segment(space.static_body, (-1, 0), (-1, WINDOW.y), 1)
    space.add(segment_shape)
    segment_shape.elasticity = 0.4
    segment_shape.friction = 1.0
    segment_shape = pymunk.Segment(space.static_body, (0, -1), (WINDOW.x, -1), 1)
    space.add(segment_shape)
    segment_shape.elasticity = 0.4
    segment_shape.friction = 1.0
    segment_shape = pymunk.Segment(space.static_body, (WINDOW.x+1, 0), (WINDOW.x+1, WINDOW.y), 1)
    space.add(segment_shape)
    segment_shape.elasticity = 0.4
    segment_shape.friction = 1.0
    segment_shape = pymunk.Segment(space.static_body, (0, WINDOW.y), (WINDOW.x, WINDOW.y), 1)
    space.add(segment_shape)
    segment_shape.elasticity = 0.4
    segment_shape.friction = 1.0

