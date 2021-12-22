import RPi.GPIO as GPIO
from flask import Flask, render_template

LED_PIN = 4

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
@app.route("/")
def home():
    return render_template("led.html")
    
@app.route("/led/<op>")
def led_on(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    else:
        return "URL ERROR"
# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()