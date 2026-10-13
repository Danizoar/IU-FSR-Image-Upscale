import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

import qdarktheme
import ctypes as ct

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FSR Image Upscaler")
        self.setFixedSize(QSize(960, 810))
        self.dark_title_bar()
        self.setWindowIcon(QIcon(r"assets\img\icon.ico"))

        # Variables
        self.file_filepath = ""
        self.folder_filepath = ""
        self.log_entry_number = 0

        # -- Frames --

        # -- About --

        # -- File Select --

        # -- Image Scaling --

        # -- Output --

        # -- Console Log --

        # -- Progress Panel --
    
    def dark_title_bar(self):
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = self.winId()
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
        self.setFixedSize(QSize(960, 810))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("auto")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
