from time import sleep
import RPi.GPIO as GPIO

STEPS360 = 200
RESOLUTION = {1 : (0, 0, 0),
              2 : (1, 0, 0),
              4 : (0, 1, 0),
              8 : (1, 1, 0),
              16: (0, 0, 1),
              32: (1, 0, 1)}

class Stepper: 
    def __init__(self, pin_dir, pin_step, pin_sleep, pin_M0, pin_M1, pin_M2):
        self.pin_dir = pin_dir
        self.pin_step = pin_step
        self.pin_sleep = pin_sleep
        self.pin_microstep = (pin_M0, pin_M1, pin_M2)
        
        GPIO.setup(self.pin_dir, GPIO.OUT)
        GPIO.setup(self.pin_step, GPIO.OUT)
        GPIO.setup(self.pin_sleep, GPIO.OUT)
        GPIO.setup(self.pin_microstep, GPIO.OUT)
        
        GPIO.output(self.pin_sleep, GPIO.LOW)

        
    def step(self, direction, rev, rps, microstep):

        delay = 1/rps/STEPS360
        
        GPIO.output(self.pin_microstep, RESOLUTION[microstep])
        GPIO.output(self.pin_dir, direction)
        GPIO.output(self.pin_sleep, GPIO.HIGH)
        
        
        
        for x in range(round(rev*STEPS360*microstep)):
            GPIO.output(self.pin_step, GPIO.HIGH)
            sleep(delay/2/microstep)
            GPIO.output(self.pin_step, GPIO.LOW)
            sleep(delay/2/microstep)
            
        GPIO.output(self.pin_sleep, GPIO.LOW)
