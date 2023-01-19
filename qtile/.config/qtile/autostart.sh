#!/bin/sh
nitrogen --restore
picom --experimental-backends &
dunst &
~/.config/polybar/launch.sh 
lxsession &
flameshot &
/usr/bin/emacs --daemon &
volumeicon &
