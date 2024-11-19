import pygame
from sys import exit
from constants import ASSET_PATH, HEIGHT, WIDTH
from helper import resource_path

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME TITLE")

clock = pygame.time.Clock()

font = pygame.font.Font(resource_path(ASSET_PATH + "Pixeltype.ttf"), 50)

sky_surface = pygame.image.load(resource_path(ASSET_PATH + "Sky.png"))
ground_surface = pygame.image.load(resource_path(ASSET_PATH + "ground.png"))
text_surface = font.render("Some text", True, "blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)
