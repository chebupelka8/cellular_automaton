from scripts import *
from widgets import *


class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(WINDOW_SIZE, 165)

        self.set_window_icon(Image("assets/icon.png", False))
        self.pause = Pause(Vec2(10, 10))
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            if __event.key == K_s:
                Grid.update_grid()
            
            if __event.key == K_c:
                Grid.clear()
            
            if __event.key == K_r:
                Grid.random_generate_grid(50, Vec2(100, 100))

            if __event.key == K_SPACE:
                self.pause.click_update(True, True, not self.pause.pause_option)
        
        if self.pause.rectangle.collidepoint(pygame.mouse.get_pos()):
            self.pause.click_update(True, False)
            if __event.type == MOUSEBUTTONUP:
                
                if __event.button == 1:
                    self.pause.click_update(True, True, not self.pause.pause_option)
        
        else:
            super().update_events(__event)
    
    def main(self) -> None:
        while True:
            if not self.pause.pause_option:
                Grid.update_grid()
            
            Grid.draw_grid(self)
            Grid.draw_grid_lines(loop=self)

            self.pause.draw(self.display)

            self.update_display()


if __name__ == "__main__":
    # def application():
    #     app = QApplication([])
    #
    #     widget = MainWidget()
    #     widget.show()
    #
    #     app.exec()
    
    # threading.Thread(target=application).start()
    Main().main()
    
    
    