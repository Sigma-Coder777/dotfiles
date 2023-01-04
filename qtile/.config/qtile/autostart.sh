#!/bin/sh
nitrogen --restore
picom --experimental-backends &
dunst &
~/.config/polybar/launch.sh 
lxsession &
flameshot &
emacs --daemon &
killall redshift 
redshift   
