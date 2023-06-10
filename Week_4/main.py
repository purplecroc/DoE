import network
from time import sleep
import machine
import credentials

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.ssid, credentials.password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    return wlan


def run():
    wlan = connect()

    print(wlan.ifconfig())