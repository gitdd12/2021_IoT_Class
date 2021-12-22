import datetime
now = datetime.datetime.now()
separated_second= []
separated_minute= []
# 시간과 분 받기
second = now.strftime('%S')
minute = now.strftime('%M')

second_1= int(int(second)/10)
second_2= int(int(second)%10)

minute_1= int(int(minute)/10)
minute_2= int(int(minute)%10)

# 4digit.py
import RPi.GPIO as GPIO
import time

#               A,B,C,D,E,F,G
SEGMENT_PINS = [2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]

GPIO.setmode(GPIO.BCM)

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

def display(digit, number)): #자릿수, 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정
    for i in range(4): # 0~3
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)

# 숫자 출력
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])

try:
    while True:
        display(1, minute_1)
        display(2, minute_2)
        display(3, second_1)
        display(4, second_2)

finally:
    GPIO.cleanup()
    print('bye')

