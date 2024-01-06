from GlobEngine.mainloop import *
from GlobEngine.locals import KEYDOWN
from GlobEngine.UI import Text
from numpy import random
import copy
import pygame

grid_size = [100, 100]
B, S = [3], [1, 2, 3, 4, 5]


array = [
    [0 for i in range(grid_size[0])] for i in range(grid_size[1])
]


def generate_random_number(persent: int = 10):
    num = random.random()
    if num < persent / 100:
        return 1
    else:
        return 0


def get_neighbors(pos: tuple[int, int], arr: list):
    row, col = pos

    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0]) and (i != row or j != col):
                neighbors.append(arr[i][j])

    return sum(neighbors)


def update_neighbors():
    global array

    next_generation = copy.deepcopy(array)

    for y in range(len(array)):
        for x in range(len(array[y])):
            neighbors = get_neighbors(pos=(y, x), arr=array)

            if array[y][x] == 1:  # if cell is alive
                if neighbors in S:
                    next_generation[y][x] = 1
                else:
                    next_generation[y][x] = 0

            if array[y][x] == 0:  # if cell is dead
                if neighbors in B:
                    next_generation[y][x] = 1

    array = copy.deepcopy(next_generation)


# Graphic
app = Mainloop("1200x1200", "#2d2d2d", 160, "Game of life")

text = Text("PAUSE", (8, 8), (10, 10), "#e9c46a")
tile_size = [app.width // grid_size[0], app.height // grid_size[1]]
pause = True
time = 0
scene = "game"


def events(event):
    global pause, array, tile_size, grid_size

    if event.type == KEYDOWN:
        if event.key == K_SPACE:  # step
            update_neighbors()

        if event.key == K_p:
            pause = True  # pause
        if event.key == K_o:
            pause = False  # unpause

        if event.key == K_c:  # clear grid
            pause = True
            array = [[0 for i in range(grid_size[0])]
                     for i in range(grid_size[1])]

        if event.key == K_r:  # generate random
            array = [[generate_random_number(30) for i in range(
                grid_size[0])] for i in range(grid_size[1])]

        if event.key == K_s:
            grid_size[0] += 1
            grid_size[1] += 1
            array = [[0 for i in range(grid_size[0])]
                     for i in range(grid_size[1])]
            tile_size = [app.width // grid_size[0], app.height // grid_size[1]]


while True:

    for col in range(len(array)):
        for row in range(len(array[col])):
            x, y = row * tile_size[0], col * tile_size[1]

            pygame.draw.rect(app.display, "#495057",
                             (x, y, tile_size[0], tile_size[1]), 1)

            if array[col][row] == 1:
                pygame.draw.rect(app.display, "lightgreen",
                                 (x, y, tile_size[0], tile_size[1]))

    if pygame.mouse.get_pressed()[0]:
        posx, posy = (pygame.mouse.get_pos()[
                      0] // tile_size[0], pygame.mouse.get_pos()[1] // tile_size[1])
        try:
            array[posy][posx] = 1
        except:
            pass

    if pygame.mouse.get_pressed()[2]:
        posx, posy = (pygame.mouse.get_pos()[
                      0] // tile_size[0], pygame.mouse.get_pos()[1] // tile_size[1])
        try:
            array[posy][posx] = 0
        except:
            pass

    time += 1

    if not pause and time >= 8:
        update_neighbors()
        time = 0
    if pause:
        text.draw(app.display)

    app.update()
    app.update_events(command=events)
