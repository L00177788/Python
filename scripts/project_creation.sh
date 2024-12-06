#!/bin/bash

clear
echo "**********************************************"
echo This script will create a project directory
echo "**********************************************"
echo "*** press [ctrl][c] to exit or [return] to continue ***"
read
echo "Enter the name of the project, then press [return]"
read NAME
echo "Creating directory" $NAME

if [ -d $NAME ]; then
  echo "Directory exists" $NAME
  cd $NAME
else
  echo "Creating directory" $NAME
  mkdir $NAME
  cd $NAME
fi

# Using -p to create directories and subdirectories automatically
mkdir -p Documentation/ReadMeDocLinks
mkdir Documentation/References
mkdir -p Source/modules
mkdir Tests
mkdir Examples

ls -l
# Ommiting this because I don't want to go back home
#cd ~ 

echo "**********************************************"
echo "Finished creating project $NAME"
echo "**********************************************"