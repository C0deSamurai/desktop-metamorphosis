"""This file adds a command into the crontab file pointing to the morph.sh file which will change
the desktop background."""

from configparser import ConfigParser
from pathlib import Path


def get_owner():
    config = ConfigParser()
    config.read("config.ini")
    return config["SETTINGS"]["owner"]


def add_to_crontab():
    """Adds the proper entry to /etc/crontab. Returns 64 for /etc/crontab not existing, 65 for
    permission errors, 1 for anything else, and 0 for success. """
    CRONTAB_PATH = "/etc/crontab"  # surely this won't change, right?
    if not Path(CRONTAB_PATH).exists():  # well, accidents happen
        return 64
    
    script_dir = Path(__file__).parent
    try:  # often there might be permission errors
        with open("/etc/crontab", 'a') as crontab:
            crontab.write("\n* * * * * {} bash {} >> {}\n".format(
                get_owner(), script_dir.joinpath("morph.sh"),
                script_dir.joinpath("metamorphosislog")))
    except PermissionError:
        return 65

    except:  # blanket for anything else
        return 1

    return 0  # last man standing
