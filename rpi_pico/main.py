import time
import network
from rpi_pico import credentials


wlan = None

def waitNetwork():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.ssid, credentials.password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    return wlan

def run(week):
    print(f"Run week {week}")

    if week == 1:
        print("No code in week 1")
    elif week == 2.1:
        from rpi_pico.Week_2.Input_test import run
        run()
    elif week == 2.2:
        from rpi_pico.Week_2.switch_control_led import run
        run()
    elif week == 3:
        from rpi_pico.Week_3.PIR_sensor import run
        run()
    elif week == 4:
        from rpi_pico.Week_4.main import run
        run()
    elif week == 5:
        from rpi_pico.Week_5.pub import run
        waitNetwork()
        run()
    else:
        print("Unknown week")
