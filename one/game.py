import pygame

pygame.init()
SIZE = 500
win = pygame.display.set_mode((SIZE, SIZE))

pygame.display.set_caption('Cubes Game')


width, height = 60, 71
x, y = 5, SIZE - height - 5
speed = 5
color = (0, 0, 255)
DELAY = 50

run = True
is_jump = False
jump_count = 10
left, right = False, False
anim_frame = 0

walk_right = [pygame.image.load(f'pygame_right_{k}.png') for k in range(1, 7)]
walk_left = [pygame.image.load(f'pygame_left_{k}.png') for k in range(1, 7)]
stand = pygame.image.load('pygame_stand.png')
bg = pygame.image.load('pygame_bg.jpg')

clock = pygame.time.Clock()

def draw():
    global anim_frame

    win.blit(bg, (0, 0))
    if anim_frame == 30:
        anim_frame = 0
    if left:
        win.blit(walk_left[anim_frame // 5], (x, y))
        anim_frame += 1
    elif right:
        win.blit(walk_right[anim_frame // 5], (x, y))
        anim_frame += 1
    else:
        win.blit(stand, (x, y))

    # win.fill((0, 0, 0))
    # win.blit(bg, (0, 0))
    # pygame.draw.rect(win, color, (x, y, width, height))
    pygame.display.update()

while run:
    # pygame.time.delay(DELAY)
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left, right = True, False
    elif keys[pygame.K_RIGHT] and x < (SIZE - width - speed):
        x += speed
        left, right = False, True
    else:
        left, right = False, False
        anim_frame = 0

    if not is_jump:
        # if keys[pygame.K_UP] and y > speed:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < (SIZE - height - speed):
        #     y += speed
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw()

pygame.quit()