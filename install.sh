#!/bin/bash

sudo apt install --upgrade python3
sudo apt install python3-pip
sudo -H pip3 install --upgrade pyqt5
pip3 install tqdm
rm -r ~/.desktop-metamorphosis
mkdir ~/.desktop-metamorphosis
cp -r * ~/.desktop-metamorphosis
python3 ~/main.py
