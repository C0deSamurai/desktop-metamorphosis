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


def configure_from_file():
    """Takes the config.ini file, if it exists, and modifies the settings to that file"""
    if not Path.exists(Path(__file__).parent.joinpath("config.ini")):  # move along people
        return None
    else:
        config = configparser.ConfigParser()
        config.read("config.ini")
        settings = config["SETTINGS"]
        # Warning: what lies ahead is hacky as fuck. But code repetition sucks, and Python lets me!
        defaults = ["IMAGE_DIR", "NUM_GROUPS", "DEFAULT_IMAGE_FILETYPES", "DEFAULT_OWNER"]
        for i, setting in enumerate(("imagedirectory", "numsortinggroups",
                                     "imagefiletypes", "owner")):
            if setting in settings:
                globals()[defaults[i]] = settings[setting]

        globals()["IMAGE_DIR"] = Path(IMAGE_DIR)  # this would otherwise be a string
        globals()["IMAGE_FILETYPES"] = tuple(IMAGE_FILETYPES.split())  # ditto
        globals()["NUM_GROUPS"] = int(NUM_GROUPS)  # ditto


def sort(im_dir=IMAGE_DIR, im_types=IMAGE_FILETYPES, num=NUM_GROUPS, owner=DEFAULT_OWNER,
         use_gui=False):
    """Sorts the directory by brightness into subdirectories to use for metamorphosis.
    If use_gui is True, uses a graphical progress bar. Then gives the directory with the
    images to the specified user."""
    makedirs("{}/sorted-images".format(im_dir), exist_ok=True)

    for i in range(num):
        makedirs("{}/sorted-images/sorted-{}".format(im_dir, i+1), exist_ok=True)
    image_paths = [pth for pth in Path(im_dir).iterdir()
                   if pth.suffix[1:] in im_types]

    top = 255
    thresholds = [top*i/num for i in range(1, num+1)]
    # print(thresholds)
    if use_gui:
        progressbar = QtWidgets.QProgressDialog()
        progressbar.setModal(True)
        progressbar.setMinimum(0)
        progressbar.setMaximum(len(image_paths))
        progressbar.setLabelText("Classifying wallpapers...")
        progressbar.show()
    for i, pth in tqdm(enumerate(image_paths)):
        if use_gui:
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
        print("Successful!")

if __name__ == "__main__":
    sort()
