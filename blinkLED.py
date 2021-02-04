import time
# import urllib2 (this is good when fetching a remote resource instead of a local one)
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # important step with GPIO
ledPin = 17
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

def getBlinkRate():
    # get the blinkrate from the local file system
    f = open("/var/www/html/blinkRate.txt")
    # read the contents of the file 
    return float(f.read())

def main():
    blink_rate = 0
    prev_time = time.time()
    # run the main loop for controlling the led
    while True:
        if(time.time() - prev_time > 1): # every 1 second, read the contents of the file
            # print(getBlinkRate())
            blink_rate = getBlinkRate()
            prev_time = time.time()
        if(blink_rate != 0):
            GPIO.output(ledPin, GPIO.HIGH) # Turn on
            sleep(blink_rate) # stay on for blink_rate
        GPIO.output(ledPin, GPIO.LOW) # Turn off
        sleep(blink_rate) # remain off for blink_rate

main()
