# Attach: SR-04 Range finder, switch on SW1, and of course motors.

# The switch stops and starts the robot

from rrb2 import *
import time, random

rr = RRB2()

motor_speed = 0.6

# if you dont have a switch, change the value below to True
running = False

def turn_randomly():
    turn_time = random.randint(1, 3)
    if random.randint(1, 2) == 1:
        rr.left(turn_time, motor_speed)
    else:
        rr.right(turn_time, motor_speed)
    rr.stop()

while True:
    distance = rr.get_distance()
    if distance < 50 and running:
        turn_randomly()
    if running:
        rr.forward(0, motor_speed)
    if rr.sw2_closed():
        running = not running
    if not running:
        rr.stop()
    time.sleep(0.2)
