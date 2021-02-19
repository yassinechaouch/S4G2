import RPI.GPIO as GPIO
from time import sleep
GPIO.setup (8, GPIO.OUT, initial=GPIO.LOW)
for i in range (5):
    GPIO.output (8,GPIO.HIGH)
    sleep (1)
    GPIO.output(8,GPIO.LOW)
    sleep (1)