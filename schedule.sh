#!/bin/bash

cd /home/pi/Desktop/bird-alert
python3 bird_monitor.py --led-rows=32 --led-cols=64 --led-gpio-mapping=adafruit-hat --led-brightness=50
