
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
# 주파수 설정(262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 392)
pwm.start(10)  # duty cycle (0~100)

# 도레미파솔라시도
melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 300, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262 ]
# melody = [262, 294, 330, 349, 392, 440, 494, 523]


try:
    for i in melody:
        pwm.ChangeFrequency(i)
        if i == 11 or i == 23:
            time.sleep(1)
        else:
            time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()
