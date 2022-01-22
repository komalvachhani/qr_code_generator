import os
import sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt

class QRCodeApp (QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200,800)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = QRCodeApp()
    demo.show

    sys.exit(app.exec_())
