import random
from Engine import *
from scripts.config import B, S
import copy


class Math:
    
    @staticmethod
    def find_neighbors(__position: Vec2, __arr: list) -> int:
        row, col = __position.xy

        neighbors = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if not (not (0 <= i < len(__arr)) or not (j >= 0) or not (j < len(__arr[0]))) and (i != row or j != col):
                    neighbors.append(__arr[i][j])

        return sum(neighbors) 
    
    @staticmethod
    def __random(__arg: int) -> int:
        num = random.random()
        
        if num < __arg / 100: return 1
        return 0
    
    @classmethod
    def generate_grid_with_chance(cls, __arg: int, __size: Vec2) -> list:
        match __arg:
            case arg if not isinstance(arg, int):
                raise TypeError("Argument must be 'int'")
            case arg if arg not in range(0, 101):
                raise ValueError("Number must be in the range from 0 to 100")
        
        return [
            [cls.__random(__arg) for _ in range(__size.x)] for _ in range(__size.y)
        ]
    
    @staticmethod
    def generate_grid(__size: Vec2, is_filled: bool = False) -> list:
        if not is_filled:
            return [
                [0 for _ in range(__size.x)] for _ in range(__size.y)
            ]
        
        else:
            return [
                [1 for _ in range(__size.x)] for _ in range(__size.y)
            ]
    
    @classmethod
    def next_generation(cls, __array: list) -> list:
        __next_generation = copy.deepcopy(__array)

        for y in range(len(__array)):
            for x in range(len(__array[y])):
                neighbors = cls.find_neighbors(Vec2(y, x), __array)

                if __array[y][x] == 0:
                    if neighbors in B:
                        __next_generation[y][x] = 1

                if __array[y][x] == 1:
                    if neighbors in S:
                        __next_generation[y][x] = 1
                    else:
                        __next_generation[y][x] = 0

        return __next_generation
