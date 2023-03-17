import pygame
import sys
width = 500
height = 500

size = (width, height)
screen = pygame.display.set_mode(size)

clock=pygame.time.Clock()

square = pygame.Rect((150, 400), (20, 20))

vx = 3
vy = 3

def draw(square):
    pygame.draw.rect(screen, 'red', square)

def update():
    global vx, vy
    square.x += vx
    square.y += vy
    if square.right > width or square.left < 0:
        vx = -vx
    if square.bottom > height or square.top < 0:
        vy = -vy

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('light steel blue')
    draw(square)
    update()

    clock.tick(50)
    pygame.display.update()
