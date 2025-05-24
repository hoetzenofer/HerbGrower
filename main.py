# main.py

from greenhouse import Sensors, Control
from debugger import Debug
import json
import RPi.GPIO as GPIO
import time as t

with open("meta.json", "r") as file:
    PINS = json.load(file)

with open("config.json", "r") as file:
    SETTINGS = json.load(file)["settings"]

GPIO.setmode(GPIO.BCM if SETTINGS["pinout"] == "bcm" else GPIO.BOARD)

sensors = Sensors(PINS["sensors"], SETTINGS["pinout"])
control = Control(PINS["control"], SETTINGS["pinout"])
debug = Debug("debuglog.txt", True)

running = True
while running:
    try:
        sensors.update()
        debug.log(sensors.data)
        control.irrigate(1)
        t.sleep(2)

    except KeyboardInterrupt:
        running = False

    except Exception as e:
        debug.log(e)
        running = False

GPIO.cleanup()
