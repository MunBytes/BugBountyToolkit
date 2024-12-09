#!/bin/bash


BBT_SCRIPT="BBT.py"


if [ "$(id -u)" -ne 0 ]; then
    echo "[ERROR] This script must be run as root. Please run with 'sudo' or as the root user."
    exit 1
fi



echo "[INFO] Checking if Python is installed..."
if ! command -v python3 &> /dev/null; then
    echo "[INFO] Python is not installed. Installing Python..."
        apt update
        apt install -y
else
    echo "[INFO] Python is already installed."
fi




if [ ! -f "$BBT_SCRIPT" ]; then
    echo "[ERROR] BBT script '$BBT_SCRIPT' not found!"
    exit 1
fi


echo "[INFO] Running the BBT script: $BBT_SCRIPT..."
python3 "$BBT_SCRIPT"

