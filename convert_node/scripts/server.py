#!/usr/bin/env python

from __future__ import print_function

from convert_node.srv import converttopolar,converttopolarResponse
import rospy
import math

def handle_conversion(req):
    # Converting cartesian to polar coordinate
# Calculating radius
    radius = math.sqrt( req.x * req.x + req.y * req.y )
# Calculating angle (theta) in radian
    theta = math.atan(req.y/req.x)
# Converting theta from radian to degree
    theta = 180 * theta/math.pi
    print(radius,theta)
    return converttopolarResponse(radius,theta)

def conversion_server():
    rospy.init_node('conversion_server')
    s = rospy.Service('conversion', converttopolar, handle_conversion)
    print("Ready to convert from cartesian to polar")
    rospy.spin()

if __name__ == "__main__":
    conversion_server()