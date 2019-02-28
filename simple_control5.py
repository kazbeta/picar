import time
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO


import sys,tty,termios
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

            #def get():
#    inkey = _Getch()
#    while(1):
#        k=inkey()
#        if k!='':break
#    if k=='\x1b[A':
#            print("up")
#    elif k=='\x1b[B':
#            print("down")
#    elif k=='\x1b[C':
#            print("right")
#    elif k=='\x1b[D':
#            print("left")
#    elif k==',':
#            print("<")
#    elif k=='.':
#            print(">")
#    else:
#            print("not an arrow key!")

def main():
    import time
    
    print "********************************************"
    print "*                                          *"
    print "*           SunFounder TB6612              *"
    print "*                                          *"
    print "*          Connect MA to BCM17 -> 20            *"
    print "*          Connect MB to BCM18 -> 16           *"
    print "*         Connect PWMA to BCM27 -> 12          *"
    print "*         Connect PWMB to BCM22 -> 26          *"
    print "*                                          *"
    print "********************************************"
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
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b[A':
        print("forward")
        motorA.forward()
        motorA.speed =100
        motor.forward()
        motorB.speed =100
    elif k=='\x1b[B':
        print("backward")
        motorA.backward()
        motorA.speed = 100
        motor.backward()
        motorB.speed = 100
    elif k=='\x1b[C':
        print("right")
        motorA.backward()
        motorA.speed = 100
        motor.forward()
        motorB.speed = 100
    elif k=='\x1b[D':
        print("left")
        motorA.forward()
        motorA.speed = 100
        motor.backward()
        motorB.speed = 100
#    elif k==',':
#        print("<")
#    elif k=='.':
#        print(">")
    else:
        print("not an arrow key!")


#    delay = 0.05
#
#    motorA.forward()
#    for i in range(0, 101):
#        motorA.speed = i
#        time.sleep(delay)
#    for i in range(100, -1, -1):
#        motorA.speed = i
#        time.sleep(delay)
#
#    motorA.backward()
#    for i in range(0, 101):
#        motorA.speed = i
#        time.sleep(delay)
#    for i in range(100, -1, -1):
#        motorA.speed = i
#        time.sleep(delay)
#
#    motorB.forward()
#    for i in range(0, 101):
#        motorB.speed = i
#        time.sleep(delay)
#    for i in range(100, -1, -1):
#        motorB.speed = i
#        time.sleep(delay)
#
#    motorB.backward()
#    for i in range(0, 101):
#        motorB.speed = i
#        time.sleep(delay)
#    for i in range(100, -1, -1):
#        motorB.speed = i
#        time.sleep(delay)

def destroy():
    motorA.stop()
    motorB.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
