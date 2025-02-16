import pygame
from constants import *  # Import SCREEN_WIDTH and SCREEN_HEIGHT

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Use constants
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB color for black

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()  # Cleanup after the game loop ends
