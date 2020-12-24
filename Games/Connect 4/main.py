from pygame.locals import *
import pygame
import sys


def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Connect 4")
    icon = pygame.image.load("./img/logo.png")
    pygame.display.set_icon(icon)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Create grid
    boxWidth = boxHeight = 100
    x = y = 0
    for i in range(42):
        if(i % 7 == 0 and i > 1):
            x = 0
            y += 100
        rect = pygame.Rect(x, y, boxWidth, boxHeight)
        pygame.draw.rect(background, (0, 0, 0), rect, 1)
        print(i)
        x += 100

        # Display
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        if(background.get_rect().collidepoint(pygame.mouse.get_pos())):
            print('Im in the game!')
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
