# Final project

For my final project I will combine all the skills I learn in previous projects to detect when a dog is seen by the raspberry pi 4. 

All the code for the detector will be in the [detector directory](/Final_project/Detector/) and the code for the alerter will be in the [alerter directory](/Final_project/Alerter/).


## Detector

The decector is a slight modification of the code I created in [week 7](/Week_7/Week_7.md).  Instead of showing the detections on the screen, I check for a dog being in the set of data returned from the YOLO model.

If I detect a a dog with a confidence of over 60%, I send a message to the MQTT topic saying that a dog has been detected.  This message can then be picked up by all clients subscribed to the same topic.

Because I are not using micropython on the Raspberry Pi 4 as I was on the Raspberry Pi Pico, I have had to use a different MQTT library.

```
pip3 install paho-mqtt
```

The code was completed and tested and I could see messages being published to the topic when my dog was visible.

## Alerter

In the previous project in [Week 5](/rpi_pico/Week_5/) I was sending messages to the topic.  I will need to modify this slightly to respond to messages read from the topic.

When the device receives the messahe "Detected dog", it turns on the LED for 5 seconds.