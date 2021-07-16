#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def first_name():
    pub = rospy.Publisher('name', String)
    rospy.init_node('first_name', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        f_name = "Yash %s" % rospy.get_time()
        rospy.loginfo(f_name)
        pub.publish(f_name)
        rate.sleep()

if __name__ == '__main__':
    try:
        first_name()
    except rospy.ROSInterruptException:
        pass