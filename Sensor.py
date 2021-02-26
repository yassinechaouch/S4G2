import RPi.GPIO as GPIO

led=8
sensor=10
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(sensor, GPIO.IN)

while True:
    if GPIO.input(sensor):
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)





