from circleshape import CircleShape
import pygame
import random
from constants import *


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)

        direction_1 = self.velocity.rotate(angle)
        direction_2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid_1.velocity = direction_1 * 1.2
        asteroid_2.velocity = direction_2 * 1.2
