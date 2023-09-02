from ultralytics import YOLO
from paho.mqtt import client as mqtt_client
import time

broker="test.mosquitto.org"
port=1883
topic="doe_project/detector"
client_id=f'raspberry-pub-{time.time_ns()}'


def sendmessage(connection, detected_item):
    print("sending message")
    msg = f"Detected {detected_item}"
    result = connection.publish(topic, msg)
    
def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print("Failed to connect, return code %d", rc)
    
    client=mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
    
mqtt_connection = connect()    
    
model=YOLO("yolov8n.pt")
names=model.names


results = model.predict(source=0, stream=True, device="cpu")
for r in results:
    for box in r.boxes:
        name = names[int(box.cls)]
        conf = float(box.conf)
        # print(name, conf)
        if name == "dog" and conf > 0.6:
            sendmessage(mqtt_connection, name)
