import re
import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


from Design_ui.Ui_files.Design import Ui_MainWindow
from Design_ui.Abstract.class_example import class_example

class class_main_design(QtWidgets.QMainWindow, Ui_MainWindow):
    """Abstract class for MainWindow"""

    def __init__(self, parent=None):
        super(class_main_design, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ChooseFile)
        self.pushButton_2.clicked.connect(self.Make_Files)
        self.checkBox.setVisible(False)


#-----Create QDialog with-----#
#---------Progress bar.-------#
#-----Return object of Dialog-#

    def openProgBar(self):
        form = class_example()
        form.show()
        form.Start_Thread_Operations(self.path, self.wav_check)
        return form


#-----Create QFileDialog------#
#-----window for choosing-----#
#-----path to .log or .txt----#
#-------------file.-----------#
#-----Write path to lineEdit--#


    def ChooseFile(self):
        fname = QFileDialog.getOpenFileName(None, "Choose the log file", "", "Choose file (*.log *txt)")[0]
        self.lineEdit.setText(fname)


#-----Check type of file------#
#-----Get chechBox value------# 

    def CheckFileds(self):
        path = Path(self.lineEdit.text())
        typee = path.suffix
        filter = "(\.log)|(\.txt)|(\.TXT)|(\.LOG)$"
        wav_check = self.checkBox.isChecked()

        if (re.match(filter, typee) != None):
            self.path = path
            self.typee = typee
            self.wav_check = wav_check
            return True
        else:
            QMessageBox.warning(
                None, "Oops!",
                "File should be .log or .txt type.\n"
                "Please, choose file with correct type!"
            )
            return False


#-----Make files functio------#

    def Make_Files(self):
        if (self.CheckFileds() == True):
            progwin = self.openProgBar()














