# from pyqt5_plugins.examplebutton import QtWidgets
import sys

from PyQt5.QtWidgets import QApplication

from view.slotFunc.MarkingVideo_slot import MarkingVideoSlot

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MarkingVideoSlot()
    MainWindow.show()
    sys.exit(app.exec_())