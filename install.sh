#!/bin/bash

sudo apt install --upgrade python3
sudo -H pip3 install --upgrade pyqt5
mkdir ~/.desktop-metamorphosis
cp -r * ~/.desktop-metamorphosis
cd * ~/.desktop-metamorphosis
python3 main.py
