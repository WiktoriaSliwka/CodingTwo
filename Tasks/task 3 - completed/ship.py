import pygame
import numpy as np
import math
import utils

class Ship:
    def __init__(self, x, y, surface):
        self.pos = np.array([x, y])
        self.angle = 0.0
        self.surface = surface
        self.radius = 20
        self.color = (0, 0, 0)
        self.collided = False

    def update(self, mouse_pos, asteroids, game_status):
        if game_status != "started":
            return

        # Move toward mouse
        direction = mouse_pos - self.pos
        self.pos += direction * 0.1  # Smooth follow

        # Rotate toward mouse
        self.angle = math.atan2(direction[1], direction[0])

        self.collision(asteroids)

#flipped direction looks better
    def draw(self):
        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((-40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((-30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((-40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    def collision(self, asteroids):
        for asteroid in asteroids:
            if np.linalg.norm(asteroid.pos - self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 0, 0)
                self.collided = True
                break
