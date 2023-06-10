from picamera2 import Picamera2, Preview
from pynput import keyboard
import time
picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

def on_press(key):
    if key.char == 'a':
        picam2.capture_file("picture.jpg")

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

while True:
    time.sleep(1)
