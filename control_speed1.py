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
#        state = 0
#        if k!='':break
#    if k=='\x1b[A':
#        state = 1
##        print("up"),
##        print(state)
#    elif k=='\x1b[B':
#        state = -1
##        print("down")
##        print(state)
#    elif k=='\x1b[C':
#        state = 2
##        print("right")
##        print(state)
#    elif k=='\x1b[D':
#        state = 3
##        print("left")
##        print(state)

# def main():
#     for i in range(0,20):
#         get()

# if __name__=='__main__':
#     main()


#----------------------------------------#


import time
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO

def main():
	import time

    #Connect MA to BCM20
    #Connect MB to BCM16
    #Connect PWMA to BCM12
    #Connect PWMB to BCM26

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
	motorA.debug = True
	motorB.debug = True
	motorA.pwm = a_speed
	motorB.pwm = b_speed

	delay = 1
	state = 0

    	inkey = _Getch()
    	while 1:
        	k=inkey()
        	if k!='':break
		if k=='\x1b[A':
			state = 1
		elif k=='\x1b[B':
			state = -1
		elif k=='\x1b[C':
			state = 2
		elif k=='\x1b[D':
			state = 3
			
		if state == 1:
			print("forward")
			motorA.forward()
			motorA.speed = 100
			motorB.forward()
			motorB.speed = 100
#			time.sleep(delay)
		elif state == -1:
			print("backward")
			motorA.backward()
			motorA.speed = 100
			motorB.backward()
			motorB.speed = 100
#			time.sleep(delay)
		elif state == 2:
			print("right")
			motorA.forward()
			motorA.speed = 100
			motorB.backward()
			motorB.speed = 100
#			time.sleep(delay)
		elif state == 3:
			print("forward")
			motorA.backward()
			motorA.speed = 100
			motorB.forward()
			motorB.speed = 100
#			time.sleep(delay)
		else:
			motorA.stop()
			motorB.stop()

def destroy():
	motorA.stop()
	motorB.stop()

#if __name__ == '__main__':
while True:
	try:
		main()
	except KeyboardInterrupt:
		destroy()
