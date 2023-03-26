#	ENA,	IA1,	IA2,	ENB,	IB3,	IB4
#	1		1		0		1		1		0		- FORWARD - CLOCKWISE * 2
#  	1		0		1		1		0		1		- BACKWARD - ANTICLOCKWISE * 2
#	1		1		0		1		0		1		- ROTATE RIGHT
#   1		0		1		1		1		0     	- ROTATE LEFT
#   1       0       0       1       0       0       - STOP
# 	1		1		0		1		0		0		- TURN - RIGHT
#  	1		0		0		1		1		0		- TURN - LEFT
# 	1		0		0		1		0		1		- TURN - RIGHT - inv
#  	1	    0		1		1		0		0		- TURN - LEFT  - inv


import RPi.GPIO as GPIO
GPIO.setwarnings("False")
GPIO.setmode(GPIO.BOARD)

RIGHT_MOTOR_IA1 = 16
RIGHT_MOTOR_IA2 = 20
LEFT_MOTOR_IB3 = 19
LEFT_MOTOR_IB4 = 26

GPIO.setup(RIGHT_MOTOR_IA1,GPIO.OUT)
GPIO.output(RIGHT_MOTOR_IA1,GPIO.LOW)
GPIO.setup(RIGHT_MOTOR_IA2,GPIO.OUT)
GPIO.output(RIGHT_MOTOR_IA2,GPIO.LOW)
GPIO.setup(LEFT_MOTOR_IB3,GPIO.OUT)
GPIO.output(LEFT_MOTOR_IB3,GPIO.LOW)
GPIO.setup(LEFT_MOTOR_IB4,GPIO.OUT)
GPIO.output(LEFT_MOTOR_IB4,GPIO.LOW)

def forward(speed):
    print("Forwarding")
    GPIO.output(RIGHT_MOTOR_IA1,GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_IA2,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB3,GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_IB4,GPIO.LOW)

def backward(speed):
    print("Backwarding")
    GPIO.output(RIGHT_MOTOR_IA1,GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_IA2,GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_IB3,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB4,GPIO.HIGH)

def right_rotate(speed):
    print("right_rotate")
    GPIO.output(RIGHT_MOTOR_IA1,GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_IA2,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB3,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB4,GPIO.HIGH)

def left_rotate(speed):
    print("left_rotate")
    GPIO.output(RIGHT_MOTOR_IA1,GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_IA2,GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_IB3,GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_IB4,GPIO.LOW)
    
def stop(speed):
    print("stop")
    GPIO.output(RIGHT_MOTOR_IA1,GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_IA2,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB3,GPIO.LOW)
    GPIO.output(LEFT_MOTOR_IB4,GPIO.LOW)







