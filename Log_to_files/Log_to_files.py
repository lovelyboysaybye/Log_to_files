import sys
from PyQt5 import QtWidgets
from Design_ui.Abstract.class_main_design import class_main_design

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = class_main_design()
    MainWindow.show()
    sys.exit(app.exec_())

