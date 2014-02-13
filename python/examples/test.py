#Python 2

import rrb2 as rrb
import time

rr = rrb.RRB2(revision=2)

def confirm(question):
    answer = raw_input(question)

def test_leds():
    rr.set_led1(0)
    rr.set_led2(0)
    confirm("Are LED1 and LED2 both OFF?")
    
    rr.set_led1(1)
    rr.set_led2(0)
    confirm("Is LED1 ON and LED2 OFF?")
    
    rr.set_led1(1)
    rr.set_led2(1)
    confirm("Are LED1 and LED2 both ON?")
    
    rr.set_led1(0)
    rr.set_led2(0)
    confirm("Are LED1 and LED2 both OFF?")
    

def test_oc():
    rr.set_oc1(1)
    rr.set_oc2(1)
    confirm("Are [LED E] and [LED F] both OFF?")
    
    rr.set_oc1(0)
    rr.set_oc2(1)
    confirm("Is [LED E] ON and [LED E] OFF?")

    rr.set_oc1(1)
    rr.set_oc2(1)
    confirm("Are [LED E] and [LED F] both ON?")
    
    rr.set_oc1(1)
    rr.set_oc2(1)
    confirm("Are [LED E] and [LED F] both OFF?")
    
def test_switches():
    print("Remove header jumpers from [SW1] and [SW2]")
    while sw1_closed() or sw2_closed():
        pass
    print("PASS: [SW1] and [SW2] open")
    
    print("Fit header jumpers over [SW1] only")
    while not sw1_closed() or sw2_closed():
        pass
    print("PASS: [SW1] closed")
    
    print("Fit header jumpers over [SW2] only")
    while sw1_closed() or not sw2_closed():
        pass
    print("PASS: [SW2] closed")
    
    print("Fit header jumpers on both [SW1] and [SW2]")
    while not sw1_closed() or not sw2_closed():
        pass
    print("PASS: [SW1] and [SW2] closed")
    
