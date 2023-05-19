import RPi.GPIO as GPIO
import time

PIR_sensor1 = 18
PIR_sensor2 = 16
m11 = 29
m12 = 31

GPIO.setmode(GPIO.BCM) 
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(PIR_sensor1, GPIO.IN)
GPIO.setup(PIR_sensor2, GPIO.IN)

pwm = GPIO.PWM(36, 100) 
pwm.start(90)

try:
    while True:
        if GPIO.input(PIR_sensor1):
            GPIO.output(m11, GPIO.HIGH)  # gate opening
            GPIO.output(m12, GPIO.LOW)
            time.sleep(10)  # delay for simulation 

            GPIO.output(m11, GPIO.LOW)  # gate stop for a while
            GPIO.output(m12, GPIO.LOW)
            time.sleep(5)

        if GPIO.input(PIR_sensor2):
            GPIO.output(m11, GPIO.LOW)  # gate closing
            GPIO.output(m12, GPIO.HIGH)
            time.sleep(10)

            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
