import pygame
import os
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('splat.wav')
pygame.mixer.music.play(loops=-1)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Simple animation')
background = pygame.image.load('stage.png')
clock = pygame.time.Clock()

img_list = ['boy1.png', 'boy2.png', 'boy3.png', 'boy4.png']
hero_img = pygame.image.load('boy1.png')
count = 0

while True:
    screen.blit(background, (0,0))
    hero_img = pygame.image.load(img_list[count % len(img_list)])
    count += 1
    screen.blit(hero_img, (75, 200))

    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    pygame.display.update()
    clock.tick(5)




'''_________________________________________________________________________'''

hero_list = [hero1,hero2,hero3,hero4]


clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x = 50
y = 770
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

spin = False
left = False
right = False
walkCount = 0
attackCount = 0

'''DRAWING SECTION___________________________________________________________'''
def redrawGameWindow():
    global walkCount
    global attackCount
    screen.blit(bg, (0,0))

    if walkCount + 1 >= 24:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
        attackCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
        attackCount += 1
    else:
        screen.blit(char, (x,y))

    if spin:
        screen.blit(spinAttackList[attackCount//3], (x,y))

    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
#_________________________________________________________________________
    if keys[pygame.K_w]:
        spin = True

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < WIDTH - 40:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        spin = False

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
