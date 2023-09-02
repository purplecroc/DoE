# DoE coding projects

Please not that some files are for the rpi_pico and others for the rpi.

The files for rpi_pico are in the rpi_pico directory.  This is so that they can be uploaded independent of the rpi files.

To run the examples targeting the rpi pico, upload this project and then import the 'run' function like this:

```python
>>> from rpi_pico.main import run
>>> # Then you can run any example you want
>>> run(1)
Run week 1
No code in week 1
```

## Plan
- [Week 1](./rpi_pico/Week_1/Week_1.md)
    - Plan the project
    - Run a hello world program on the raspberry pi pico in micropython
- [Week 2](./rpi_pico/Week_2/Week_2.md)
    - Learn how to use [GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output#:~:text=A%20general%2Dpurpose%20input%2Foutput,and%20is%20controllable%20by%20software.)
    (General Purpose Input Output)
- [Week 3](./rpi_pico/Week_3/Week_3.md)
    - Source components for motion sensor project 
    - Wire a circuit 
    - Write code to detect motion over a GPIO
- [Week 4](./rpi_pico/Week_4/Week_4.md)
    - Use a rpi pico w and connect it to WiFi using python
- [Week 5](./rpi_pico/Week_5/Week_5.md)
    - Build a piblish/subscribe demonstration
    - Turn on/off an LED from a remote PC using the pub/sub
- [Week 6](./Week_6/Week_6.md)
    - Use a rpi4 and camera to take pictures using python
- [Week 7](./Week_7/Week_7.md)
    - Install YOLO (You Only Look Once) to do object detection from the camera
- [Final Project](./Final_project/Final_project.md)
    - Bring together all the things I have learnt on this project
    - If a dog is deteted, send a message over MQTT
    - The messages are received by a rpi pico device and alerts the user that a dog is in front of the camers