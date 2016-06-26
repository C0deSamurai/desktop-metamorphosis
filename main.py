"""The main logic for the application, prompting the user for a directory to store images in, the
number of groups to sort the images into by average luminosity, and how many minutes should pass in
between desktop wallpaper changes. It then adds a script to perform those actions into the user's
crontab. The script and directory it creates in ~/.desktop-metamorphosis are what is pointed to."""

from PyQt5 import QtCore, QtGui, QtWidgets
from QtWidgets import QFileDialog
from mainui import MainUIDialog
from pathlib import Path
import configparser


class MainProgram(MainUIDialog):
    """The main program"""
    def __init__(self, dialog):
        """Sets up all required event handlers"""

        MainUIDialog.__init__(self)
        self.setupUi(dialog)

        self.directory = None  # change later
        self.buttonBox.accepted.connect(self.accept)
        self.folderselect_pushButton.clicked.connect(self.select_directory)

    def no_selected_directory(self):
        """Creates a message box to inform the user that no directory has been selected."""
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText("You cannot run the program without a directory of wallpapers!")
        msgbox.exec()

    def accept(self):
        """Does some input checking and does the dirty work"""
        if self.directory is None:  # no folder was ever selected
            self.no_selected_directory()  # tell the user
            return False  # no soup for you!
        else:
            self.configure_script()
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText("Operation successful!")
            return True  # we did it!

    def select_directory(self):
        """Uses the QFileDialog to select a directory for the images."""
        im_dir = QFileDialog.getExistingDirectory(self, "Select Directory",  Path.home(),
                                                  QFileDialog.ShowDirsOnly)
        self.directory = im_dir

    def configure_script(self):
        """Adds values to a configuration file, config.ini"""
        im_filetypes = ("png", "jpg")  # yeah yeah yeah hardcoding evil blah blah blah
        num_groups = self.numGroups_spinbox.value()
        delay = self.minutes_spinBox.value()
        # add to config.ini file
        config = configparser.ConfigParser()
        config["SETTINGS"] = {"ImageDirectory": str(self.directory),
                              "NumSortingGroups": num_groups,
                              "ImageFiletypes": ' '.join(im_filetypes),
                              "ChangeDelay": delay}
        with open("config.ini", 'w') as configfile:
            config.write(configfile)
