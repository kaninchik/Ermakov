import RPi.GPIO as GPIO

def dec2bin(value):
    return[int(elem) for elem in bin(value) [2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("number from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                volt = float(num)/255 * 3,3
                
            else:
                if num < 0:
                    print("error! num have to be >= 0")
                else:
                    if num > 255:
                        print("error! num have to be <= 255")
        except Exception:
            if num == 'q':
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()