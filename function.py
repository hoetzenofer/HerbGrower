# function.py

import Adafruit_DHT as DHT

def avg(iterable: list[int] | tuple[int]) -> float:
    counter = 0
    val = 0

    for num in iterable:
        val += num
        counter += 1
    return val / counter

def sleep_ups(num: int | float) -> None:
    return 1 / num
