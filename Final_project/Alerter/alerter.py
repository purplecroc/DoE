from machine import Pin
import time
from umqtt.simple import MQTTClient

server="test.mosquitto.org"
ClientID = f'raspberry-sub-{time.time_ns()}'
user = "emqx"
password = "public"
topic="doe_project/detector"


pin_led = Pin(16, mode=Pin.OUT)


def connect():
    print('Connected to MQTT Broker "%s"' % (server))
    client = MQTTClient(ClientID, server, 1883, user, password)
    client.connect()
    return client

def reconnect(client):
    print('Failed to connect to MQTT broker, Reconnecting...' % (server))
    time.sleep(5)
    client.reconnect()


def turn_led_on():
    pin_led.on()
    time.sleep(5)
    pin_led.off()
    

def process_message(topic, msg):
    # We are only subscribed to one topic, so we don't need to check the topic
    if msg == "Detected dog":
        turn_led_on()
    

def run():
    try:
        client = connect()
    except OSError as e:
        reconnect(client)


    # Set a callback for when messages are received on subscribed topics
    client.set_callback(process_message)
    # Subscribe to the topic
    client.subscribe(topic)

    while True:
        # Wait for any messages
        # This will trigger the callback when a message is available on our topic
        client.wait_msg()
