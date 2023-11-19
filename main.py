import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Second_file(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        # кнопка называется pushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Sf = Second_file()
    Sf.show()
    sys.exit(app.exec())
