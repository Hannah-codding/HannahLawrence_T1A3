#!/bin/bash

# check whether python is installed

# check when venv exists or not

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py