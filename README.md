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
`$ sudo python`

Then, within the python console, type the following, one line at a time:

```
from rrb2 import *
rr = RRB2()
rr.set_led1(1)
rr.set_led1(0)
rr.set_led2(1)
rr.set_led2(0)
rr.sw1_closed()
```

The last step should display the answer "False" because no switch is attached.



# Connect a Battery and Motors


# API Reference

## General
The library implements a class called RaspiRobot. This is only available for Python 2 and any Python programs that you write that use the libaray must be run as a super user. I.e.

`su python myProgram.py'

To import the library and create an instance of the class, put this at the top of your Python program.

```
from rrb2 import *
rr = RRB2()
```

The rest is pretty straightforward, there are just a load of useful methods on the class that you can use.

## LEDs

There are two LEDs built-in to the RaspiRobotBoard, called LED1 and LED2. Both of these can be turned on and off using the following methods:

To turn LED1 on just do:

`rr.setLED1(1)`

To turn it off again do:

`rr.setLED1(0)`

To control LED2 just do the same thing but using setLED2.

## Switch Inputs

The sw1_closed() and sw2_closed() functions return true if the contacts for that switch are closed. By default, the switches are open. You can test out closing the switch by shorting the two contacts with a screwdriver.

The following test program will show you the state of each of the switch contacts.

```
import RPi.GPIO as GPIO
from rrb2 import *

rr = RRB2()

while True:
    print("SW1=" + str(rr.sw1_closed()) + " SW2=" + str(rr.sw2_closed()))
    raw_input("check again")
```


## Open Collector Outputs

The RaspiRobotBoard has two low-power open collector outputs. These can each source up to 25mA and so are suitable for driving LEDs with series resistors. They can also be used to drive transistors and other external electronics. They are buffered and therefore protect the Raspberry Pi' s processor.

To turn the Open Collector OC1 output on just do:

`rr.set_oc1(1)`

To turn it off again do: 

`rr.set_oc1(0)`

To control OC2, substitute oc2 in place of oc1 in the examples above

## Motor (High Level Interface)

There are two levels of command for controlling the motors. There is a high level interface that assumes that the motors are connected to wheels on a rover. These commands are forward, reverse, left, right and stop.

`rr.forward()`

... will start both motors running in the same direction to move the robot rover forwards. They will continue in this direction until another command is issued.

If you want to move forward for a certain amount of time, you can specify a number of seconds as an optional first argument. If you supply a second parameter between 0 and 1 this will control the speed of the motor. This is set to 0.5 as a defaut. If you want the motors to run indefinately, but also want to control the speed, then use 0 as the first patrameter.

Some examples:

```
rr.forward()       # forward half speed indefinately
rr.forward(5)      # forward for 5 seconds at half speed
rr.forward(5, 1)   # forward for 5 seconds at full speed
```

The commands left, right and reverse all work in the same way.

The stop command stops all the motors.




# Example Projects

Have a look in the examples folder of this library for some examples using the RRB2.
