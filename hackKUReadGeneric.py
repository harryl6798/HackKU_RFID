import RPi.GPIO as GPIO
import SimpleMFRC522
import time
from squid import *

reader = SimpleMFRC522.SimpleMFRC522()
led = Squid(18, 23, 24)

print("Hold a tag near the reader")

def flash(color, times, delay):
    for i in range(0, times):
        led.set_color(color)
        time.sleep(delay)
        led.set_color(OFF)
        time.sleep(delay)

try:
    while True:
        led.set_color(GREEN)

        id, text = reader.read()
        if id:
            values = text.split(",")
            allergies = ""
            if len(values) == 8:
                
                #Will print the values according to the card given
                
                if values[1] == "1":
                    allergies += "Vegetarian, "
                if values[2] == "1":
                    allergies += "Vegan, "
                if values[3] == "1":
                    allergies += "Halal, "
                if values[4] == "1" :
                    allergies += "Pork, "
                if values[5] == "1":
                    allergies += "Lactose, "
                if values[6] == "1":
                    allergies += "Peanut, "
                if values[7] != "":
                    allergies += values[7]
                    
                print("Name: " + values[0] )
                print("Allergies: " + allergies)
                
            flash(RED, 6, .08)

finally:
    print("cleaning up")
    GPIO.cleanup()


