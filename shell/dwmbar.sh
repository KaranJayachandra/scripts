#!/bin/bash

while :
do
time=$(date '+%Y-%m-%d (%a) %H:%M')
battery=$(cat /sys/class/power_supply/BAT0/capacity)
xsetroot -name "B: $battery% | $time"
sleep 1m
done
