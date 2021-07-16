#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import sys

def radius(rad_value):
    pub = rospy.Publisher('/radius', Float32, queue_size=10)
    rospy.init_node('radius', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        radius_value= "The radius is %f" %rad_value
        rospy.loginfo(radius_value)
        pub.publish(rad_value)
        rate.sleep()

if __name__ == '__main__':
    try:
        radius(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass

