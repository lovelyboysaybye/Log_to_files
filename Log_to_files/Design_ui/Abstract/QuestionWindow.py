
from PyQt5.QtWidgets import QMessageBox

from SepareteFIle import set_check_True

class QuestionWindow(QMessageBox):

    def __init__(self, event, parent = None):
        super(QuestionWindow, self).__init__(parent)
        self.event = event

        self.setWindowTitle("Process launched")
        self.setText("Process isn't finished, yet.\n Are you sure?")
        self.setIcon(QMessageBox.Question)
        self.Btn1 = self.addButton("Yes", QMessageBox.ActionRole)
        self.Btn2 = self.addButton("No", QMessageBox.RejectRole)
        self.Btn1.clicked.connect(self.Answer_Yes)
        self.Btn2.clicked.connect(self.Answer_No)
        
    def Answer_Yes(self):
        set_check_True()
        self.event.accept()

    def Answer_No(self):
        self.close()