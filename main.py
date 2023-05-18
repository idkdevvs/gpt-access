import sys
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()