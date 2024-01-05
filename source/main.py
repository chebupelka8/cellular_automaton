from Engine import *
from scripts.algorithms import Math
from scripts.grid import Grid
from scripts.ui import Pause
from scripts.config import *


class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(WINDOW_SIZE, 165)

        self.set_window_icon(Image("source/assets/icon.png", False))
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            Grid.update_grid()
        
        if self.pause.rectangle.collidepoint(pygame.mouse.get_pos()):
            self.pause.click_update(True, False)
            if __event.type == MOUSEBUTTONUP:
                
                if __event.button == 1:
                    self.pause.click_update(True, True, not self.pause.get_pause_option())
        
        else:
            super().update_events(__event)
    
    def main(self) -> None:
        Grid.random_generate_grid(50, Vec2(100, 100))
        self.pause = Pause(Vec2(10, 10))

        while True: # mainloop
            if not self.pause.get_pause_option(): Grid.update_grid()
            
            Grid.draw_grid(self)
            Grid.draw_grid_lines(loop=self)


            self.pause.draw(self.display)

            self.update_display()


if __name__ == "__main__":
    Main().main()