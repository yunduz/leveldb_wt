#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Not enough arguments passed $#."
else
    echo "Running $1"
fi

python process_log.py logs/${1}.log processed_logs/${1}.txt

