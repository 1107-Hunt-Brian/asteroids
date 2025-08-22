import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Starting Asteroids!")
    
    # Game loop (infinite for now)
    running = True
    while running:
        # Handle quit events (so you can close the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Step 3: drawing
        # Fill screen with black (RGB 0,0,0)
        screen.fill((0, 0, 0))

        # Refresh the screen (this should always be last in the loop)
        pygame.display.flip()

    # Quit pygame properly
    pygame.quit()

if __name__ == "__main__":
    main()

