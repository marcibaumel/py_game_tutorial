import pygame
from sys import exit 

ASSET_PATH = 'asset/'

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('GAME TITLE')
clock = pygame.time.Clock()

test_surface = pygame.image.load(ASSET_PATH+'Sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface, (200, 100))
    pygame.display.update()
    clock.tick(60)