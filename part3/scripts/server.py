#!/usr/bin/env python

from __future__ import print_function

from part3.srv import service,serviceResponse
import rospy

def calculate_angular_velocity(req):
    print("The Angular Velocity is: %f" %(1/req.radius))
    return serviceResponse(angular_velocity)

def angular_velocity_server():
    rospy.init_node('angular_velocity_server')
    s = rospy.Service('compute_ang_vel', service, calculate_angular_velocity)
    print("Ready to calculate angular velocity")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()