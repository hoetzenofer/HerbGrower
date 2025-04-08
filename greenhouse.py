# greenhouse.py

import time as t
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import luma.core.interface.serial as LUMA

class Sensors:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout
        self.data = {}

    def setup(self) -> None:
        for name, data in self.meta:
            GPIO.setup(data[f"pin-{self.pinout}"], GPIO.IN)

    def update(self) -> None:
        humidity, temperature = DHT.read_retry(DHT.DHT22, self.meta["DHT22"][f"pin-{self.pinout}"])
        self.data["temperature"] = temperature
        self.data["humidity"] = humidity
        self.data["moisture"] = GPIO.input(self.meta["moisture-sensor"][f"pin-{self.pinout}"]) == 0

class Control:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout
    
    def setup(self) -> None:
        for name, data in self.meta:
            GPIO.setup(data[f"pin-{self.pinout}"], GPIO.OUT)
        self.fan_pwm = GPIO.PWM(self.meta["fan"][f"pin-{self.pinout}"])
        self.fan_pwm.start(0)
        
    def irrigate(self, time: int | float) -> None:
        GPIO.output(self.meta["pump"][f"pin-{self.pinout}"], GPIO.HIGH)
        t.sleep(time)
        GPIO.output(self.meta["pump"][f"pin-{self.pinout}"], GPIO.LOW)

    def lights(self, on: bool) -> None:
        GPIO.output(self.meta["lights"][f"pin-{self.pinout}"], GPIO.HIGH if on else GPIO.LOW)

    def fan(self, speed: float) -> None:
        self.fan_pwm.ChangeDutyCycle(speed)

class Display:
    def __init__(self, meta: dict):
        self.meta = meta

    def setup(self):
        self.serial = LUMA.i2c(port=1, address=int(self.meta["address"]))
        self.device = ...

    def place_img(self, img: str):
        pass

    def place_text(self, text: str):
        pass
