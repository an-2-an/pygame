import pygame
import random

SIZE = (800, 600)
BLOCK_W = SIZE[0] // 10
BLOCK_H = SIZE[1] // 10
SPEED = (5, -10)

x, y = random.randint(10, 70) * 10, SIZE[1] - 50

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
TIMES = 50
run = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
CORAL = (100, 50, 31)
BLUE = (0, 0, 255)
COLORS = [RED, GREEN, BLUE, CORAL, YELLOW, GREY, WHITE]

# bg = pygame.image.load('bg.jpg')

class Block:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = random.choice(COLORS)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + BLOCK_W, self.y))
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x, self.y + BLOCK_H))

    def collides(self, x, y):
        return (self.x < x < self.x + BLOCK_W) and (self.y < y < self.y + BLOCK_H)

blocks = []

for row in range(5):
    for col in range(10):
        blocks.append(Block(col * BLOCK_W, row * BLOCK_H, BLOCK_W, BLOCK_H))

class Ball:
    def __init__(self, x, y):
        self.radius = 20
        self.x = x
        self.y = y
        self.vx, self.vy = SPEED
        self.color = WHITE
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def bounce_h(self):
        self.vx = -self.vx
    def bounce_v(self):
        self.vy = -self.vy

ball = Ball(x, y)

class Pad:
	def __init__(self, x):
		self.x = x
		self.width = SIZE[0] // 5
		self.height = SIZE[1] // 10
	def draw(self):
		pygame.draw.rect(screen, WHITE, 
			(self.x - self.width, SIZE[1] - self.height, self.width * 2, self.height))
		# print('pad')

pad = Pad(SIZE[0] // 2)

def draw():
    screen.fill(BLACK)
    # screen.blit(bg, (0, 0))
    for block in blocks:
        block.draw()
    ball.draw()
    pad.draw()

    pygame.display.update()

stop = False

while run:
    clock.tick(TIMES)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
    	if pad.x > 50:
    		pad.x -= 50

    if keys[pygame.K_RIGHT]:
    	if pad.x < SIZE[0] - 50:
    		pad.x += 50

    ball.move()

    if ball.y == (SIZE[1] - pad.height - ball.radius) and\
     (pad.x - pad.width <= ball.x <= pad.x + pad.width) and\
      ball.vy > 0:
    	ball.bounce_v()

    if ball.x == 0 or ball.x == SIZE[0]:
        ball.bounce_h()
    if ball.y == 0:
        ball.bounce_v()
    if ball.y == SIZE[1]:
    	stop = True
    for block in blocks:
        if block.collides(ball.x, ball.y):
            ball.bounce_v()
            ball.color = block.color
            blocks.pop(blocks.index(block))

    if len(blocks) == 0:
        stop = True

    if stop:
    	ball.vx = 0
    	ball.vy = 0

    draw()

pygame.quit()
