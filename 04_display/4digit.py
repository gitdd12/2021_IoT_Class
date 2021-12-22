# 4digit.py
import time
import RPi.GPIO as GPIO


#               A, B, C, D, E, F, G
SEGMENT_PINS = [14,15,18,13,19,25,26]
DIGIT_PINS = [10,9,11,16]

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

def display(digit, number): #자릿수, 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정
    for i in range(4): # 0~3
        if i + 1 == digit:
            for segment in SEGMENT_PINS:
                GPIO.output(SEGMENT_PINS, GPIO. LOW)
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

# 숫자 출력
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
try:
    while True:
        display(1, 2)
        display(2, 0)
        display(3,2)
        display(4, 1)

finally:
    GPIO.cleanup()
    print('bye')

