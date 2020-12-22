#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

if which python3 > /dev/null 2>&1;
then
    #Python is installed
    python_version=`python3 --version 2>&1 | awk '{print $2}'
    `
    echo "Found python $python_version installed."
    if  [ -e "/usr/bin/ssender.py" ]; then
       echo "updating installed script .."
            
    fi
    echo "copying files ...."
    cp -r src/simplesender /usr/bin/
    cp -r src/ssender.py /usr/bin
    chmod +x /usr/bin/ssender.py
    echo "copying complete !"
    
else
    #Python is not installed
    echo "program requires python3.x"
    exit
fi
