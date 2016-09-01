#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Not enough arguments passed $#."
else
    echo "Running $1"
fi

echo python process_log_2.py logs/${1}.log processed_logs/${1}.txt
python process_log_2.py logs/${1}.log processed_logs/${1}.txt

