import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

FORWARD = "FORWARD"
LEFT_TURN = "LEFT"
RIGHT_TURN = "RIGHT"
DIRECTION_AFTER_RED = RIGHT_TURN
DIRECTION_AFTER_GREEN = LEFT_TURN

IN1, IN2 = 17, 27
ENA = 13
TRIG, ECHO = 5, 6

GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1, IN2, ENA, TRIG], GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

def motor_ileri(hiz=70):
    GPIO.output(IN1, True); GPIO.output(IN2, False)
    pwm.ChangeDutyCycle(hiz)

def motor_dur():
    GPIO.output(IN1, False); GPIO.output(IN2, False)
    pwm.ChangeDutyCycle(0)

def motor_sola_don(hiz=60):
    GPIO.output(IN1, False); GPIO.output(IN2, True)
    pwm.ChangeDutyCycle(hiz)

def motor_saga_don(hiz=60):
    GPIO.output(IN1, True); GPIO.output(IN2, False)
    pwm.ChangeDutyCycle(hiz)

def mesafe_olc():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    baslangic = time.time()
    while GPIO.input(ECHO) == 0:
        baslangic = time.time()
    while GPIO.input(ECHO) == 1:
        bitis = time.time()
    return (bitis - baslangic) * 34300 / 2

cap = cv2.VideoCapture(0)
tur = 0

try:
    while tur < 3:
        ret, frame = cap.read()
        if not ret:
            continue
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv, (0,120,70), (10,255,255)) + cv2.inRange(hsv, (170,120,70), (180,255,255))
        green_mask = cv2.inRange(hsv, (40,50,50), (80,255,255))
        red_area = cv2.countNonZero(red_mask)
        green_area = cv2.countNonZero(green_mask)
        mesafe = mesafe_olc()
        if red_area > 1000:
            motor_saga_don(); time.sleep(0.5); motor_ileri(); time.sleep(1)
        elif green_area > 1000:
            motor_sola_don(); time.sleep(0.5); motor_ileri(); time.sleep(1)
        elif mesafe <= 50:
            motor_sola_don(); time.sleep(0.5)
        else:
            motor_ileri(); time.sleep(1); tur += 1
        motor_dur(); time.sleep(0.3)
except KeyboardInterrupt:
    pass
cap.release()
motor_dur()
GPIO.cleanup()
