import sys,tty,termios
import time
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO

#Note#
#Connect MA to BCM20
#Connect MB to BCM16
#Connect PWMA to BCM12
#Connect PWMB to BCM26

def main():
	import time
	GPIO.setwarnings(False)
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
# 	motorA.debug = True
# 	motorB.debug = True
	motorA.pwm = a_speed
	motorB.pwm = b_speed

	delay = 0.05
	s = get()
	
	while(1):
	if s == 0
	#stop if nothing pressed#
	    motorA.stop()
	    motorB.stop()   
	elif state == 1
	#going forward#
	    motorA.forward()
	    motorA.speed = 100
	    motorB.forward()
	    motorB.speed = 100
	
	elif s == -1
	#going backward#
	    motorA.backward()
	    motorA.speed = 100
	    motorB.backward()
	    motorB.speed = 100
	
	elif s == 2
	#rotate right#	
	    motorA.forward()
	    motorA.speed = 100
	    motorB.backward()
	    motorB.speed = 100
	
	elif s == 3
	#rotate left#
	    motorA.backward()
	    motorA.speed = 100
	    motorB.forward()
	    motorB.speed = 100

	else:
            destroy()

def destroy():
	motorA.stop()
	motorB.stop()

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

def get():
    inkey = _Getch()
    state = 0
    while(1):
	k=inkey()
    if k=='\x1b[A':
	state == 1
        print("forward")
    elif k=='\x1b[B':
	state == -1
        print("backward")
    elif k=='\x1b[C':
	state == 2
	print("right")
    elif k=='\x1b[D':
	state == 3
	print("left")
    else:
        print("not an arrow key!")
    return state
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()

# def main():
#     for i in range(0,20):
#         get()

# if __name__=='__main__':
#     main()
