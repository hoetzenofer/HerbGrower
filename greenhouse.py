# greenhouse.py

import time as t
import RPi.GPIO as GPIO
import board
import adafruit_dht as ADHT

class Sensors:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout
        self.data = {}
        
        self.dht22 = ADHT.DHT22(board.D4)
        GPIO.setup(self.meta["moisture-sensor"][f"pin-{self.pinout}"], GPIO.IN)

    def update(self) -> None:
        try:
            temperature, humidity = self.dht22.temperature, self.dht22.humidity
            self.data["temperature"] = temperature
            self.data["humidity"] = humidity
        except RuntimeError as error:
            print(error.args[0])
            t.sleep(2.0)
        except Exception as error:
            self.dht22.exit()
            raise error

        self.data["moisture"] = GPIO.input(self.meta["moisture-sensor"][f"pin-{self.pinout}"]) == 0

class Control:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout

    def setup(self) -> None:
        for name, data in self.meta.items():
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

