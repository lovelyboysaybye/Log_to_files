import subprocess
import time
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QDialog

import SepareteFIle as SF

from Design_ui.Abstract.QuestionWindow import QuestionWindow

class ProgressBarThread(QThread):
    """
    Runs a counter thread.
    """
    check_if_it_end = False
    countChanged = pyqtSignal(int)

    def __init__(self, path, wav_checked, progwin):
        super(ProgressBarThread, self).__init__()
        self.path = path
        self.wav_checked = wav_checked
        self.progwin = progwin

    def run(self):
        count = SF.count_value
        thread1 = Thread(target = SF.SplitFiles, name="fuck", daemon = True, args=(self.path, "txt",  str(time.time())),)
        thread1.start()

        while (count != -1):
            count = SF.count_value
            self.countChanged.emit(count)
            check = SF.get_check()
            if (check == False or check == True):
                break
            
        self.countChanged.emit(0)
        thread1._is_stopped = True
        del thread1
        SF.clear_count()

    def __del__(self):
        self.wait()


#-----After finishing---------#
#-----Make files functio------#
#-----Close QDialog ProgBar---#
#-----------------------------#
#-----Call information about--#
#-----creating process results#

    def shit(self):
        print(ProgressBarThread.check_if_it_end)

        ProgressBarThread.check_if_it_end = True
        self.progwin.close()
        ProgressBarThread.check_if_it_end = False

        self.Congratulation()


#-----Information about-------#
#-----Process results.--------#

    def Congratulation(self):
        folder = SF.get_folder()
        check = SF.get_check()

        if (check == False):
            QMessageBox.warning(
                None, "Oops!",
                "Something went wrong!\n"
                "Maybe your file has not compability formating?"
            )
        elif (check == True):
            subprocess.Popen("explorer \"{}\"".format(folder))
            QMessageBox.information(None, "Caution!",
                                    "Operation was canceled.\nBut you can check, what had been done!"
            )
        else:
            subprocess.Popen("explorer \"{}\"".format(folder))
            QMessageBox.information(
                None, "Nice!",
                "Done!\n"
            )
        SF.set_check_None()






