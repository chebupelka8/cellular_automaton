from Engine import *
from scripts.algorithms import Math


class ObjectGrid:
    def __init__(self, __matrix: list) -> None:
        self.__verify(__matrix)

        self.__matrix = __matrix
    
    def set(self, __matrix: list) -> None:
        self.__verify(__matrix)

        self.__matrix = __matrix
    
    def get(self) -> list:
        return self.__matrix
    
    @property
    def size(self) -> int:
        return len(self.__matrix)
    
    @classmethod
    def __verify(cls, __arg) -> None:
        match __arg:
            case arg if not cls.__verify_rows(*arg):
                raise ValueError("All rows must be equal in length")
            case arg if not len(arg) == len(arg[0]):
                raise ValueError("Columns and rows must be equal in lenght")

    @staticmethod
    def __verify_rows(*__rows) -> bool:
        length = len(__rows[0])

        for row in __rows: 
            if len(row) != length: return False
        
        return True
    
    def __repr__(self) -> str:
        return f"ObjectGrid(\n{"\n[".join(str(self.__matrix).split("[")).replace("\n", "", 2)}\n)"
    
    def __len__(self) -> int:
        return len(self.__matrix)

    def __getitem__(self, __index: int) -> int:
        return self.__matrix[__index]

class Grid:
    __current_grid = ObjectGrid([[1]])
    
    @classmethod
    def get(cls) -> list:
        return cls.__current_grid
    
    @classmethod
    def clear(cls) -> None:
        cls.__current_grid.set(Math.generate_grid(Vec2(cls.__current_grid.size, cls.__current_grid.size)))

    @classmethod
    def random_generate_grid(cls, __chance: int, __size: Vec2) -> None:
        cls.__current_grid.set(Math.generate_grid_with_chance(__chance, __size))
    
    @classmethod
    def generate_grid(cls, __size: Vec2, is_filled: bool = False) -> None:
        cls.__current_grid.set(Math.generate_grid(__size, is_filled))
    
    @classmethod
    def update_grid(cls) -> None:
        cls.__current_grid.set(Math.next_generation(cls.__current_grid.get()))

    @classmethod
    def draw_grid_lines(cls, loop: WindowLoop, __size: Vec2 = None) -> None:
        if __size == None:
            __size = Vec2(len(cls.__current_grid), len(cls.__current_grid))

        tile_size = Vec2(loop.window_width / __size.x, loop.window_height / __size.y)

        for i in range(1, __size.x):
            pygame.draw.line(loop.display, "#495057", (0, i * tile_size.x), (__size.x * tile_size.x, i * tile_size.x))
        
        for i in range(1, __size.y):
            pygame.draw.line(loop.display, "#495057", (i * tile_size.y, 0), (i * tile_size.y, __size.y * tile_size.y))
    
    @classmethod
    def draw_grid(cls, loop: WindowLoop) -> None:
        tile_size = Vec2(loop.window_width / cls.__current_grid.size, loop.window_height / cls.__current_grid.size)
        
        for col in range(cls.__current_grid.size):
            for row in range(cls.__current_grid.size):
                x, y = row * tile_size.x, col * tile_size.y

                if cls.__current_grid[col][row] == 1:
                    pygame.draw.rect(loop.display, "lightgreen", (x, y, tile_size.x, tile_size.y)) 