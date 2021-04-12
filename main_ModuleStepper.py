import ModuleStepper
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

stepper1 = ModuleStepper.Stepper(20,21,16)
stepper1.step(0,0.5,2) #dir, revs, rps
stepper1.step(1,1,4) #dir, revs, rps
stepper1.step(0,2,8) #dir, revs, rps

GPIO.cleanup()
