#!/bin/bash
# Python environment setup
python3 -m venv .venv
# shellcheck disable=SC1091
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

ulimit -n 8096
cd src || exit
python main.py --skip-plot
# python main.py --train-evaluator
sudo poweroff
