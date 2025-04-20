# main.py

import greenhouse
import json
import RPi.GPIO as GPIO
import statistics as stt
import time as t

with open("meta.json", "r") as file:
    PINS = json.load(file)

with open("config.json", "r") as file:
    SETTINGS = json.load(file)["settings"]

GPIO.setmode(GPIO.BCM if SETTINGS["pinout"] == "bcm" else GPIO.BOARD)

sensors = greenhouse.Sensors(PINS["sensors"], SETTINGS["pinout"])
control = greenhouse.Control(PINS["control"], SETTINGS["pinout"])

running = True
while running:
    sensors.update()
    print(sensors.data)
    control.irrigate(1)
    t.sleep(2)

