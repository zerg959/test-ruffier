from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QVBoxLayout, QLabel, QPushButton
)

from instr import *

class TestWin(QWidget):
        def __init__(self):
            super().__init__()
            self.show()

        self.main_line = QVBoxLayout()
