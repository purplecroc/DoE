# Week 5

This week I am going to be experimenting with sending messages to a publish/subscribe server.  This will enable me to send and recieve messages to and from the device.

I decided to use the popular [MQTT](https://mqtt.org/) protocol as there are many libraries available for Pyton that implement the protocol.

As I am using micropython, I researched the corret library to use, and found [umqtt.simple](https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html).

Once this was installed on the device, I was able to use it to connect to a public MQTT broker.  I decided to use [test.mosquitto.org](https://test.mosquitto.org/) as it is free to use.

Once connected, I could see messages arriving on the topic, so I am ready to move on to the next step.

## Problems

This was quite a difficult task to complete because I needed help getting the umqtt.simple library installed on the target device.  I had to be manually copy it onto the device.  I think I was packaging the application incorrectly, so I will come back to this at a future date to try and resolve properly.