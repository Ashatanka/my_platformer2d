import pygame, sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()  # to control frames per second

# reading level_map and display it on our screen
level = Level(level_map, screen)

# MAIN LOOP
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # background
        screen.fill('black')
        level.run()  # draw a level

        pygame.display.update()
        clock.tick(60)  # set fps