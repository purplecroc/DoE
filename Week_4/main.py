import network
from time import sleep
import machine
#import credentials

ssid = '18mlf'
password = 'eieioitsofftoworkwego'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    return wlan


wlan = connect()

print(wlan.ifconfig())