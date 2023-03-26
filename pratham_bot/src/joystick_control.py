#!/usr/bin/env python3

import rospy
# from motor_drivers_interface import basic_motor_driver 
from geometry_msgs.msg import Twist

def callback(msg):
    print(f"linear_x : {msg.linear.x} \n angular_z : {msg.angular.z}")
    take_action(msg.linear.x,msg.angular.z)

def take_action(X,Z):
    pass

def main():
    rospy.init_node("joystick_subscriber")
    rospy.Subscriber('/joystick',Twist,callback)
    rospy.spin()

if __name__ == '__main__':
    main()