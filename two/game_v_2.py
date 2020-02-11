import pygame

pygame.init()
SIZE = 500
window = pygame.display.set_mode((SIZE, SIZE))

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
lastmove = 'right'

walk_right = [pygame.image.load('pygame_right_%d.png' % k) for k in range(1, 7)]
walk_left = [pygame.image.load('pygame_left_%d.png' % k) for k in range(1, 7)]
stand = pygame.image.load('pygame_stand.png')
bg = pygame.image.load('pygame_bg.jpg')

clock = pygame.time.Clock()
bullets = []


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x, self.y, self.radius, self.color, self.facing = x, y, radius, color, facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)
    def move(self):
        self.x += self.vel
                

def draw():
    global anim_frame

    window.blit(bg, (0, 0))
    if anim_frame == 30:
        anim_frame = 0
    if left:
        window.blit(walk_left[anim_frame // 5], (x, y))
        anim_frame += 1
    elif right:
        window.blit(walk_right[anim_frame // 5], (x, y))
        anim_frame += 1
    else:
        window.blit(stand, (x, y))

    for b in bullets:
        b.draw(window)
    
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

    for bullet in bullets:
        if 0 < bullet.x < SIZE:
            bullet.move()
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            if lastmove == 'right':
                facing = 1
            else:
                facing = -1
            bullets.append(Bullet(x + width // 2, y + height // 2, 10, (255, 0, 0), facing))
            
    
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left, right = True, False
        lastmove = 'left'
    elif keys[pygame.K_RIGHT] and x < (SIZE - width - speed):
        x += speed
        left, right = False, True
        lastmove = 'right'
    else:
        left, right = False, False
        anim_frame = 0

    if not is_jump:
        # if keys[pygame.K_UP] and y > speed:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < (SIZE - height - speed):
        #     y += speed
        if keys[pygame.K_UP]:
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
