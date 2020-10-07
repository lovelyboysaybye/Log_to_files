# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 67)
        self.gridLayoutWidget = PyQt5.QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(PyQt5.QtCore.QRect(10, 10, 381, 52))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = PyQt5.QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = PyQt5.QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 2)
        spacerItem = PyQt5.QtWidgets.QSpacerItem(40, 20, PyQt5.QtWidgets.QSizePolicy.Expanding, PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton = PyQt5.QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.retranslateUi(Dialog)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))

    #app = PyQt5.QtWidgets.QApplication(sys.argv)
    #Dialog = PyQt5.QtWidgets.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    #Dialog.show()
    #sys.exit(app.exec_())




