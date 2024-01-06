from GlobEngine.mainloop import Mainloop
from pygame.locals import *
from GlobEngine.UI import Text, FigureColorButton2D, Frame2D, CheckBox
from numpy import random
import copy
import pygame
from tkinter.filedialog import askopenfilename


def generate_random_number(percent: int = 10):
    num = random.random()
    if num < percent / 100:
        return 1
    else:
        return 0


def get_neighbors(pos: tuple[int, int], arr: list):
    row, col = pos

    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(arr) and j >= 0 and j < len(arr[0]) and (i != row or j != col):
                neighbors.append(arr[i][j])

    return sum(neighbors)


def _get_array(string: str) -> list:
    def find_numbers(string): return [int(i) for i in string if i.isdigit()]

    return [find_numbers(s) for s in string.split("\n") if s != ""]


def _get_string(array: list) -> str:
    return "\n".join(["".join(list(map(str, i))) for i in array])


class MainWindow(Mainloop):
    def __init__(self):
        super().__init__("1200x1200", "#2d2d2d", 160, "Game of life", show_fps=True)

        self.grid_size = [50, 50]
        # become alive | stay alive (else became dead)
        self.B, self.S = [3], [2, 3]

        self.tile_size = [self.width // self.grid_size[0],
                          self.height // self.grid_size[1]]
        self.pause = True
        self.time = 0
        self.scene = "game"

        self.array = [
            [0 for i in range(self.grid_size[0])] for i in range(self.grid_size[1])
        ]

        self.call_classes()

    def call_classes(self):
        # self.text = Text("p", (8, 8), (10, 10), "#e9c46a")

        self.uiGroup = pygame.sprite.Group()
        CheckBox((100, 100), True, (30, 30), (0, 200, 0),
                 ("#ffffff", 2), (4, 4, 4, 4), self.uiGroup)
        Frame2D((self.width // 2 - 740 // 2, self.height // 2 - 860 // 2), (740, 860), "#303030", ("white", 2),
                (0, 22, 22, 0), self.uiGroup)

    def _load_level(self):
        with open(askopenfilename(), "r") as file:
            self.array = _get_array(file.read())
            self.grid_size = [len(self.array[0]), len(self.array)]
            file.close()

    def update_neighbors(self):

        next_generation = copy.deepcopy(self.array)

        for y in range(len(self.array)):
            for x in range(len(self.array[y])):
                neighbors = get_neighbors(pos=(y, x), arr=self.array)

                if self.array[y][x] == 1:  # if cell is alive
                    if neighbors in self.S:
                        next_generation[y][x] = 1
                    else:
                        next_generation[y][x] = 0

                if self.array[y][x] == 0:  # if cell is dead
                    if neighbors in self.B:
                        next_generation[y][x] = 1

        self.array = copy.deepcopy(next_generation)

    def events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:  # step
                self.update_neighbors()

            if event.key == K_p:
                self.pause = True  # pause
            if event.key == K_o:
                self.pause = False  # unpause

            if event.key == K_c:  # clear grid
                self.pause = True
                self.array = [
                    [0 for i in range(self.grid_size[0])] for i in range(self.grid_size[1])]

            if event.key == K_r:  # generate random
                self.array = [[generate_random_number(50) for i in range(self.grid_size[0])] for i in
                              range(self.grid_size[1])]

            if event.key == K_s:
                self.grid_size[0] += 1
                self.grid_size[1] += 1
                self.array = [
                    [0 for i in range(self.grid_size[0])] for i in range(self.grid_size[1])]
                self.tile_size = [
                    self.width // self.grid_size[0], self.height // self.grid_size[1]]

            if event.key == K_q:  # open settings
                self.pause = True
                self.scene = "settings"

            if event.key == K_g:
                print(_get_string(self.array))

            if event.key == K_l:
                self._load_level()

    def settings(self):
        for sprite in self.uiGroup:
            sprite.draw(self.display)

        self.update()
        self.update_events()

    def game(self):
        for col in range(self.grid_size[1]):
            for row in range(self.grid_size[0]):
                x, y = row * self.tile_size[0], col * self.tile_size[1]

                if self.array[col][row] == 1:
                    pygame.draw.rect(self.display, "lightgreen",
                                     (x, y, self.tile_size[0], self.tile_size[1]))

        # grid
        for i in range(self.grid_size[0]):
            pygame.draw.line(self.display, "#495057", (0, i * self.tile_size[0]), (
                self.grid_size[0] * self.tile_size[0], i * self.tile_size[0]))
        
        for i in range(self.grid_size[1]):
            pygame.draw.line(self.display, "#495057", (i * self.tile_size[1], 0), (
                i * self.tile_size[1], self.grid_size[1] * self.tile_size[1]))

        if pygame.mouse.get_pressed()[0]:
            posx, posy = (
                pygame.mouse.get_pos()[0] // self.tile_size[0], pygame.mouse.get_pos()[1] // self.tile_size[1])
            try:
                self.array[posy][posx] = 1
            except:
                pass

        if pygame.mouse.get_pressed()[2]:
            posx, posy = (
                pygame.mouse.get_pos()[0] // self.tile_size[0], pygame.mouse.get_pos()[1] // self.tile_size[1])
            try:
                self.array[posy][posx] = 0
            except:
                pass

        self.time += 1

        if not self.pause and self.time >= 0:
            self.update_neighbors()
            self.time = 0

        self.update()
        self.update_events(command=self.events)

    def mainloop(self):
        while True:
            if self.scene == "game":
                self.game()
            if self.scene == "settings":
                self.settings()


if __name__ == "__main__":
    MainWindow().mainloop()
