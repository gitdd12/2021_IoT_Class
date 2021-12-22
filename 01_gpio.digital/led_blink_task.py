import RPi.GPIO as GPIO
import time
LED_PIN_R = 17
LED_PIN_Y = 27
LED_PIN_G = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_Y, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)
for i in range(1):
    GPIO.output(LED_PIN_R, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_R, GPIO.LOW)
    print("led off")
    time.sleep(2)
    GPIO.output(LED_PIN_Y, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_Y, GPIO.LOW)
    print("led off")
    time.sleep(2)
    GPIO.output(LED_PIN_G, GPIO.HIGH)
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN_G, GPIO.LOW)
    print("led off")
    time.sleep(2)
  
      

GPIO.cleanup()