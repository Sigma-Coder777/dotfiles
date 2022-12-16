#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar leftbar 2>&1 | tee -a /tmp/polybar1.log & disown
polybar middlebar 2>&1 | tee -a /tmp/polybar1.log & disown
polybar rightbar 2>&1 | tee -a /tmp/polybar1.log & disown

echo "Bars launched..."
