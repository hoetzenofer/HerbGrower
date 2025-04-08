# main.py

import greenhouse
import json
import RPi.GPIO as GPIO

with open("meta.json", "r") as file:
    PINS = json.load(file)

with open("config.json", "r") as file:
    SETTINGS = json.load(file)

sensors = greenhouse.Sensors(PINS["sensors"], SETTINGS["pinout"])
control = greenhouse.Control(PINS["control"], SETTINGS["pinout"])

GPIO.setmode(GPIO.BCM if SETTINGS["pinout"] == "bcm" else GPIO.BOARD)
GPIO.setup(PINS["sensors"]["DHT22"]["pin-bcm"], GPIO.IN)
GPIO.setup(PINS["sensors"]["moisture-sensor"]["pin-bcm"], GPIO.IN)
GPIO.setup(PINS["control"]["pump"]["pin-bcm"], GPIO.OUT)
GPIO.setup(PINS["control"]["lights"]["pin-bcm"], GPIO.OUT)

running = True
while running:
    ...
