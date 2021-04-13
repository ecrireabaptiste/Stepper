import ModuleStepper
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

stepper1 = ModuleStepper.Stepper(20,21,16,12,7,8) # (pin_dir, pin_step, pin_sleep, pin_M0, pin_M1, pin_M2)
stepper1.step(0,0.5,2,32) #dir, revs, rps, microstep
stepper1.step(1,1,4,16) #dir, revs, rps, microstep
stepper1.step(0,2,8,8) #dir, revs, rps, microstep

GPIO.cleanup()
