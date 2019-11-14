#!/bin/sh

clear
current=$PWD

echo "Your current directory is $current"

if [ $current != $HOME ]; then
       echo "You are not in the home directory"
fi

echo "But let's continue"
echo " "

loop=True

while [ $loop != False ]
do
	read -p "Enter a filename: " filename
#	echo $filename
	if [ $filename = "quit" ]; then
		echo "BYEEEEE"
		exit 0
	else
		file=$(find . -name $filename)
		echo "File is $file"
		if [ -z $file ]; then
			echo "The File you are looking for can't be found!!!"
		else
			loop=False
		fi
	fi
done

echo " "
echo "Congrats. The file exist!!"
echo "Time for linking"
echo " "

echo "The symbolic link will be stored on the Desktop"
abspath="$current/$filename"
output="$HOME/Desktop/$filename"
#echo $output

ln -s $abspath $output
echo "Successfully"
echo " "

echo "The symbolic link will be stored at this location: $output"

bad="$HOME/Desktop"
symcount=$(ls -la -1 $bad | grep ^l | wc -l)
echo "There are $symcount on the Desktop"
echo " "


echo "Listing symbolic link and target"
symfind=$(find $bad -type l)
ind=1
for path in $symfind
do
    echo "$ind: $path"
    let "ind=ind+1"
done
echo " "

echo "Listing the target path"
symtarget=$(readlink $symfind)
ind=1
for path in $symtarget
do
   echo "$ind: $path"
   let "ind=ind+1"
done
