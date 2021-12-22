import RPi.GPIO as GPIO
from flask import Flask

LED_PIN = 4
LED_PIN2 = 3
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p> 
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="./led/blue/on">BLUE LED ON</a>
        <a href="./led/blue/off">BLUE LED OFF</a>
    '''
    
@app.route("/led/<color>/<op>")
def led_on(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return '''
                <p>RED LED ON</p> 
                <a href="/">Go Home</a>
                '''
        elif op == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            return '''
                <p>RED LED OFF</p> 
                <a href="/">Go Home</a>
                '''
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return '''
                <p>BLUE LED ON</p> 
                <a href="/">Go Home</a>
                '''
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return '''
              <p>BLUE LED OFF</p> 
              <a href="/">Go Home</a>
                '''
            

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
