#!/bin/sh

V=$(amixer -c 1 get Master | grep -o '[0-9]*\%' | grep -o '[0-9]*')
echo $V
if [[ $1 == + ]]
then
	if [ $V -lt 100 ]
	then
		V=`expr $V + 5`
	else
		V=100
	fi
elif [[ $1 == - ]]
then
	if [ $V -gt 0 ]
	then
		V=`expr $V - 5`	
	else
		V=0
	fi
fi
echo $V
amixer -c 1 set Master $V% >/dev/null
