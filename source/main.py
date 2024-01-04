from Engine import *
from scripts.algorithms import Math
from scripts.grid import Grid
from scripts.config import *


class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(WINDOW_SIZE, 165)
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            Grid.update_grid()    
            print(Grid.__dict__)
        
        else:
            super().update_events(__event)
    
    def main(self) -> None:
        # pprint(Math.generate_with_chance(50, Vec2(10, 10)))
        Grid.random_generate_grid(50, Vec2(50, 50))
        print(Grid.__dict__)

        while True: # mainloop
            
            Grid.update_grid()
            Grid.draw_grid(self)
            Grid.draw_grid_lines(loop=self)

            self.update_display()


if __name__ == "__main__":
    Main().main()