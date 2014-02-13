
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
    OC2_PIN_R1 = 21
    OC2_PIN_R2 = 27
    TRIGGER_PIN = 18
    ECHO_PIN = 23

    def __init__(self, revision=2):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(LEFT_GO_PIN, GPIO.OUT)
        GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_GO_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_DIR_PIN, GPIO.OUT)

        GPIO.setup(LED1_PIN, GPIO.OUT)
        GPIO.setup(LED2_PIN, GPIO.OUT)

        GPIO.setup(OC1_PIN, GPIO.OUT)
        if revision == 1:
            GPIO.setup(OC2_PIN_R1, GPIO.OUT)
        else:
            GPIO.setup(OC2_PIN_R2, GPIO.OUT)

        GPIO.setup(SW1_PIN, GPIO.IN)
        GPIO.setup(SW2_PIN, GPIO.IN)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)


    def set_motors(self, left_go, left_dir, right_go, right_dir):
        GPIO.output(LEFT_GO_PIN, left_go)
        GPIO.output(LEFT_DIR_PIN, left_dir)
        GPIO.output(RIGHT_GO_PIN, right_go)
        GPIO.output(RIGHT_DIR_PIN, right_dir)

    def forward(self, seconds=0):
        self.set_motors(1, 0, 1, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        self.set_motors(0, 0, 0, 0)
 
    def reverse(self, seconds=0):
        self.set_motors(1, 1, 1, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()
    
    def left(self, seconds=0):
        self.set_motors(1, 0, 1, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=0):
        self.set_motors(1, 1, 1, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def sw1_closed(self):
        return not GPIO.input(SW1_PIN)

    def sw2_closed(self):
        return not GPIO.input(SW2_PIN)

    def set_led1(self, state):
        GPIO.output(LED1_PIN, state)

    def set_led2(self, state):
        GPIO.output(LED2_PIN, state)

    def set_oc1(self, state):
        GPIO.output(OC1_PIN, state)

    def set_oc2(self, state):
        GPIO.output(OC2_PIN, state)    

    def _send_trigger_pulse(self):
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.0001)
        GPIO.output(TRIGGER_PIN, False)

    def _wait_for_echo(self, value, timeout):
        count = timeout
        while GPIO.input(ECHO_PIN) != value and count > 0:
            count = count - 1

    def get_distance(self):
        send_trigger_pulse()
        wait_for_echo(True, 10000)
        start = time.time()
        wait_for_echo(False, 10000)
        finish = time.time()
        pulse_len = finish - start
        distance_cm = pulse_len / 0.000058
        return distance_cm
