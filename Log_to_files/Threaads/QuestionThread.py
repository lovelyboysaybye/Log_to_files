
from Design_ui.Abstract.QuestionWindow import QuestionWindow
from Threaads.ProgressBarThread import ProgressBarThread

def Start_Thread(obj, event):
    if (ProgressBarThread.check_if_it_end == False):
        obj.win = QuestionWindow(event)
        obj.win.show()
        event.ignore()
    else:
        if(obj.win != None):
            obj.win.close()
        event.accept()