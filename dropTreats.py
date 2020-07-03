
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
from subprocess import call

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)

p.start(1.5)


p.ChangeDutyCycle(7.5)  # turn towards 90 degree
time.sleep(1) # sleep 1 second
p.stop()

call(["python", "runCamera.py"])


