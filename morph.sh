#!/bin/bash

DISPLAY=:0
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

sleep 3
python3 /home/nicholas/programs/desktop-metamorphosis/metamorphosis.py
