import turtle

tile_size = 64
width = tile_size * 8
height = tile_size * 8

tiles = ['empty', 'wall', 'goal', 'door', 'key']
unlock = 0

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 3, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

player = Actor('player', anchor=(0, 0), pos=(1 * tile_size, 1 * tile_size))
enemy = Actor('enemy', anchor=(0, 0), pos=(3 * tile_size, 6 * tile_size))
enemy.yv = -1

def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * tile_size
            y = row * tile_size
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    player.draw()
    enemy.draw()

def on_key_down(key):
    # движение на играча
    row = int(player.y / tile_size)
    column = int(player.x / tile_size)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    tile = tiles[maze[row][column]]
    if tile == 'empty':
        x = column * tile_size
        y = row * tile_size
        animate(player, duration=0.1, pos=(x, y))
    global unlock
    if tile == 'goal':
        print('Well done')
        exit()
    elif tile == 'key':
        unlock = unlock + 1
        maze[row][column] = 0 # 0  празна плочка
    elif tile == 'door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 # 0 празна плочка

    # движение на врага
    row = int(enemy.y / tile_size)
    column = int(enemy.x / tile_size)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == 'wall':
        x = column * tile_size
        y = row * tile_size
        animate(enemy, duration=0.1, pos=(x, y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print('You died')
        exit()
# Write your code here :-)
