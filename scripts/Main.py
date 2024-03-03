import pygame, sys
from Settings import *
from Levels import Level

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
level = Level(levelMap, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)