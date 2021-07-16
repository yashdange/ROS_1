#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
import math 

from convert_node.srv import *

def convert_to_polar(x,y):
    rospy.wait_for_service('conversion')
    try:
        conversion = rospy.ServiceProxy('conversion', converttopolar)
        resp = conversion(x, y)
        return (resp.radius,resp.theta)
    except rospy.ServiceException as e:
        print("Service call failed: %s",e)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        resp1,resp2 = convert_to_polar(x,y)
    else:
        print(usage())
        sys.exit(1)
    print("Converting",(x, y))
    print('Conversion of {x},{y} is {resp1},{resp2}'.format(x=x,y=y,resp1=resp1,resp2=resp2))