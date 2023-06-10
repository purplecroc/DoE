import time
import network
import credentials


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
        from Week_2.Input_test import run
        run()
    elif week == 2.2:
        from Week_2.switch_control_led import run
        run()
    elif week == 3:
        from Week_3.PIR_sensor import run
        run()
    elif week == 4:
        from Week_4.main import run
        run()
    elif week == 5:
        from Week_5.pub import run
        waitNetwork()
        run()
    else:
        print("Unknown week")
