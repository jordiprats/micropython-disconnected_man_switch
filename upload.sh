#!/bin/bash

pkill screen

for file in main.py config.py uping.py;
do
    echo "refreshing $file"
    ampy --port /dev/ttyUSB0 rm $file
    ampy --port /dev/ttyUSB0 put $file
done

