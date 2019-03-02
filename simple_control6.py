import sys,tty,termios
import time
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO


#motor GPIO assignment#
#Connect MA to BCM20
#Connect MB to BCM16
#Connect PWMA to BCM12
#Connect PWMB to BCM26

#------------------------------#

def destroy():
    motorA.stop()
    motorB.stop()

#Get keyboard input#
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#------------------------------#

#Control#
def test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup((12, 26), GPIO.OUT)
    a = GPIO.PWM(12, 60)
    b = GPIO.PWM(26, 60)
    a.start(0)
    b.start(0)
    
    def a_speed(value):
        a.ChangeDutyCycle(value)
    
    def b_speed(value):
        b.ChangeDutyCycle(value)
    
    motorA = TB6612.Motor(20)
    motorB = TB6612.Motor(16)
#    motorA.debug = True
#    motorB.debug = True
    motorA.pwm = a_speed
    motorB.pwm = b_speed

    inkey = _Getch()
    
    if inkey=='\x1b[A':
        print("forward")
        motorA.forward()
        motorA.speed = 100
        motorB.forward()
        motorB.speed = 100

    elif inkey=='\x1b[B':
        print("backward")
        motorA.backward()
        motorA.speed = 100
        motorB.backward()
        motorB.speed = 100

    elif inkey=='\x1b[C':
        print("right")
        motorA.forward()
        motorA.speed = 100
        motorB.backward()
        motorB.speed = 100

    elif inkey=='\x1b[D':
        print("left")
        motorA.backward()
        motorA.speed = 100
        motorB.forward()
        motorB.speed = 100

#------------------------------#

#main part#
#if __name__ == '__main__':
while True:
    try:
        test()
    except KeyboardInterrupt:
        destroy()
