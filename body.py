import pymunk.pygame_util
import random
from typing import Tuple
from settings import *


class Body:
    def __init__(
        self,
        physic_space: pymunk.Space,
        position: Tuple[int],
        size: int,
        mass: int,
    ) -> None:
        self.size = size
        self.mass = mass
        moment = pymunk.moment_for_circle(self.mass, 0, self.size, (0, 0))
        self.body: pymunk.Body = pymunk.Body(self.mass, moment)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, self.size, pymunk.Vec2d(0, 0))
        self.shape.elasticity = 0.8
        self.shape.friction = 1.0
        physic_space.add(self.body, self.shape)

    def force(self, force: Tuple[int]) -> None:
        self.body.apply_force_at_local_point(force, (0, 0))

