#Library
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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Apple
class Apple:
    image = pygame.image.load("assets/apple.jpg")
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    image = pygame.image.load("assets/block.jpg")
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Game Variable
background = pygame.image.load("assets/background.jpg")

# apple = pygame.image.load("assets/apple.jpg")

apple = Apple(0, 0)
#Game Loop
START = True

while START:
    pygame.display.flip()
    pygame.display.update()

    screen.blit(background, (0, 0))
    screen.blit(apple.image, (apple.x, apple.y))
    screen.blit(snake.image, (snake.x, snake.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            START = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                START = False
