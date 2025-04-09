import RPi.GPIO as GPIO
import time
import random
import os
GPIO.setmode(GPIO.BCM)
led_pin = 17
button_pin = 27
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
player_name = input("Please enter your name: ")
try:
    while True:
        wait_time = random.uniform(1, 5)
        time.sleep(wait_time)
        GPIO.output(led_pin, GPIO.HIGH)
        start_time = time.time()
        while GPIO.input(button_pin) == GPIO.HIGH:
            pass
        end_time = time.time()
        reaction_time = end_time - start_time
        GPIO.output(led_pin, GPIO.LOW)
        print(f"{player_name}, your reaction time is: {reaction_time:.3f} seconds")
except KeyboardInterrupt:
    print("Game over")
finally:
    GPIO.cleanup()    
