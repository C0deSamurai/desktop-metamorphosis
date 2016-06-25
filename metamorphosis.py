"""This file checks what time of day it is and selects an appropriate background wallpaper."""

import subprocess
import datetime
from random import choice
from pathlib import Path
from sorter import sort


SWITCH_DELAY = 1  # in minutes
NUM_GROUPS = 6
IMAGE_DIR = Path(__file__).parent.joinpath("test")
IMAGE_FILETYPES = ("png", "jpg")
if not Path(("{}/sorted-images/sorted.txt".format(IMAGE_DIR))).exists():
    sort(IMAGE_DIR, IMAGE_FILETYPES, NUM_GROUPS)


def get_brightness(hour):
    """Gets a fudged value between 1 and NUM_GROUPS for the brightness outside right now."""
    return (12 - abs(hour-12)) * NUM_GROUPS / 12  # told you it was fudged

now = datetime.datetime.now()
if now.minute % SWITCH_DELAY == 0:  # time to switch
    # select a random image from the correct directory
    brightness = int(get_brightness(now.hour) + 1)
    # print(brightness)

    # if 0 or 1 files in the directory, choose randomly from whole directory
    if len(list(Path("{}/sorted-images/sorted-{}".format(IMAGE_DIR, brightness)).iterdir())) <= 1:
        new_background = choice(list(Path(IMAGE_DIR).iterdir()))

    # get a random file from that directory
    new_background = choice(list(Path("{}/sorted-images/sorted-{}".format(IMAGE_DIR,
                                                                          brightness)).iterdir()))

    print(new_background)

    subprocess.call("gsettings set org.gnome.desktop.background picture-uri {}".format(
        new_background.resolve().as_uri()), shell=True)
print(now.hour, now.minute, now.second)
