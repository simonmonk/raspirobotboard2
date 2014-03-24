
# Attach: SR-04 Range finder and of course motors.


from rrb2 import *
import time, random

rr = RRB2()

def turn_randomly():
    turn_time = random.randint(1, 3)
    rr.left(turn_time, 0.5)
    rr.stop()

while True:
    distance = rr.get_distance()
    if distance < 30:
        turn_randomly()
    rr.forward(0, 0.7)
    time.sleep(0.5)
