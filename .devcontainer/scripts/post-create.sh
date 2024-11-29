#!/bin/bash

cd "$(dirname "$0")"

sudo apt update && sudo apt upgrade -y
sudo apt -y install uvicorn

pip install --upgrade pip

cd ../..

pip3 install -r requirements.txt