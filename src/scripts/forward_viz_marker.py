#!/usr/bin/env python
import roslib
from visualization_msgs.msg import Marker
import rospy
import math

topic = "visualization_marker"
publisher = rospy.Publisher(topic, Marker, queue_size=10)
rospy.init_node('register')

marker = Marker()
marker.header.frame_id = "base_link";
marker.ns = "my_namespace";
marker.type = marker.SPHERE
marker.action = marker.ADD
marker.scale.x = 0.2
marker.scale.y = 0.2
marker.scale.z = 0.2
marker.color.a = 1.0
marker.color.r = 1.0
marker.color.g = 1.0
marker.color.b = 0.0
marker.pose.orientation.w = 1.0
marker.pose.position.x = 1h
marker.pose.position.y = 0
marker.pose.position.z = 0

r = rospy.Rate(10)
while not rospy.is_shutdown():
  publisher.publish(marker)
  r.sleep()