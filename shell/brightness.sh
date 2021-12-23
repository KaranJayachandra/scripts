#!/bin/sh

T=$(cat /sys/class/backlight/intel_backlight/brightness)

if [[ $1 == + ]] 
then
	if [ $T -lt 900 ]
       	then	
		T=`expr $T + 50`
	else
		T=937
	fi
elif [[ $1 == - ]]
then
	if [ $T -gt 50 ]
       	then
		T=`expr $T - 50`
	else
		T=10
	fi
fi

echo $T | sudo tee /sys/class/backlight/intel_backlight/brightness >/dev/null

exit 0
