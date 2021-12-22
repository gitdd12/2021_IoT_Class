import RPi.GPIO as GPIO
from flask import Flask, render_template

LED_PIN = 4
LED_PIN2 = 3
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def home():
    return render_template("led2.html")
    
@app.route("/led/<color>/<op>")
def led_on(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif op == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            return "RED LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "BLUE LED OFF"
            

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
