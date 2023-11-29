import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('123')
        self.btn = QPushButton('Draw', self)
        self.btn.move(70, 150)
        self.btn.resize(60, 40)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_flag(painter)
            painter.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, painter):
        a = random.randint(10, 100)
        r = 255
        g = 255
        b = 0
        painter.setBrush(QColor(r, g, b))
        painter.drawEllipse(random.randint(0, 200), random.randint(0, 200), a, a)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())

