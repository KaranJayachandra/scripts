#!/bin/bash

while :
do
time=$(date '+%Y-%m-%d (%a) %H:%M')
battery=$(cat /sys/class/power_supply/BAT0/capacity)
volume=$(amixer -c 1 get Master | grep -o '[0-9]*%')
brightness=$(cat /sys/class/backlight/intel_backlight/brightness)
mbrightness=$(cat /sys/class/backlight/intel_backlight/max_brightness)
brightness=`expr $brightness \* 100`
brightness=`expr $brightness / $mbrightness`
xsetroot -name "V: $volume | S: $brightness% | B: $battery% | $time"
sleep 1m
done
