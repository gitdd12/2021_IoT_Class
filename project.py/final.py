import datetime

# 4digit.py
import RPi.GPIO as GPIO

#dht11.py
import time
import Adafruit_DHT

# Thread
import threading


GPIO.setmode(GPIO.BCM)        
LED_PIN = 2
GPIO.setup(LED_PIN, GPIO.OUT)
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4






#4_digit_FND 출력
#               A, B, C, D, E, F, G
SEGMENT_PINS = [14,15,18,13,19,25,26]
DIGIT_PINS = [10,9,11,16]



for segment in SEGMENT_PINS:
    GPIO.setup(SEGMENT_PINS, GPIO.OUT)
    GPIO.output(SEGMENT_PINS, GPIO. LOW)
#digit 핀은 (HIGH->OFF, LOW->ON)
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

def display(digit, number): #자릿수, 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)
            

hour_1 = 0
hour_2 = 0
minute_1 = 0
minute_2 = 0

def getTime():
    global hour_1, hour_2, minute_1, minute_2
    while True:
        now = datetime.datetime.now()
        # 시간과 분 받기
        hour = int(now.strftime('%H')) + 8
        minute = now.strftime('%M')

        hour_1= int(int(hour)/10)
        hour_2= int(int(hour)%10)

        minute_1= int(int(minute)/10)
        minute_2= int(int(minute)%10)
        time.sleep(60)

humidity = 0
def getHumidity():
    global humidity
    while True:
        # 습도 출력
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (t, h))
            humidity = h
        
        time.sleep(5)
        # 습도가 70이상이면 LED_PIN에 불들어오기
def lightByHumid():
    while True:
        if(humidity>=70):
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

timeThread = threading.Thread(target = getTime)
timeThread.start()

humidityThread = threading.Thread(target = getHumidity)
humidityThread.start()

lightThread = threading.Thread(target = lightByHumid)
lightThread.start()

try:
    while True:
        display(1, hour_1)
        display(2, hour_2)
        display(3, minute_1)
        display(4, minute_2)


        # 습도 출력

        
        # 습도가 70이상이면 LED_PIN에 불들어오기
        if(humidity>70):
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
finally:
    GPIO.cleanup()
    print('bye')

