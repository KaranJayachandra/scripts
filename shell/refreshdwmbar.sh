#!/bin/sh

PID=$(ps aux | grep "/dwmbar.sh" | grep "tty1" | awk '{print $2}')
echo $PID
xargs kill -9 $PID
/home/karan/wrkspc/scripts/shell/dwmbar.sh & >/dev/null
