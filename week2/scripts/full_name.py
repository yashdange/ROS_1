#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def full_name():


    rospy.init_node('full_name', anonymous=True)

    rospy.Subscriber("name", String, callback)
    rospy.Subscriber("surname", String, callback)

    rospy.spin()

if __name__ == '__main__':
    full_name()