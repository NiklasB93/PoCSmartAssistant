import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class GUI:
    def __init__(self):
        pass

    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()
        app.exec_()

    def change_image(self, idx):
        if idx == 1:
            mask = QtGui.QPixmap("cockpit.jpg")
        elif idx == 2:
            mask = QtGui.QPixmap("red_mask.png")

        mask = mask.scaledToWidth(600, QtCore.Qt.SmoothTransformation)

        self.window.change_image(mask)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas1 = QtGui.QPixmap("cockpit.jpg")
        canvas1 = canvas1.scaledToWidth(600, QtCore.Qt.SmoothTransformation)

        self.label.setPixmap(canvas1)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None

    def change_image(self, qpixmap):
        self.label.setPixmap(qpixmap)


    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.title = "PyQt5 Drawing Tutorial"
#         self.top = 150
#         self.left = 150
#         self.width = 500
#         self.height = 500
#         self.xcoord = 100
#
#         self.InitWindow()
#
#     def InitWindow(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)
#         self.show()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         pic = QPixmap("cockpit.jpg")
#         painter.drawPixmap(self.rect(), pic)
#         painter.setPen(QPen(Qt.red, 8))
#         painter.drawRect(int(self.xcoord), 40, 400, 200)
#         if self.xcoord > 1000:
#             self.xcoord = 100
#         else:
#             self.xcoord = self.xcoord + 5
#
#
#
# # class MyWidget(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.label = QLabel(self)
# #         self.pixmap = QPixmap("cockpit.jpg")
# #         self.pixmap = self.pixmap.scaledToWidth(1200, QtCore.Qt.SmoothTransformation)
# #         #self.label.setPixmap(self.pixmap)
# #
# #
# #         painter = QPainter(self)
# #         painter.drawPixmap(self.rect())
# #         painter.setPen(QPen(Qt.red, 8))
# #         painter.drawEllipse(200,200,100,100)
# #
# #
# #         self.grid = QGridLayout()
# #         self.grid.addWidget(self.label, 1, 1)
# #         self.setLayout(self.grid)
# #
# #         self.setGeometry(50, 50, 1200, 1200)
# #         self.setWindowTitle("PyQT show image")
# #         self.show()
# #
# #
# #
# # def
