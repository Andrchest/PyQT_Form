import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.uic import loadUi


class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        loadUi('UI.ui', self)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)

        ellipse_item = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse_item.setBrush(QColor(Qt.yellow))
        self.scene.addItem(ellipse_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MyForm()
    main_form.show()
    sys.exit(app.exec_())
