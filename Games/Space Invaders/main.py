import pygame
import sys

# Initialize pygame
pygame.init()

# params -- window width, window height
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("./img/logo.png")
pygame.display.set_icon(icon)

# Player Model
avatar = pygame.transform.scale(
    pygame.image.load("./img/avatar.png"), (50, 50))
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(avatar, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += 1

    player(playerX, playerY)
    pygame.display.update()
