import RPi.GPIO as GPIO
from flask import Flask

LED_PIN = 4

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p> 
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''
    
@app.route("/led/<op>")
def led_on(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>LED ON</p> 
            <a href="/">Go Home</a>
            '''
    elif op == "off":
        return '''
            <p>LED OFF</p> 
            <a href="/">Go Home</a>
            '''
    

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")
