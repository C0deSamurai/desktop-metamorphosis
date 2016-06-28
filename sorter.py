from PIL import Image
from averagecolor import luminance
from os import makedirs
from pathlib import Path
from PyQt5 import QtWidgets
import subprocess
import configparser
from tqdm import tqdm


IMAGE_DIR = Path.cwd().joinpath("test")
IMAGE_FILETYPES = ("png", "jpg")
NUM_GROUPS = 2
DEFAULT_OWNER = "root"


def get_settings_from_config():
    """Gets settings from the config.ini file and returns a list of settings:
    [imagedirectory, imagefiletypes, numsortinggroups, owner]"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    settings = config["SETTINGS"]
    configlist = []
    for key in ["imagedirectory", "imagefiletypes", "numsortinggroups", "owner"]:
        configlist.append(settings[key])
    configlist[0] = Path(configlist[0])  # make a Path not a string
    configlist[2] = int(configlist[2])  # make an integer not a string
    return configlist


def sort(im_dir=IMAGE_DIR, im_types=IMAGE_FILETYPES, num=NUM_GROUPS, owner=DEFAULT_OWNER,
         use_gui=False, configure_from_file=True):
    """Sorts the directory by brightness into subdirectories to use for metamorphosis.
    If use_gui is True, uses a graphical progress bar. Then gives the directory with the
    images to the specified user.

    If configure_from_file is True, ignores the previous arguments (except use_gui and q_app) and
    uses config.ini.
    
    q_app is the parent QApplication, if use_gui is True.
    """
    if configure_from_file:
        im_dir, im_types, num, owner = get_settings_from_config()
    #print(im_dir, im_types, num, owner, use_gui)
    makedirs("{}/sorted-images".format(im_dir), exist_ok=True)

    for i in range(num):
        makedirs("{}/sorted-images/sorted-{}".format(im_dir, i+1), exist_ok=True)
    image_paths = [pth for pth in Path(im_dir).iterdir() if pth.suffix[1:] in im_types and
                   len(pth.suffix) == 4]  # adding the last condition fixes it, don't know why

    top = 255
    thresholds = [top*i/num for i in range(1, num+1)]
    # print(thresholds)
    if use_gui:
        progressbar = QtWidgets.QProgressDialog()
        progressbar.setModal(True)
        progressbar.setMinimum(0)
        progressbar.setMaximum(len(image_paths))
        progressbar.setMinimumDuration(0)
        progressbar.setLabelText("Classifying wallpapers...")
    for i, pth in tqdm(enumerate(image_paths)):
        # print(pth.suffix, pth.suffix[1:], pth)
        if use_gui:
            progressbar.show()
            progressbar.setValue(i)
            if progressbar.wasCanceled():
                # clean up by deleting sorted-images
                subprocess.call("rm -r {}/sorted-images".format(str(im_dir.resolve())), shell=True)
                break
        im = Image.open(pth)
        im = im.convert("RGB")
        average = luminance(im)
        # print(average)
        # test for which "bucket" to throw the image in
        for i, threshold in enumerate(thresholds):
            diff = thresholds[1] - thresholds[0]
            if average <= threshold and (average+diff) >= threshold:
                im.save("{}/sorted-images/sorted-{}/{}".format(im_dir, i+1, pth.name))
                continue
    if use_gui:
        progressbar.setValue(len(image_paths))

    if not progressbar.wasCanceled():
        with open("{}/sorted-images/.sorted".format(im_dir), mode="w") as file:
            file.write("These files are sorted by luminosity.")
        subprocess.call("chown -R {} {}/sorted-images".format(owner, im_dir), shell=True)
        print(num)
        QtWidgets.QMessageBox.information(None, "Message", "Successful!")
