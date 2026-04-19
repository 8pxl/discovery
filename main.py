import RPi.GPIO as GPIO
import time

IN1 = 23
IN2 = 24
IN3 = 27
IN4 = 22
ENA = 18
ENB = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# PWM setup (1kHz is standard for motors)
pwmA = GPIO.PWM(ENA, 1000)
pwmB = GPIO.PWM(ENB, 1000)

pwmA.start(0)
pwmB.start(0)

# ----- Motor functions -----

def forward(speed=60):
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)

def backward(speed=60):
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)

def stop():
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)

def turn_left(speed=60):
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)

def turn_right(speed=60):
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)

# ----- Test run -----
try:
    forward(70)
    time.sleep(2)

    turn_left(60)
    time.sleep(1)

    backward(50)
    time.sleep(2)

    stop()

finally:
    GPIO.cleanup()
