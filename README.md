Source code for use with the RaspiRobot Board V2.

Note that if you are looking for version 1 of this board, please see:

https://github.com/simonmonk/raspirobotboard

# Introduction

Version 2 of the RaspiRobot Board has learnt from the lessons and feedback from version 1 and it is a great improvement over version 1. 

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/rrb_on_chassis_fully%20loaded.JPG)


The main features of version 2 are listed below. Improvements from version 1 are highlighted in bold:
+ Supplied fully assembled - no soldering
+ Bidirectional control of two motors
+ **Variable (PWM) power control**. This allows you to both control the speed of the motors independently and the use of  lower voltage motors than the battery pack. 
+ **Supplies the Raspberry Pi with upto 2A using a switch mode power supply - run a fully loaded Pi and the Robot from 6 x AA batteries**
+ **Rangefinder header socket directly compatible with cheap HC-SR-04 ultrasonic range finders. Just plug them in directly**
+ **5V I2C header, pin compatible with Adafruit displays**
+ Two buffered open collector outputs
+ Two LEDs
+ Two switch inputs
+ Screw terminals for motors and battery
 

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/labelled_rrb2.png)


# How it Works

The diagram below shows how an RRB2 board is used. The RRB2 is powered from a battery pack that needs to be between 6 and 12V DC. Although using 4 x AA batteries can in theory provide 6V, actually the battery voltage will usually quickly fall below that, so it it better to use at least 6 x AA batteries, either rechargeable or regular heavy duty batteries. A 7.2V LiPo battery pack will also work just fine.

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/schematic.png)

Note that you don't need a separate power supply for the Raspberry Pi. The RRB2 will provide 5V at 2A with ease to the Raspberry Pi, and because the motors are powered directly from the battery and not via the RRB2s voltage regulator, the supply to the Raspberry Pi will remain clean and reliable.

This does mean that the motors that you use may be okay with the battery voltage. So, if you are using 6 x AA batteries giving a voltage of 9V then you should use motors that are okay with 9V.

If you have lower voltage motors, such as 6V motors often supplied as part of a robot chassis, then you can still use these, but you must be careful to lower the output power of the motors in your control program, or you could burn out your motors.


# Installing the Python Libraries

On your Raspberry Pi, issue the following commands in a Terminal window:

`
$ wget https://github.com/simonmonk/raspirobotboard2/archive/master.zip
$ unzip master.zip
$ cd raspirobotboard2-master
$ sudo python setup.py install
`
Attach the RRB2 to your Raspberry Pi. You do not need to attach batteries, motors or anything else to the RRB2 just yet. For now you can just power it through the Pi. 

Run Some Tests from the Python Console Now that everything is installed, we can experiment with the RaspiRobot Board v2, without any motors 

Open a Python console (Python2 not 3) by typing the following into a Terminal window:
`
$ sudo python
`

Then, within the python console, type the following, one line at a time:

`
from rrb2 import *
rr = RaspiRobot()
rr.set_led1(1)
rr.set_led1(0)
rr.set_led2(1)
rr.set_led2(0)
rr.sw1_closed()
`

The last step should display the answer "False" because no switch is attached.




# Example Code
