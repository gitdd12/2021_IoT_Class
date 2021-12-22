import RPi.GPIO as GPIO
import time
import cv2
import spidev
import numpy as np
import sys

#GPIO PIN 설정
TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN_RED = 5

#GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# xml 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

#LDR 설정
spi = spidev.SpiDev()

spi.open(0,0) # bus: 0, dev: 0

spi.max_speed_hz = 100000

# analog -> digital 변환
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 : 0000 1000 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

# 초음파 센서
try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)   # 10us(1us -> 0.000001s)      
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time() # 시작시간

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time() # 종료시간

        duration_time = stop - start
        distance = 17160 * duration_time
        #동영상 촬영
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        #조도센서 값 읽기
        reading = analog_read(0)
        cv2.imshow('frame', frame)
        print("Reading=%d" % reading)
        #명암대비 조절을 위한 배열과 변수 설정
        val = 100
        array = np.full(frame.shape, (val, val, val), dtype=np.uint8)
        #만약 조도센서의 값이 100이하면(주변이 어두워지면) 밝아지게
        if reading <= 100:
            print("Bright UP")
            frame = cv2.add(frame, array)
            cv2.imshow('frame', frame)
        #만약 조도센서의 값이 150이상이면(주변이 밝아지면) 어두워지게
        elif reading >= 150:
            print("Bright Down")
            frame = cv2.subtract(frame, array)
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) == 13:
            now_str = time.strftime("%Y%m%d_%H%M%S")
            cv2.imwrite('photo_%s.jpg' % now_str, frame)
        #1m안에서 움직임이 감지되면 RED LED ON
        print('Distance: %.1fcm' % distance)
        time.sleep(0.1)
        if distance <= 100:
            GPIO.output(LED_PIN_RED, GPIO.HIGH)
    
        else:
            GPIO.output(LED_PIN_RED, GPIO.LOW)
    

finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    spi.close()