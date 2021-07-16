#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from part3.srv import *

def angular_velocity_client(radius):
    rospy.wait_for_service('compute_ang_vel')
    try:
        add_two_ints = rospy.ServiceProxy('compute_ang_vel', service)
        resp1 = compute_ang_vel(radius)
        return resp1.angular_velocity
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x,y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        radius = float(sys.argv[1])
       
    else:
        print(usage())
        sys.exit(1)
    print("The angular velocity is:"% angular_velocity_client(radius))