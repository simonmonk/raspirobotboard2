#rrb2.py Library

import RPi.GPIO as GPIO
import time

class RRB2:
	
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
    OC2_PIN_R1 = 21
    OC2_PIN_R2 = 27
    TRIGGER_PIN = 18
    ECHO_PIN = 23
    left_pwm = 0
    right_pwm = 0

    def __init__(self, revision=2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.LEFT_GO_PIN, GPIO.OUT)
        self.left_pwm = GPIO.PWM(self.LEFT_GO_PIN, 500)
        self.left_pwm.start(0)
        GPIO.setup(self.LEFT_DIR_PIN, GPIO.OUT)
        GPIO.setup(self.RIGHT_GO_PIN, GPIO.OUT)
        self.right_pwm = GPIO.PWM(self.RIGHT_GO_PIN, 500)
        self.right_pwm.start(0)
        GPIO.setup(self.RIGHT_DIR_PIN, GPIO.OUT)

        GPIO.setup(self.LED1_PIN, GPIO.OUT)
        GPIO.setup(self.LED2_PIN, GPIO.OUT)

        GPIO.setup(self.OC1_PIN, GPIO.OUT)
        if revision == 1:
            self.OC2_PIN = self.OC2_PIN_R1
        else:
            self.OC2_PIN = self.OC2_PIN_R2

        GPIO.setup(self.OC2_PIN_R2, GPIO.OUT)

        GPIO.setup(self.SW1_PIN, GPIO.IN)
        GPIO.setup(self.SW2_PIN, GPIO.IN)
        GPIO.setup(self.TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)



    def set_motors(self, left_go, left_dir, right_go, right_dir):
        self.left_pwm.ChangeDutyCycle(left_go * 100)
        GPIO.output(self.LEFT_DIR_PIN, left_dir)
        self.right_pwm.ChangeDutyCycle(right_go * 100)
        GPIO.output(self.RIGHT_DIR_PIN, right_dir)

    def forward(self, seconds=0, speed=0.5):
        self.set_motors(speed, 0, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        self.set_motors(0, 0, 0, 0)
 
    def reverse(self, seconds=0, speed=0.5):
        self.set_motors(speed, 1, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()
    
    def left(self, seconds=0, speed=0.5):
        self.set_motors(speed, 0, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=0, speed=0.5):
        self.set_motors(speed, 1, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def sw1_closed(self):
        return not GPIO.input(self.SW1_PIN)

    def sw2_closed(self):
        return not GPIO.input(self.SW2_PIN)

    def set_led1(self, state):
        GPIO.output(self.LED1_PIN, state)

    def set_led2(self, state):
        GPIO.output(self.LED2_PIN, state)

    def set_oc1(self, state):
        GPIO.output(self.OC1_PIN, state)

    def set_oc2(self, state):
        GPIO.output(self.OC2_PIN, state)    

    def _send_trigger_pulse(self):
        GPIO.output(self.TRIGGER_PIN, True)
        time.sleep(0.0001)
        GPIO.output(self.TRIGGER_PIN, False)

    def _wait_for_echo(self, value, timeout):
        count = timeout
        while GPIO.input(self.ECHO_PIN) != value and count > 0:
            count = count - 1

    def get_distance(self):
        self._send_trigger_pulse()
        self._wait_for_echo(True, 10000)
        start = time.time()
        self._wait_for_echo(False, 10000)
        finish = time.time()
        pulse_len = finish - start
        distance_cm = pulse_len / 0.000058
        return distance_cm
