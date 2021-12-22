from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    print('Writing to Display')
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string(now.strftime("%x%X"), 1)
        time.sleep(0.5)
        if h is not None and t is not None:
            display.lcd_display_string('%.1f*C, %.1f%%   ' % (t, h),2)
            time.sleep(6)

    
finally:
    print("cleaning up")
    display.lcd_clear()

    
        