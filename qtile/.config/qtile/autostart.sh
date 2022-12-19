#!/bin/sh
nitrogen --restore
picom --experimental-backends &
dunst &
lxsession &
redshift &
~/.config/polybar/launch.sh
