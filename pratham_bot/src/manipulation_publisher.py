#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
import sys
from select import select
import termios
import tty
# Initialize the node with rospy

pose_tilt = 0
pose_pan = 0

def getKey(timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    return key


def main():
    global pose_pan,pose_tilt
    rospy.init_node('manipulation_publisher')
    publisher = rospy.Publisher("/manipulation/servo_ctl",Float32MultiArray,queue_size=10)
    rospy.rate = 10
    msg = Float32MultiArray()
    while not rospy.is_shutdown():
        try :
            key = getKey(0.1)
        except rospy.ROSInterruptException:
            print("stopped")
        msg.data = [pose_pan,pose_tilt]
        publisher.publish(msg)
        if key == "w":
            if pose_tilt <  0.9:
                pose_tilt = pose_tilt + 0.1
            else :
                pose_tilt = 0.9
        elif key == "s":
            if pose_tilt > -0.9:
                pose_tilt = pose_tilt - 0.1
            else :
                pose_tilt = -0.9
        elif key == "a":
            if pose_pan > -0.9:
                pose_pan = pose_pan - 0.1
            else :
                pose_pan = -0.9
        elif key == "d":
            if pose_pan < 0.9:
                pose_pan = pose_pan + 0.1
            else :
                pose_pan = 0.9
        elif key == "x":
            pose_pan = 0
            pose_tilt = 0 

if __name__ == '__main__':
        try:
            main()
        except rospy.ROSInterruptException:
            pass
 