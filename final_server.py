#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty

def handle_hi(request):
    rospy.loginfo("Hi, My name is 6352500251")
    return []

def final_server():
    rospy.init_node('final_server')
    rospy.Service('/hi', Empty, handle_hi)
    rospy.spin()

if __name__ == '__main__':
    final_server()
