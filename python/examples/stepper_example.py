# To create this I stared with 
# http://razzpisampler.oreilly.com/ch06.html and
# http://www.nmbtc.com/step-motors/engineering/full-half-and-microstepping/
# with some modifcations to make this easier to understand
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pin constants
COIL_A_1 = 17  # power coil a
COIL_A_2 = 04  # direction coil a
COIL_B_1 = 10  # power coil b
COIL_B_2 = 25  # direction coil b 

#  coil state constants
ON = True # Power
OFF = False # Off = no power
FD = True # Current flows forward
BK = False # Current flows backward

GPIO.setup(COIL_A_1, GPIO.OUT) 
GPIO.setup(COIL_A_2, GPIO.OUT) 
GPIO.setup(COIL_B_1, GPIO.OUT) 
GPIO.setup(COIL_B_2, GPIO.OUT)

init_seq = [ OFF, FD, OFF, FD ]

# Single phase this mode requires the least amount 
# of power from the driver.
single_phase_seq = [
   [OFF, BK,  ON, FD],
   [ ON, BK, OFF, BK],
   [OFF, FD,  ON, BK],
   [ ON, FD, OFF, FD],
]

# Dual phase excitation provides about 30% to 40%
# more torque than single phase excitation.
dual_phase_seq = [
   [ON, BK, ON, FD],
   [ON, BK, ON, BK],
   [ON, FD, ON, BK],
   [ON, FD, ON, FD],
]

# Half stepping produces roughly 15% less 
# torque than dual phase full stepping
# and twice the resolution
half_step_seq = [
   [ ON, FD,  ON, FD],
   [OFF, FD,  ON, FD],
   [ ON, BK,  ON, FD],
   [ ON, BK, OFF, FD],
   [ ON, BK,  ON, BK],
   [OFF, BK,  ON, BK],
   [ ON, FD,  ON, BK], 
   [ ON, FD, OFF, BK],
]

def step(sequence, forward, delay, steps):
   global curPos
   seqLen = len(sequence);
   for i in range(steps):
      if forward:
         curPos = curPos + 1
      else:
         curPos = curPos - 1
      if curPos < 0: curPos = seqLen - 1 
      if curPos == seqLen: curPos = 0
      set_coils(sequence[curPos])
      time.sleep(delay)

def set_coils(step):
   GPIO.output(COIL_A_1, step[0])
   GPIO.output(COIL_A_2, step[1])
   GPIO.output(COIL_B_1, step[2])
   GPIO.output(COIL_B_2, step[3])

try:
  while True:
    set_coils(init_seq)
    curPos = 0
    seq_type = raw_input("Choose type\n 0: Single Phase\n 1: Dual Phase \n 2: Half Step \n?")
    if seq_type == 2: sequence = half_step_seq
    if seq_type == 1: sequence = dual_phase_seq
    else: sequence = single_phase_seq
    delay = raw_input("Delay between steps (milliseconds)?")
    steps_forward = raw_input("How many steps forward? ")
    step(sequence, True, int(delay) / 1000.0, int(steps_forward))
    steps_step_backward = raw_input("How many steps backwards? ")
    step(sequence, False, int(delay) / 1000.0, int(steps_forward))
except KeyboardInterrupt:
   GPIO.cleanup()
   print "Cleanup GPIO"
except:
   GPIO.cleanup()
   raise
