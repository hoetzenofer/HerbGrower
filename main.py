# main.py

import greenhouse
import json
import RPi.GPIO as GPIO
import statistics as stt

with open("meta.json", "r") as file:
    PINS = json.load(file)

with open("config.json", "r") as file:
    SETTINGS = json.load(file)["settings"]

sensors = greenhouse.Sensors(PINS["sensors"], SETTINGS["pinout"])
control = greenhouse.Control(PINS["control"], SETTINGS["pinout"])

GPIO.setmode(GPIO.BCM if SETTINGS["pinout"] == "bcm" else GPIO.BOARD)

running = True
while running:
    ...
    # code here
