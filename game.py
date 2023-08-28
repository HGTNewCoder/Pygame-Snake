#Library
from random import randrange
import pygame

#Resolution
WIDTH = 800
HEIGHT = 600

#SPEED
GAME_SPEED = 200

#COLOR
RED = (245, 66, 66)

#Initialize
pygame.init()
pygame.display.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Apple
class Apple:
    image = pygame.image.load("assets/apple.jpg").convert()
    image = pygame.transform.scale(image, (40, 40))

    def __init__(self):
        self.y = randrange(0, HEIGHT- 40, 40)
        self.x = randrange(0, WIDTH - 40, 40)
    def eaten(self):
        self.y = randrange(0, HEIGHT- 40, 40)
        self.x = randrange(0, WIDTH - 40, 40)
        print("Score!")
    def draw(self):
        screen.blit(apple.image, (apple.x, apple.y))

#Snake
class Snake:
    image = pygame.image.load("assets/block.jpg").convert()
    image = pygame.transform.scale(image, (40, 40))

    def __init__(self):
        self.y = randrange(0, HEIGHT- 40, 40)
        self.x = randrange(0, WIDTH - 40, 40)
        self.direction = 'down'
        self.size = 1
    def move_left(self):
        if self.direction == 'right':
            self.direction = 'right'
        else:
            self.direction = 'left'
    def move_right(self):
        if self.direction == 'left':
            self.direction = 'left'
        else:
            self.direction = 'left'
    def move_up(self):
        if self.direction == 'down':
            self.direction = 'down'
        else:
            self.direction = 'up'
    def move_down(self):
        if self.direction == 'up':
            self.direction = 'up'
        else:
            self.direction = 'down'

    def draw(self):
        screen.blit(snake.image, (snake.x, snake.y))

    def move(self):
        if self.direction == 'left':
            self.x -= 40
        if self.direction == 'right':
            self.x += 40
        if self.direction == 'up':
            self.y -= 40
        if self.direction == 'down':
            self.y += 40
    def eat(self, apple):
        if self.x == apple.x and self.y == apple.y:
            self.size += 1
            apple.eaten()

#Game Variable
background = pygame.image.load("assets/background.jpg").convert()
apple = Apple()
snake = Snake()

#Game Loop
START = True

while START:
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(GAME_SPEED)

    screen.blit(background, (0, 0))

    snake.draw()
    apple.draw()
    snake.move()
    snake.eat(apple)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            START = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                START = False
            if event.key == pygame.K_LEFT:
                snake.move_left()
            if event.key == pygame.K_RIGHT:
                snake.move_right()
            if event.key == pygame.K_UP:
                snake.move_up()
            if event.key == pygame.K_DOWN:
                snake.move_down()
            