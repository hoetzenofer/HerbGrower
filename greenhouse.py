# greenhouse.py

import time as t
import RPi.GPIO as GPIO
import board
import adafruit_dht as ADHT

gpio_to_board = {
    # starting at 2 since 0 and 1 may be reserved for i2c or dont even exist in board module
    2: board.D2,
    3: board.D3,
    4: board.D4,
    5: board.D5,
    6: board.D6,
    7: board.D7,
    8: board.D8,
    9: board.D9,
    10: board.D10,
    11: board.D11,
    12: board.D12,
    13: board.D13,
    14: board.D14,
    15: board.D15,
    16: board.D16,
    17: board.D17,
    18: board.D18,
    19: board.D19,
    20: board.D20,
    21: board.D21,
    22: board.D22,
    23: board.D23,
    24: board.D24,
    25: board.D25,
    26: board.D26,
    27: board.D27
    # only to 27 (only 27 gpio pins)
}

class Sensors:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout
        self.data = {}
        
        # setup
        self.dht22 = ADHT.DHT22(gpio_to_board[self.meta["DHT22"]["pin-bcm"]])
        GPIO.setup(self.meta["moisture-sensor"][f"pin-{self.pinout}"], GPIO.IN)

    def update(self) -> None:
        try:
            temperature, humidity = self.dht22.temperature, self.dht22.humidity
            self.data["temperature"] = temperature
            self.data["humidity"] = humidity
        except Exception as e:
            self.dht22.exit()
            print(f"[DHT22] ERROR: {e.args[0]}")
        
        try:
            self.data["moisture"] = GPIO.input(self.meta["moisture-sensor"][f"pin-{self.pinout}"]) == 0
        except Exception as e:
            print(f"[SM-SENSOR] ERROR: {e.args[0]}")

class Control:
    def __init__(self, meta: dict, pinout: str):
        self.meta = meta
        self.pinout = pinout
        
        # setup
        GPIO.setup(self.meta["pump"]["pin-{self.pinout}"], GPIO.OUT)

    def irrigate(self, time: int | float) -> None:
        GPIO.output(self.meta["pump"][f"pin-{self.pinout}"], GPIO.HIGH)
        t.sleep(time)
        GPIO.output(self.meta["pump"][f"pin-{self.pinout}"], GPIO.LOW)

    def lights(self, on: bool) -> None:
        GPIO.output(self.meta["lights"][f"pin-{self.pinout}"], GPIO.HIGH if on else GPIO.LOW)

