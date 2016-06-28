#!/bin/bash

apt install --upgrade python3
apt install python3-pip
pip3 install --upgrade pyqt5
pip3 install tqdm
rm -r ~/.desktop-metamorphosis
mkdir ~/.desktop-metamorphosis
cp -r * ~/.desktop-metamorphosis
python3 ~/.desktop-metamorphosis/main.py
