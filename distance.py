import time
import RPi.GPIO as GPIO

TRIG = 23 # check input
ECHO = 24 # check input

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def present(threshold=12, duration=5):
    start_time = time.time()
    while time.time() - start_time < duration:
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance > threshold:
            return False
    return True
