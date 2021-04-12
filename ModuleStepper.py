from time import sleep
import RPi.GPIO as GPIO

steps360 = 200

class Stepper: 
    def __init__(self, pin_dir, pin_step, pin_sleep):
        self.pin_dir = pin_dir
        self.pin_step = pin_step
        self.pin_sleep = pin_sleep

        GPIO.setup(self.pin_dir, GPIO.OUT)
        GPIO.setup(self.pin_step, GPIO.OUT)
        GPIO.setup(self.pin_sleep, GPIO.OUT)
        GPIO.output(self.pin_sleep, GPIO.LOW)

    def step(self, direction, rev, rps):

        delay = 1/rps/steps360
        
        GPIO.output(self.pin_sleep, GPIO.HIGH)
        
        GPIO.output(self.pin_dir, direction)
        
        for x in range(round(rev*steps360)):
            GPIO.output(self.pin_step, GPIO.HIGH)
            sleep(delay/2)
            GPIO.output(self.pin_step, GPIO.LOW)
            sleep(delay/2)
            
        GPIO.output(self.pin_sleep, GPIO.LOW)