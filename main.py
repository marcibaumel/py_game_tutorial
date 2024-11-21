import pygame
from sys import exit
from constants import ASSET_PATH, HEIGHT, WIDTH
from helper import resource_path

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME TITLE")

clock = pygame.time.Clock()

font = pygame.font.Font(resource_path(ASSET_PATH + "Pixeltype.ttf"), 50)

sky_surface = pygame.image.load(resource_path(ASSET_PATH + "Sky.png")).convert()
ground_surface = pygame.image.load(resource_path(ASSET_PATH + "ground.png")).convert()

snail_surface = pygame.image.load(
    resource_path(ASSET_PATH + "snail1.png")
).convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

text_surface = font.render("GAME TITLE", True, "blue")

player_surf = pygame.image.load(
    resource_path(ASSET_PATH + "player_walk_1.png")
).convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint((event.pos)):
                print("Mouse collided with player")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4

    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("Collision")

    pygame.display.update()
    clock.tick(60)
