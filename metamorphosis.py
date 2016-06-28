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


def get_settings_from_config():
    """Gets the settings from config.ini and returns a list:
    [imagedirectory, imagefiletypes, numsortinggroups, changedelay]"""
    config = configparser.ConfigParser()
    config.read(str(Path(__file__).parent.joinpath("config.ini").resolve()))
    print(config.sections())
    settings = config["SETTINGS"]
    settingslist = []
    for key in "imagedirectory imagefiletypes numsortinggroups changedelay".split():
        settingslist.append(settings[key])
    settingslist[0] = Path(settingslist[0])  # make a Path not a string
    settingslist[2] = int(settingslist[2])  # make an int not a string
    settingslist[3] = int(settingslist[3])  # ditto
    return settingslist


def get_brightness(hour, num_groups=DEFAULT_NUM_GROUPS):
    """Gets a fudged value between 1 and num_groups for the brightness outside right now."""
    return (12 - abs(hour-12)) * num_groups / 12  # told you it was fudged


def main(im_dir=DEFAULT_IMAGE_DIR, im_filetypes=DEFAULT_IMAGE_FILETYPES,
         num_sorting_groups=DEFAULT_NUM_GROUPS, delay=SWITCH_DELAY, config_from_file=True):
    if config_from_file:
        im_dir, im_filetypes, num_sorting_groups, delay = get_settings_from_config()

    if not Path(("{}/sorted-images/.sorted".format(im_dir))).exists():
        sort(im_dir, im_filetypes, num_sorting_groups)

    now = datetime.datetime.now()
    if now.minute % delay == 0:  # time to switch
        # select a random image from the correct directory
        brightness = int(get_brightness(now.hour, num_sorting_groups) + 1)
        # print(brightness)

        # if 0 or 1 files in the directory, choose randomly from whole directory
        if len(list(Path("{}/sorted-images/sorted-{}".format(im_dir, brightness)).iterdir())) <= 1:
            new_background = choice(list(Path(im_dir).iterdir()))

        # get a random file from that directory
        new_background = choice(list(Path("{}/sorted-images/sorted-{}".format(
            im_dir, brightness)).iterdir()))

        # print(new_background)

        subprocess.call("gsettings set org.gnome.desktop.background picture-uri {}".format(
            new_background.resolve().as_uri()), shell=True)
    print(now.hour, now.minute, now.second)


if __name__ == "__main__":  # what happens next is a shocker!
    main()
