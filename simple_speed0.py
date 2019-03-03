
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

	delay = 5

	motorA.forward()
    motorA.speed = 100
    motorB.forward()
    motorB.speed = 100
    time.sleep(delay)

	motorA.backward()
    motorA.speed = 100
	motorB.backward()
    motorB.speed = 100
    time.sleep(delay)

def destroy():
	motorA.stop()
	motorB.stop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()
