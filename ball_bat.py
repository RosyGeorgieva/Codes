import pygame
import sys

width = 500
height = 500
size = (width, height)

screen = pygame.display.set_mode(size)
Color=pygame.Color('light steel blue')

clock=pygame.time.Clock()

square = pygame.Rect((150, 400), (20, 20))
platform = pygame.Rect((200, 480), (60, 20))

vx = 3
vy = 3

def draw(square, platform):
    pygame.draw.rect(screen, 'dark red', square)
    pygame.draw.rect(screen, 'dark blue', platform)

def update():
    global vx, vy
    square.x += vx
    square.y += vy
    if square.right > width or square.left < 0:
        vx = -vx
    if square.colliderect(platform) or square.top < 0:
        vy = -vy
    if square.bottom > height:
        exit()
    if(keyboard.right):
        platform.x += 2
    elif(keyboard.left):
        platform.x -= 2

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('light steel blue')
    draw(square,platform)
    update()

    clock.tick(50)
    pygame.display.update()
