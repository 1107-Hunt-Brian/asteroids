import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Starting Asteroids!")

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable_group, drawable_group)


    # Instantiate player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create some asteroids
    for _ in range(5):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        Asteroid(x, y)

    # Create the asteroid field (handles automatic spawning)
    asteroid_field = AsteroidField()

    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        # Handle quit events (so you can close the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable_group.update(dt)

        for asteroid in asteroids_group:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
        # Bullet-asteroid collisions
        for asteroid in asteroids_group:
            for shot in shots_group:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        # Fill screen with black (RGB 0,0,0)
        screen.fill((0, 0, 0))
        for obj in drawable_group:
            obj.draw(screen)

        # Refresh the screen (this should always be last in the loop)
        pygame.display.flip()

        

    # Quit pygame properly
    pygame.quit()

if __name__ == "__main__":
    main()

