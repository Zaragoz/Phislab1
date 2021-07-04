import sys

from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QtWidgets.QWidget):
    def setupUi(self, mainwindow):
        mainwindow.resize(333, 333)
        self.vbox = QtWidgets.QVBoxLayout()
        mainwindow.setLayout(self.vbox)
        self.btn = QtWidgets.QPushButton()
        self.vbox.addWidget(self.btn)
        self.btn.clicked.connect(mainwindow.open)
class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
    def open(self):
        self.ex = MyGraphicView()
        self.ex.show()

class GraphicView(QtWidgets.QGraphicsView):
    def setupUi(self, gh):
        self.s = QtWidgets.QGraphicsScene()
        gh.setScene(self.s)
        self.item = self.s.addRect(0, 0, 30, 30)

class MyGraphicView(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.ui = GraphicView()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())