import RPi.GPIO as GPIO
from time import sleep

def dec2bin(value):
    return[int(elem) for elem in bin(value) [2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

is_min = 1
x = 0

try:
    period = float(input("period for signal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            is_min = 1
        else:
            if x == 255:
                is_min = 0
    
        if is_min == 1:
            x = x + 1
        else:    
            x = x - 1

        sleep(period)

except ValueError:
    print("Period isn't correct")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

