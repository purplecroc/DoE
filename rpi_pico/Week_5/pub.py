# pub.py
import time
import network
from rpi_pico.Week_4 import credentials
from umqtt.simple import MQTTClient

server="test.mosquitto.org"
ClientID = f'raspberry-pub-{time.time_ns()}'
user = "emqx"
password = "public"
topic = "raspberry/mqtt"
msg = b'{"msg":"hello"}'

def connect_wifi():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.ssid, credentials.password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    return wlan

def connect_mqtt():
    print('Connected to MQTT Broker "%s"' % (server))
    client = MQTTClient(ClientID, server, 1883, user, password)
    client.connect()
    return client

def reconnect_mqtt(client):
    print('Failed to connect to MQTT broker, Reconnecting...' % (server))
    time.sleep(5)
    client.reconnect()


def run():
    wifi = connect_wifi()
    
    try:
        client = connect_mqtt()
    except OSError as e:
        reconnect_mqtt(client)

    while True:
        print('send message %s on topic %s' % (msg, topic))
        client.publish(topic, msg, qos=0)
        time.sleep(1)