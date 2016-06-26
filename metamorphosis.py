"""This file checks what time of day it is and selects an appropriate background wallpaper."""

import configparser
import subprocess
import datetime
from random import choice
from pathlib import Path
from sorter import sort


SWITCH_DELAY = 1  # in minutes
DEFAULT_NUM_GROUPS = 6
DEFAULT_IMAGE_DIR = Path(__file__).parent.joinpath("test")
DEFAULT_IMAGE_FILETYPES = ("png", "jpg")


def configure_from_file():
    """Takes the config.ini file, if it exists, and modifies the settings to that file"""
    if not Path.exists(Path(__file__).parent.joinpath("config.ini")):  # move along people
        return None
    else:
        config = configparser.ConfigParser()
        config.read("config.ini")
        settings = config["SETTINGS"]
        # Warning: what lies ahead is hacky as fuck. But code repetition sucks, and Python lets me!
        defaults = ["DEFAULT_IMAGE_DIR", "DEFAULT_NUM_GROUPS",
                    "DEFAULT_IMAGE_FILETYPES", "SWITCH_DELAY"]
        for i, setting in enumerate(("ImageDirectory", "NumSortingGroups",
                                     "ImageFiletypes", "ChangeDelay")):
            if setting in settings:
                globals()[defaults[i]] = settings[setting]

        globals()["DEFAULT_IMAGE_DIR"] = Path(DEFAULT_IMAGE_DIR)  # this would otherwise be a string
        globals()["SWITCH_DELAY"] = int(SWITCH_DELAY)  # this would otherwise be a string
        globals()["DEFAULT_IMAGE_FILETYPES"] = tuple(DEFAULT_IMAGE_FILETYPES.split())  # ditto
        globals()["DEFAULT_NUM_GROUPS"] = int(DEFAULT_NUM_GROUPS)  # ditto


def get_brightness(hour, num_groups):
    """Gets a fudged value between 1 and num_groups for the brightness outside right now."""
    return (12 - abs(hour-12)) * num_groups / 12  # told you it was fudged


def main(im_dir, im_filetypes, num_sorting_groups, delay=SWITCH_DELAY):
    if not Path(("{}/sorted-images/sorted.txt".format(im_dir))).exists():
        sort(im_dir, im_filetypes, num_sorting_groups)

    now = datetime.datetime.now()
    if now.minute % delay == 0:  # time to switch
        # select a random image from the correct directory
        brightness = int(get_brightness(now.hour) + 1)
        # print(brightness)

        # if 0 or 1 files in the directory, choose randomly from whole directory
        if len(list(Path("{}/sorted-images/sorted-{}".format(im_dir, brightness)).iterdir())) <= 1:
            new_background = choice(list(Path(im_dir).iterdir()))

        # get a random file from that directory
        new_background = choice(list(Path("{}/sorted-images/sorted-{}".format(im_dir,
                                                                          brightness)).iterdir()))

        print(new_background)

        subprocess.call("gsettings set org.gnome.desktop.background picture-uri {}".format(
            new_background.resolve().as_uri()), shell=True)
    print(now.hour, now.minute, now.second)


if __name__ == "__main__":
    main()
