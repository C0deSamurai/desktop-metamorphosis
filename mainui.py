# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 228)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 421, 162))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.directoryOfWallpapersLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.directoryOfWallpapersLabel.setObjectName("directoryOfWallpapersLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.directoryOfWallpapersLabel)
        self.imageDirectoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.imageDirectoryLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.imageDirectoryLineEdit.setObjectName("imageDirectoryLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.imageDirectoryLineEdit)
        self.selectDirectoryButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.selectDirectoryButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.selectDirectoryButton.setObjectName("selectDirectoryButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.selectDirectoryButton)
        self.numberOfSortedGroupsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.numberOfSortedGroupsLabel.setObjectName("numberOfSortedGroupsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numberOfSortedGroupsLabel)
        self.numberGroupsSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.numberGroupsSpinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.numberGroupsSpinBox.setMinimum(1)
        self.numberGroupsSpinBox.setMaximum(12)
        self.numberGroupsSpinBox.setProperty("value", 6)
        self.numberGroupsSpinBox.setObjectName("numberGroupsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numberGroupsSpinBox)
        self.timeBetweenWallpaperSwitchesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timeBetweenWallpaperSwitchesLabel.setObjectName("timeBetweenWallpaperSwitchesLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timeBetweenWallpaperSwitchesLabel)
        self.delaySpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.delaySpinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.delaySpinBox.setMinimum(1)
        self.delaySpinBox.setMaximum(59)
        self.delaySpinBox.setSingleStep(1)
        self.delaySpinBox.setProperty("value", 10)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.delaySpinBox)
        self.userToOwnSortedDirectoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.userToOwnSortedDirectoryLabel.setObjectName("userToOwnSortedDirectoryLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.userToOwnSortedDirectoryLabel)
        self.ownerLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ownerLineEdit.setObjectName("ownerLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ownerLineEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.directoryOfWallpapersLabel.setText(_translate("Dialog", "Directory of wallpapers"))
        self.imageDirectoryLineEdit.setText(_translate("Dialog", "~/Pictures"))
        self.selectDirectoryButton.setText(_translate("Dialog", "Browse..."))
        self.numberOfSortedGroupsLabel.setText(_translate("Dialog", "Number of sorted groups"))
        self.timeBetweenWallpaperSwitchesLabel.setText(_translate("Dialog", "Time between wallpaper switches"))
        self.userToOwnSortedDirectoryLabel.setText(_translate("Dialog", "User to own sorted directory"))

    def accept(self):
        self.dialog.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

