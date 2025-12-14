import random
import pygame

from circleshape import *
from constants import *
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, screen):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_vector = self.velocity.rotate(random.uniform(20, 50))
        another_new_vector = self.velocity.rotate(random.uniform(-20, -50))
        new_raduis = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_raduis)
        another_new_asteroid = Asteroid(self.position.x, self.position.y, new_raduis)
        new_asteroid.velocity = new_vector * 1.2
        another_new_asteroid.velocity = another_new_vector * 1.2
        new_asteroid.draw(screen)
        another_new_asteroid.draw(screen)