import RPi.GPIO as GPIO

IN1 = 17
IN2 = 27
IN3 = 23
IN4 = 24
ENA = 18
ENB = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([IN1, IN2, IN3, IN4, ENA, ENB], GPIO.OUT)

pwmA = GPIO.PWM(ENA, 1000)
pwmB = GPIO.PWM(ENB, 1000)
pwmA.start(0)
pwmB.start(0)

def ileri(hiz=80):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwmA.ChangeDutyCycle(hiz)
    pwmB.ChangeDutyCycle(hiz)

def geri(hiz=80):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwmA.ChangeDutyCycle(hiz)
    pwmB.ChangeDutyCycle(hiz)

def sag(hiz=80):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwmA.ChangeDutyCycle(hiz)
    pwmB.ChangeDutyCycle(hiz)

def sol(hiz=80):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwmA.ChangeDutyCycle(hiz)
    pwmB.ChangeDutyCycle(hiz)

def dur():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
