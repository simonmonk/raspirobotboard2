Source code for use with the RaspiRobot Board V2.

**Note that if you are looking for version 1 of this board, please see:**

https://github.com/simonmonk/raspirobotboard

***Both version 1 and version 2 of the RasPiRobot Board work just fine with the new Raspberry Pi Model B+***

# Support
If you need any help with the software or board please contact linda@monkmakes.com or leave a comment on monkmakes.com

# Introduction

Version 2 of the RaspiRobot Board (RRB2) has learnt by the feedback from version 1 and it is a great improvement. 

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/rrb_on_chassis_fully%20loaded.JPG)


The main features of version 2 are listed below. Changes from version 1 are highlighted in bold:
+ **Supplied fully assembled - no soldering**
+ Bi-directional control of two motors
+ **Variable (PWM) power control**. This allows you to both control the speed of the motors independently. 
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

Note that you don't need a separate power supply for the Raspberry Pi. The RRB2 will provide 5V at 2A with ease to the Raspberry Pi, and motors. 

Note that 6V motor will usually work just fine at 5V.



# Installing the Python Libraries

On your Raspberry Pi, issue the following commands in a Terminal window:

```
$ wget https://github.com/simonmonk/raspirobotboard2/raw/master/python/dist/rrb2-1.1.tar.gz
$ tar -xzf rrb2-1.1.tar.gz
$ cd rrb2-1.1
$ sudo python setup.py install
```

Attach the RRB2 to your Raspberry Pi. You do not need to attach batteries, motors or anything else to the RRB2 just yet. For now you can just power it through the Pi's normal USB power connector.

Lets run some tests from the Python Console now that everything is installed. We can experiment with the RaspiRobot Board v2, even without any motors 

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

If you prefer, you can use True and False in place of 1 and 0 in the examples above.

# Connect a Battery and Motors

The quickest way to use the RRB2 as a roving robot is to buy a robot chassis such as the Magician Chassis (available from many sources) or similar low-cost robot chassis kits from eBay. These kits come as a laser cut body, a pair of gearmotors, often a battery box and nuts and bolts to fix it all together.

Here is one such chassis. The first step is to bolt this all together. Note that these are usually supplied with a 4 x AA battery box. You will need to swap this for a similar 6 x AA battery box or a 7.2V LiPo battery pack. Rechargeable batteries are a good idea when driving motors.

![Chassis](https://raw.githubusercontent.com/simonmonk/wiki_images/master/rrb_robot_chassis_parts.jpg)


Once the chassis is built, use some of the bolts suppled to fix the Raspberry Pi on the chassis and then attach the RRB2 onto the GPIO connector. Make sure its the right way arround, and that all the pins meet up with the socket.

The leads from the motors will thread up through the chassis and each pair of leads should go to one of the two screw terminals labelled L and R for (left and right). If you put the leads in the wrong way around, the direction of the motor will be opposite to that expected, so just swap them over if this happens.

![Motor wiring](https://raw.githubusercontent.com/simonmonk/wiki_images/master/rrb_attaching%20motors.jpg)

Next, make sure that your Raspberry Pi's USB power lead is unplugged. From now on we are going to power it from batteries.

**WARNING: Never power the Raspberry Pi from both batteries and the USB power connector. One or other, but NOT both.**

It is a good idea to leave the wheels off the robot chassis for now so that it does not unexpectedly drive itself off your table. One or both of the motors may spin as the Raspberry Pi starts up.

Wire the battery pack into the third pair of screw terminals. +V towards the outside of the board. The Raspberry Pi's power light should light up and it will start to boot. LED1 and LED2 on the RRB2 will also light up.

Having your Pi set up for WiFi will allow you to connect to it wirelessly [over SSH](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/overview). So, you may want to plug in a USB WiFi dongle.




# API Reference

## General
The library implements a class called RRB2. This is only available for Python 2 and any Python programs that you write that use the libaray must be run as a super user. I.e.

`sudo python myProgram.py'

To import the library and create an instance of the class, put this at the top of your Python program.

```
from rrb2 import *
rr = RRB2()
```

If you have an older revision 1 Raspberry Pi, then you need to do this instead:

```
from rrb2 import *
rr = RRB2(revision=1)
```

The rest is pretty straightforward, there are just a load of useful methods on the class that you can use.

## LEDs

There are two LEDs built-in to the RaspiRobotBoard, called LED1 and LED2. Both of these can be turned on and off using the following methods:

To turn LED1 on just do:

`rr.set_led1(1)`

To turn it off again do:

`rr.set_led1(0)`

To control LED2 just do the same thing but using setLED2.

## Switch Inputs

The sw1_closed() and sw2_closed() functions return true if the contacts for that switch are closed. By default, the switches are open. You can test out closing the switch by shorting the two contacts with a screwdriver.

The following test program will show you the state of each of the switch contacts.

```
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


## Motor (Low Level Interface)

The low level interface is intended for control of the motors directly. It allows you to control the speed of each motor and its direction independently.

The method for this (set_motors) takes four arguments: the left speed, left motor direction, right spped and direction.

So to set both motors going forward at full speed, you would just use the following:

`rr.set_motors(1, 0, 1, 0)`

.. and half speed would be:

`rr.set_motors(0.5, 0, 0.5, 0)`

to send the motors both at half speed in opposite directions is:

`rr.set_motors(0.5, 1, 0.5, 0)`

## Range Finder

If you fit the RRB2 with an SR-04 ultrasonic rangefinder, then you can use the following call to measure the distance to the enarest obstacle in cm.

`rr.get_distance()`

## Hardware

The RRB2 uses the following pins:

    LEFT_GO_PIN = 17
    LEFT_DIR_PIN = 4
    RIGHT_GO_PIN = 10
    RIGHT_DIR_PIN = 25   
    SW1_PIN = 11
    SW2_PIN = 9
    LED1_PIN = 7
    LED2_PIN = 8
    OC1_PIN = 22
    OC2_PIN = 27
    OC2_PIN_R1 = 21 (rev 1) or 27 rev 2
    TRIGGER_PIN = 18
    ECHO_PIN = 23

The LEDs and OC outputs are buffered. The switch inputs are not.

You can find the EAGLE design files in the "hardware" section of tis repo.


# Using I2C Displays

The I2C socket is pin compatible with these Adafruit displays: 
+ [4 Digit 7-segment display (red)](http://www.adafruit.com/products/878)
+ [Mini 8x8 LED Matrix (red)](http://www.adafruit.com/products/870)
+ [Bi-color 8x8 LED Matrix (red)](http://www.adafruit.com/products/902)

To use these you will need to download Adafruit's Python library for the Pi from [here](http://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/overview).

Make sure that you plug the display in the right way around. The socket pins are labelled on the RRB2, make sure they match up with the labels on the display. You can use male to female jumper wires if you wish to put the display further away or its too big.


# Example Projects

Have a look in the "examples" folder of this library for some examples using the RRB2.


