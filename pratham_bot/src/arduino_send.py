#! /usr/bin/env python3

import rospy
from std_msgs.msg import UInt16
import sys
from select import select
import termios
import tty

def getKey(timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    return key

def main():
    rospy.init_node("Arduino_sender")
    publisher = rospy.Publisher("/led",UInt16,queue_size=10)
    rospy.rate = 10
    msg = UInt16()
    while not rospy.is_shutdown():
        try:
            key = getKey(0.1)
        except rospy.ROSInterruptException:
            print("Stopped")
        if key == "1":
            publisher.publish(1)
        elif key == "0":
            publisher.publish(0)
        elif key == "C":
            break

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass