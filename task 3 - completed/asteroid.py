
import pygame
import numpy as np
from random import random

class Asteroid:
    def __init__(self, x, y, radius, surface):
        self.pos = np.array([x, y])
        self.vel = np.array([(random() - 0.5) * 4, (random() - 0.5) * 4])  # Random velocity
        self.surface = surface
        self.radius = radius

    def update(self):
        self.pos += self.vel #movement logic

        # Wrap around screen
        if self.pos[0] > self.surface.get_width():
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = self.surface.get_width()

        if self.pos[1] > self.surface.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = self.surface.get_height()

    def draw(self):
        pygame.draw.circle(self.surface, (0, 0, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)
