#!/usr/bin/env python

import rospy
from sample_py.msg import dso_message

def callback(msg):
    # rospy.loginfo("I heard: seq = [%s], count = [%d]" % (msg.header.seq, msg.header.stamp))
    print msg

def subscriber():
    rospy.init_node('sample_py_subscriber', anonymous=True)
    rospy.Subscriber('/test/vodom', dso_message, callback)
    rospy.spin()

if __name__ == "__main__":
    subscriber()