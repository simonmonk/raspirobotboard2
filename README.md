Source code for use with the RaspiRobot Board V2.

Note that if you are looking for version 1 of this board, please see:

https://github.com/simonmonk/raspirobotboard

# Introduction

Version 2 of the RaspiRobot Board has learnt from the lessons and feedback from version 1 and it is a great improvement over version 1. 

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/rrb2_on_pi.jpg)


The main features of version 2 are listed below. Improvements from version 1 are highlighted in bold:
+ Supplied fully assembled - no soldering
+ Bidirectional control of two motors
+ **Variable (PWM) power control of the motors**. This allows you to both control the speed of the motors independently and use lower voltage motors than the voltage of your battery pack. 
+ **Supplies the Raspberry Pi with upto 2A using a switch mode power supply - run a fully loaded Pi and the Robot from 6 x AA batteries**
+ **Rangefinder header socket directly compatible with cheap SR-04 ultrasonic range finders. Just plug them in directly**
+ **5V I2C header, pin compatible with Adafruit displays**
+ Two buffered open collector outputs
+ Two LEDs
+ Two switch inputs
+ Screw terminals for motors and battery


# How it Works

The diagram below shows how an RRB2 board is used. The RRB2 is powered from a battery pack that needs to be between 6 and 12V DC. Although using 4 x AA batteries can in theory provide 6V, actually the battery voltage will usually quickly fall below that, so it it better to use at least 6 x AA batteries, either rechargeable or regular heavy duty batteries. A 7.2V LiPo battery pack will also work just fine.

![RRBv2](https://raw.githubusercontent.com/simonmonk/wiki_images/master/schematic.png)

Note that you do not need a separate power supply for the Raspberry Pi. The RRB2 will provide 5V at 2A with ease to the Raspberry Pi, and because the motors are powered directly from the battery and not via the RRB2s voltage regulator, the supply to the Raspberry Pi will remain clean and reliable.

This does mean that the motors that you use may be okay with the battery voltage. So, if you are using 6 x AA batteries giving a voltage of 9V then you should use motors that are okay with 9V.

If you have lower voltage motors, such as 6V motors often supplied as part of a robot chassis, then you can still use these, but you must be careful to lower the output power of the motors in your control program, or you could burn out your motors.



# Installation


# Example Code
