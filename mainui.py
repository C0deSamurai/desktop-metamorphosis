# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class MainUIDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 140)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 100, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel |
                                          QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.numGroups_spinbox = QtWidgets.QSpinBox(Dialog)
        self.numGroups_spinbox.setGeometry(QtCore.QRect(301, 40, 77, 31))
        self.numGroups_spinbox.setMinimum(1)
        self.numGroups_spinbox.setMaximum(15)
        self.numGroups_spinbox.setProperty("value", 6)
        self.numGroups_spinbox.setObjectName("numGroups_spinbox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(63, 40, 242, 16))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.folderselect_pushButton = QtWidgets.QPushButton(Dialog)
        self.folderselect_pushButton.setGeometry(QtCore.QRect(301, 10, 77, 31))
        self.folderselect_pushButton.setObjectName("folderselect_pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(132, 10, 165, 16))
        self.label_2.setObjectName("label_2")
        self.minutes_spinBox = QtWidgets.QSpinBox(Dialog)
        self.minutes_spinBox.setGeometry(QtCore.QRect(301, 70, 77, 31))
        self.minutes_spinBox.setMinimum(1)
        self.minutes_spinBox.setMaximum(60)
        self.minutes_spinBox.setProperty("value", 5)
        self.minutes_spinBox.setObjectName("minutes_spinBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 276, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "Number of groups to split images into"))
        self.folderselect_pushButton.setText(_translate("Dialog", "Select"))
        self.label_2.setText(_translate("Dialog",
                                        "Directory of images to use"))
        self.label_3.setText(_translate(
            "Dialog", "Time between wallpaper switches in minutes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainUIDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
