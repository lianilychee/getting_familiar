#!/usr/bin/env python

""" Publish a message of type visualization_messages/Marker that publishes 10x / second """

from visualization_msgs.msg import Marker
from std_msgs.msg import Header
import rospy
import math

topic = "/viz_marker"
publisher = rospy.Publisher(topic, Marker, queue_size=10)
rospy.init_node('register')

marker = Marker()
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
marker.pose.position.x = math.cos(count / 50.0)
marker.pose.position.y = math.cos(count / 40.0) 
marker.pose.position.z = math.cos(count / 30.0) 

r = rospy.Rate(10)
while not rospy.is_shutdown():
  publisher.publish(marker)
  r.sleep()

# rospy.init_node('visualization_message')


# pub = rospy.Publisher('/my_point', PointStamped, queue_size=10)

# r = rospy.Rate(10)
# while not rospy.is_shutdown():
# 	r.sleep()




# point_msg = Point(x=1.0, y=2.0)
# header_msg = Header(stamp=rospy.Time.now(), frame_id='odom')

# point_stamped_msg = PointStamped(header=header_msg,
# 								 point=point_msg)

# pub = rospy.Publisher("/my_point", PointStamped, queue_size=10)

# r = rospy.Rate(10)
# while not rospy.is_shutdown():
# 	pub.publish(point_stamped_msg)
# 	r.sleep()