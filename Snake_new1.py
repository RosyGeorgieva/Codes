import pygame
import time
import random

width = 700
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 5

msg_font = pygame.font.SysFont("Times New Roman", 20)
score_font = pygame.font.SysFont("Times New Roman", 20)

def snake(snake_block, snake_list): #рисува змията
    for x in snake_list:
        pygame.draw.rect(screen, 'dark green', [x[0], x[1], snake_block, snake_block])

def total_score(score): #извежда резултата
    value = score_font.render("Score: " + str(score), True, 'dark blue')
    screen.blit(value, [0, 0])

def message(msg, color): #съобщение за край
    mesg = msg_font.render(msg, True, color)
    screen.blit(mesg, [width / 10, height / 3])

def draw_food(x, y, radius): #рисува храната
    pygame.draw.circle(screen, 'orange', [int(x), int(y)], radius)

def main():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_move = 0
    y1_move = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10
    while not game_over:
        while game_close == True:
            screen.fill('light steel blue')
            message('You Lost The Game! Press Y to play again or N to quit.', 'red')
            total_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_move = -snake_block
                    y1_move = 0
                elif event.key == pygame.K_RIGHT:
                    x1_move = snake_block
                    y1_move = 0
                elif event.key == pygame.K_UP:
                    y1_move = -snake_block
                    x1_move = 0
                elif event.key == pygame.K_DOWN:
                    y1_move = snake_block
                    x1_move = 0
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_move
        y1 += y1_move
        screen.fill('light steel blue')
        draw_food(foodx, foody, 10)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[-1]:
            if x == snake_head:
                game_close = True
        snake(snake_block, snake_list)
        total_score(snake_length - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
main()
