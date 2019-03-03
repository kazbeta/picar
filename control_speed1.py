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

	delay = 0.1
	state = 0
	
	inkey = _Getch()
 	while 1:
 		k=inkey()
 		if k!='':break
#	while 1:
	if k=='\x1b[A':
		state = 1
		print(state)
	elif k=='\x1b[B':
		state = -1
		print(state)
	elif k=='\x1b[C':
		state = 2
	elif k=='\x1b[D':
		state = 3
	else:
		state = 0
#			break
#	i = 0
	while state == 1:
		print("forward")
		motorA.forward()
		motorA.speed = 100
		motorB.forward()
		motorB.speed = 100
		time.sleep(delay)
		k1=inkey()
 		if k1!='':break
	while state == -1:
		print("backward")
		motorA.backward()
		motorA.speed = 100
		motorB.backward()
		motorB.speed = 100
		time.sleep(delay)
		k1=inkey()
 		if k1!='':break
	while state == 2:
		print("right")
		motorA.forward()
		motorA.speed = 50
		motorB.backward()
		motorB.speed = 50
		time.sleep(delay)
		k1=inkey()
 		if k1!='':break
	while state == 3:
		print("forward")
		motorA.backward()
		motorA.speed = 50
		motorB.forward()
		motorB.speed = 50
		k1=inkey()
 		if k1!='':break
	#  		else:
	#  			motorA.stop()
	#  			motorB.stop()

	

def destroy():
	motorA.stop()
	motorB.stop()

#if __name__ == '__main__':
while True:
	try:
		main()
	except KeyboardInterrupt:
		destroy()
