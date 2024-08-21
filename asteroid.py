import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position+=self.velocity*dt
    
    def split(self):
        self.kill()
        new_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            a = pygame.math.Vector2.rotate(self.velocity, new_angle)
            b = pygame.math.Vector2.rotate(self.velocity, -new_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            na=Asteroid(*self.position, new_rad)
            nb=Asteroid(*self.position, new_rad)
            na.velocity = a*1.2
            nb.velocity = b*1.2
