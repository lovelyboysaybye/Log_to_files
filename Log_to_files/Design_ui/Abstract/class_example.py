import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Design_ui.Ui_files.progressbar import Ui_Dialog

from Threaads.ProgressBarThread import ProgressBarThread
from Design_ui.Abstract.QuestionWindow import QuestionWindow

class class_example(QtWidgets.QDialog, Ui_Dialog):
    """description of class"""

    def __init__(self, parent=None):
        super(class_example, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.win = None
    

    #-----Start Main process------#

    def Start_Thread_Operations(self, path, wav_checked):
        self.calc = ProgressBarThread(path, False, self)
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()
        self.calc.finished.connect(self.calc.shit)
        self.calc.quit()


    #-----Function, for change----#
    #-----ProgressBar value-------#

    def onCountChanged(self, value):
        self.progressBar.setValue(value)


    #-----Custom close event.------#
    #-----Ask before closing-------#

    def closeEvent(self, event):
        print("value of end:{}".format(ProgressBarThread.check_if_it_end))
        if (ProgressBarThread.check_if_it_end == False):
            #self.reply = QMessageBox.question(None, 'Process launched.', "Process isn't finished, yet.\n Are you sure?",
            #                            QMessageBox.Yes, QMessageBox.No)
            #self.event = event
            #if (self.reply == QMessageBox.Yes):
            #    set_check_True()
            #    self.event.accept()
            #else:
            #    self.event.ignore()
            self.win = QuestionWindow(event)
            self.win.show()
            event.ignore()
        else:
            if(self.win != None):
                self.win.close()
            event.accept()

        

















