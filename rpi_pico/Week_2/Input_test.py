from machine import Pin
from time import sleep

def run():
    pin_led = Pin(16, mode=Pin.OUT)

    while True:
        pin_led.toggle()
        sleep(1)