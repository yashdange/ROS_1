#!/usr/bin/env python

from __future__ import print_function

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import sys
from part3.srv import *

def callback(data):
    rospy.loginfo("The radius is : %f", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/radius", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def angular_velocity_client(radius):
    rospy.wait_for_service('compute_ang_vel')
    try:
        add_two_ints = rospy.ServiceProxy('compute_ang_vel', service)
        resp1 = compute_ang_vel(radius)
        return resp1.angular_velocity
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
def move_turtle(lin_vel,ang_vel):
    rospy.init_node('turtlemove', anonymous = True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    vel = Twist()

    while True:
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        rospy.loginfo("linear value is: %f , Angular value is: %f", lin_vel, ang_vel)

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    listener()

    if len(sys.argv) == 3:
        radius = float(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("The angular velocity is:" %angular_velocity_client(radius))