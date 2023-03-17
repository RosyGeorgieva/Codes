import pygame
import sys
import random

width = 800
height =600

score = 0
speed = 5

player_size = 50
player_pos = [width/2, height-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, width - enemy_size), 0]
enemy_list = [enemy_pos]

pygame.init()

size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.update()

game_over = False
clock=pygame.time.Clock()

myFont =pygame.font.SysFont('monospace',35,True,True)

def set_level(score, speed):
    if score < 20:
        speed = 3
    elif score < 40:
        speed = 4
    elif score < 60:
        speed = 5
    else:
        speed = 15
    return speed

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list)<10 and delay<0.1:
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.circle(screen, 'dark blue', (enemy_pos[0], enemy_pos[1]),10)

def update_position(enemy_list,score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >=0 and enemy_pos[1]< height:
            enemy_pos[1]+=speed
        else:
            enemy_list.pop(idx)
            score+=1
    return score

def check_collision(enemy_list,player_pos):
        for enemy_pos in enemy_list:
            if detect_collision(player_pos,enemy_pos):
                return True
        return False

def detect_collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x>=p_x and e_x<(p_x+player_size)) or (p_x>=e_x and p_x<(e_x+enemy_size)):
        if (e_y>=p_y and e_y<(p_y+player_size)) or (p_y>=e_y and p_y<(e_y+enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y]

    screen.fill('light steel blue')

    drop_enemies(enemy_list)
    score = update_position(enemy_list,score)
    speed = set_level(score, speed)

    text = 'Score:' + str(score)
    label = myFont.render(text, 0, 'red')
    screen.blit(label,(width-200,height-40))

    if check_collision(enemy_list,player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen,'maroon',(player_pos[0],player_pos[1],player_size,player_size/2))
    clock.tick(30)
    pygame.display.update()
