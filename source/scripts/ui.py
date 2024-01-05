from Engine import *


class Pause(StaticSprite):
    def __init__(self, position: Vec2) -> None:
        self.paused_image = ImageEditor.mult_size(Image("source/assets/Play.png"), 1.2, 1.2)
        self.unpaused_image = Image("source/assets/Pause.png")

        super().__init__(position, self.paused_image)

        self.__is_paused = True

    def click_update(self, __hover: bool = False, __pressed: bool = False, is_pause: bool | None = None) -> None:
        if __hover:
            # print("hover")
            
            if not __pressed: return
            
            if __pressed and not is_pause:
                self.image = self.unpaused_image
                self.__is_paused = False
            
            if __pressed and is_pause:
                self.image = self.paused_image
                self.__is_paused = True
    
    @property
    def pause_option(self) -> bool:
        return self.__is_paused
    
    @pause_option.setter
    def pause_option(self, __other: bool) -> None:
        self.__is_paused = __other
