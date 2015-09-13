#!/usr/bin/env python

""" Write a ROS node to move the bot in a (roughly) 1m x 1m square. """

import rospy
from geometry_msgs.msg import Twist, Vector3, Quaternion, Point
from nav_msgs.msg import Odometry

rospy.init_node('square')

def charge():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    twist = Twist()
    twist.linear.x = .1
    pub.publish(twist)
    rospy.sleep(10)

    twist.angular.z = 1
    pub.publish(twist)
    rospy.sleep(1.5);


r=rospy.Rate(10)

while not rospy.is_shutdown(): 
    charge()