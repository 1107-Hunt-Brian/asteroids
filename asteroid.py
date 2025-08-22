import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius=None):
        if radius is None:
            radius = random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
        super().__init__(x, y, radius)

        # Assign a random velocity if not set externally
        if not hasattr(self, "velocity"):
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)  # pixels per second
            self.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Kill the current asteroid
        self.kill()

        # If already small, do nothing more
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random split angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors rotated from current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # New radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn the two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2
