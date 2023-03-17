import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 800), 0, 0)

catImg = pygame.image.load('cat3.png')
Clock = pygame.time.Clock()
#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('splat.wav')
pygame.mixer.music.play(loops=-1)

catx = 10
caty = 10
direction = 'right'

while True:
    screen.fill('light steel blue')
    if direction == 'right':
         catx += 5
         if catx == 280:
             direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
         catx -= 5
         if catx == 10:
            direction = 'up'
    elif direction == 'up':
         caty -= 5
         if caty == 10:
            direction = 'right'
    screen.blit(catImg, (catx, caty))

    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    pygame.display.update()
    Clock.tick(20)
# Write your code here :-)
