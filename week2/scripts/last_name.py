#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def last_name():
    pub = rospy.Publisher('surname', String)
    rospy.init_node('last_name', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        l_name = "Dange %s" % rospy.get_time()
        rospy.loginfo(l_name)
        pub.publish(l_name)
        rate.sleep()

if __name__ == '__main__':
    try:
        last_name()
    except rospy.ROSInterruptException:
        pass