import pygame, random
from settings import *
from food import Food
from utils import *
from typing import Tuple
import pymunk.pygame_util
from body import Body


class Produser:
    def __init__(
        self,
        physic_space: pymunk.Space,
        position: Tuple[int],
        size: int,
        mass: int,
        energy: int,
    ) -> None:
        self.body = Body(
            physic_space=physic_space, position=position, size=size, mass=mass
        )
        self.timer = 0

    def update(self, delta: int, produsers, space) -> None:
        if self.timer >= 100:
            self.energy += 2
            self.timer = 0

        if self.energy >= produsers_max_energy:
            self.energy = produsers_base_energy
            produsers.append(
                Produser(
                    physic_space=space,
                    position=(
                        self.body.body.position.x + random.random() - 0.5,
                        self.body.body.position.y + random.random() - 0.5,
                    ),
                    size=produsers_base_size,
                    mass=produsers_base_mass,
                    energy=random.randint(0, produsers_max_energy),
                )
            )
        elif self.energy <= 0:
            produsers.remove(self)

        self.timer += delta
