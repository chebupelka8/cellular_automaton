from PySide6.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
    QButtonGroup, QCheckBox, QLabel
)
from PySide6.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.resize(600, 600)

        self.mainLayout = QHBoxLayout()
        self.vertLayoutB = QVBoxLayout()
        self.vertLayoutS = QVBoxLayout()
        self.checkBoxGroupB = []
        self.checkBoxGroupS = []

        self.pButton = QPushButton("Save")

        for _ in range(8): self.checkBoxGroupB.append(QCheckBox())
        for _ in range(8): self.checkBoxGroupS.append(QCheckBox())

        self.setup_ui()
        self.__set_checked(*get_rules())

    def setup_ui(self) -> None:
        self.pButton.clicked.connect(lambda: set_rules(*self.get_checked()))

        self.vertLayoutB.addWidget(QLabel("Born"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.vertLayoutS.addWidget(QLabel("Still Live"), alignment=Qt.AlignmentFlag.AlignCenter)
        
        for i, button in enumerate(self.checkBoxGroupB):
            button.setText(str(i + 1))
            self.vertLayoutB.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        for i, button in enumerate(self.checkBoxGroupS):
            button.setText(str(i + 1))
            self.vertLayoutS.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.mainLayout.addLayout(self.vertLayoutB)
        self.mainLayout.addLayout(self.vertLayoutS)
        self.mainLayout.addWidget(self.pButton, alignment=Qt.AlignmentFlag.AlignBottom)
        
        self.setLayout(self.mainLayout)
    
    def get_checked(self) -> list[list]:
        b = [int(i.text()) for i in self.checkBoxGroupB if i.isChecked()]
        s = [int(i.text()) for i in self.checkBoxGroupS if i.isChecked()]

        return [b, s]

    def __set_checked(self, __b: list, __s: list) -> None:
        for button in self.checkBoxGroupB:
            if int(button.text()) in __b:
                button.setChecked(True)
        
        for button in self.checkBoxGroupS:
            if int(button.text()) in __s:
                button.setChecked(True)