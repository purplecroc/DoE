from machine import Pin
from time import sleep

pin_led = Pin(16, mode=Pin.OUT)
pin_input = Pin(18, mode=Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if pin_input.high():
        pin_led.on()
    else:
        pin_led.off()