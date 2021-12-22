#dht11.py
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4
LED_PIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (t, h))
        if(t>70):
            GPIO.output(LED_PIN, GPIO.HIGH)
        
finally:
    print('bye')