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
        
        else:
            super().update_events(__event)
    
    def main(self) -> None:
        Grid.random_generate_grid(50, Vec2(50, 50))

        while True: # mainloop
            
            Grid.update_grid()
            Grid.draw_grid(self)
            Grid.draw_grid_lines(loop=self)

            self.update_display()


if __name__ == "__main__":
    Main().main()