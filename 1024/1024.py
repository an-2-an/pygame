import pygame
import random
import itertools

pygame.init()
SIZE = 80
n = 7
start_2s = 8
PROBA = 0.5

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
YELLOW = (255, 255, 0)
MYFONT = pygame.font.SysFont('Comic Sans MS', 30)

window = pygame.display.set_mode((SIZE * n, SIZE * n))
pygame.display.set_caption('1024')

run = True

clock = pygame.time.Clock()
nums = [[0] * n for i in range(n)]

def get_random_empty_cell():
    items = [(i, j) for i, j in itertools.product(range(n), range(n)) if nums[i][j] == 0]
    # print(items)
    if len(items) > 0:
        return random.choice(items)
    else:
        return None

for i in range(start_2s):
    k, p = get_random_empty_cell()
    nums[k][p] = 2

def left_move():
    print('left move')
    for i in range(n):
        pressed = [e for e in nums[i] if e > 0]
        for j in range(len(pressed) - 1):
            if pressed[j] == pressed[j+1]:
                pressed[j] = 2 * pressed[j]
                pressed.pop(j+1)
                break
        nums[i] = pressed + [0] * (n - len(pressed))

def right_move():
    print('right move')
    for i in range(n):
        pressed = [e for e in nums[i] if e > 0]
        for j in range(len(pressed)-1, 0, - 1):
            if pressed[j] == pressed[j-1]:
                pressed[j] = 2 * pressed[j]
                pressed.pop(j-1)
                break
        nums[i] =  [0] * (n - len(pressed)) + pressed

def up_move():
    print('up move')
    for i in range(n):
        col_i = [nums[k][i] for k in range(n)]
        pressed = [e for e in col_i if e > 0]
        for j in range(len(pressed) - 1):
            if pressed[j] == pressed[j + 1]:
                pressed[j] = 2 * pressed[j]
                pressed.pop(j + 1)
                break
        col_i = pressed + [0] * (n - len(pressed))
        for k in range(n):
            nums[k][i] = col_i[k]

def down_move():
    print('down move')
    for i in range(n):
        col_i = [nums[k][i] for k in range(n)]
        pressed = [e for e in col_i if e > 0]
        for j in range(len(pressed) - 1, 0, - 1):
            if pressed[j] == pressed[j - 1]:
                pressed[j] = 2 * pressed[j]
                pressed.pop(j - 1)
                break
        col_i = [0] * (n - len(pressed)) + pressed
        for k in range(n):
            nums[k][i] = col_i[k]

def maybe():
    try:
        if random.random() < PROBA:
            k, p = get_random_empty_cell()
            nums[k][p] = 2
    except:
        run = False


def draw():
    window.fill(BLACK)
    #grid
    for i in range(n-1):
        pygame.draw.line(window, WHITE, (0, SIZE*(i+1)), (SIZE*n, SIZE*(i+1)))
        pygame.draw.line(window, WHITE, (SIZE * (i+1), 0), (SIZE * (i+1), SIZE * n))
    #nums
    for i, j in itertools.product(range(n), range(n)):
        if nums[i][j] > 0:
            if nums[i][j] == 2:
                color = GREEN
            elif nums[i][j] >= 128:
                color = WHITE
            elif nums[i][j] >= 32:
                color = YELLOW
            else:
                color = RED
            text = MYFONT.render(str(nums[i][j]), True, color)
            textRect = text.get_rect()
            textRect.center = (j * SIZE + SIZE//2, i * SIZE + SIZE//2)
            window.blit(text, textRect)
    pygame.display.update()


while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        left_move()
        maybe()

    if keys[pygame.K_RIGHT]:
        right_move()
        maybe()

    if keys[pygame.K_UP]:
        up_move()
        maybe()

    if keys[pygame.K_DOWN]:
        down_move()
        maybe()

    draw()

pygame.quit()
# print(nums)