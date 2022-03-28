#Library
from turtle import screensize
import pygame

#Resolution
WIDTH = 800
HEIGHT = 600
#COLOR
RED = (245, 66, 66)

#Initialize
pygame.init()
pygame.display.init()
pygame.display.set_caption("Game")

#Game Variable
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/background.jpg")

#Game Loop
START = True

while START:
    pygame.display.flip()
    pygame.display.update()

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            START = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                START = False
