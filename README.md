# desktop-metamorphosis v0.1
A program that changes your desktop backgrounds randomly while adjusting the overall luminosity of the pictures to the time of day.

**WARNING:**
This is v0.1. This is barely cobbled together, and may break something or be very bad. Be warned! It *should* work, but I make no guarantees.

## Requirements ##
PyQt5 must be installed. This happens through the install script, so don't worry about this if you don't have it.
Python 3.5 must also be installed: `sudo apt install --upgrade python3`. This will happen through the install script as well, but you might want to install it manually.
tqdm is also used, which (surprise!) is installed automagically. You don't have to worry about much.


## How to Use ##
Download or clone the repository anywhere on your system, `cd` to the directory you installed it in, and run `sudo bash install.sh` to install it. All this does is install PyQt5 if it does not currently exist on your system, copy this to ~/.desktop-metamorphosis and runs the main python file. 
