"""The main logic for the application, prompting the user for a directory to store images in, the
number of groups to sort the images into by average luminosity, and how many minutes should pass in
between desktop wallpaper changes. It then adds a script to perform those actions into the user's
crontab. The script and directory it creates in ~/.desktop-metamorphosis are what is pointed to."""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from mainui import Ui_Dialog
from pathlib import Path
from addtocrontab import add_to_crontab
from sorter import sort
import configparser
import sys


IM_FILETYPES = ("png", "jpg")  # yeah yeah yeah hardcoding evil blah blah blah


def get_users():
    """Returns a list of all users on the OS."""
    users = []
    with open("/etc/passwd", 'r') as passwd:
        for line in passwd:
            users.append(line.split(':')[0])
    return users


class MainProgram(Ui_Dialog):
    """The main program"""
    def __init__(self, dialog):
        """Sets up all required event handlers"""

        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog

        self.buttonBox.accepted.connect(self.custom_accept)
        self.selectDirectoryButton.clicked.connect(self.select_directory)
        self.users = get_users()
        self.ownerLineEdit.setText(self.users[-1])  # most likely to be the user
        if Path.home().joinpath("Pictures").exists():  # has Pictures directory
            self.imageDirectoryLineEdit.setText(str(Path.home().joinpath("Pictures")))
        else:
            self.imageDirectoryLineEdit.setText("")  # just leave it blank
            
    def no_selected_directory(self):
        """Creates a message box to inform the user that an invalid directory has been selected."""
        msgbox = QMessageBox()
        msgbox.setText("The wallpaper directory must contain at least one .png or .jpg file!")
        msgbox.exec()

    def is_valid_path(self, p):
        """Returns True only if the folder exists and contains an image."""
        if not p.exists():
            return False
        else:
            return any([str(imagefile)[-3:] in IM_FILETYPES for imagefile in p.iterdir()])

    def custom_accept(self, just_config=False):
        """Does some input checking and does the dirty work. If just_config is True, do not add to
        crontab."""
        if not self.is_valid_path(Path(self.imageDirectoryLineEdit.text())):  # invalid folder
            self.no_selected_directory()  # tell the user
            # do not pass to Ui_Dialog.accept()
            return False
        else:
            self.configure_script()  # note that this sets the variables we'll use to call sort()
            if not Path(self.imageDirectoryLineEdit.text()).joinpath(
                    "sorted-images").exists():
                sort(use_gui=True)
            if not just_config:
                if self.crontab_configure() != 0:  # Houston, we have a problem
                    self.accept()  # quit
                    return False  # don't show msgbox

            msgbox = QMessageBox()
            msgbox.setText("Operation successful!")
            msgbox.exec()
            # quit the dialog
            self.accept()  # if this isn't working, it's because main.ui got rewritten
            return True

    def select_directory(self):
        """Uses the QFileDialog to select a directory for the images."""
        im_dir = Path(QFileDialog.getExistingDirectory(None, "Select Directory",  str(Path.home()),
                                                       QFileDialog.ShowDirsOnly))
        self.imageDirectoryLineEdit.setText(str(im_dir.resolve()))

    def configure_script(self):
        """Adds values to a configuration file, config.ini"""
        self.num_groups = self.numberGroupsSpinBox.value()
        self.delay = self.delaySpinBox.value()
        self.directory = self.imageDirectoryLineEdit.text()
        self.owner = self.ownerLineEdit.text()
        # add to config.ini file
        config = configparser.ConfigParser()
        config["SETTINGS"] = {"imagedirectory": str(self.directory),
                              "numsortinggroups": self.num_groups,
                              "imagefiletypes": ' '.join(IM_FILETYPES),
                              "changedelay": self.delay,
                              "owner": self.owner}
        with open("config.ini", 'w') as configfile:
            config.write(configfile)

    def show_error_message(self, msg):
        """Shows an error message using the given string."""
        msgbox = QMessageBox()
        msgbox.critical(dialog, "Error", msg)

    def crontab_configure(self):
        code = add_to_crontab()
        if code == 0:  # success!
            return None  # quit
        elif code == 64:  # /etc/crontab not found
            self.show_error_message("/etc/crontab not found")
        elif code == 65:  # permissions errors
            self.show_error_message("Permission denied. Are you root?")
        elif code == 1:  # we don't even know
            self.show_error_message("An unknown error occurred. Good luck!")
        return code

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    program = MainProgram(dialog)

    dialog.show()
    sys.exit(app.exec())
