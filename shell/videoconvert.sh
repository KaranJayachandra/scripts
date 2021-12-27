#!/bin/sh

FILES=$(ls -al $1 | grep .$2 | awk '{print $9}')
NUMBER=$(echo $FILES | wc -w )
echo $NUMBER files found. Shall I convert them? [Y/n] 
read USERINPUT
if [[ $USERINPUT == 'Y' ]]
then 
	mkdir $1OUTPUT	
	for FILE in $FILES;
	do
		INPUT=$1/$FILE	
		OUTPUT=$1OUTPUT/${FILE/.$2/.$3}
		echo Converting $INPUT	
		ffmpeg -i $INPUT $OUTPUT  
	done
fi
echo Output Written to $1OUTPUT
