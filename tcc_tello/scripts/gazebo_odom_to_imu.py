#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

def odom_callback(msg):
    imu_msg = Imu()
    
    # Copiar timestamp e frame_id
    imu_msg.header.stamp = msg.header.stamp
    imu_msg.header.frame_id = msg.header.frame_id
    
    # Copiar orientação
    imu_msg.orientation = msg.pose.pose.orientation
    
    # Copiar velocidades angulares
    imu_msg.angular_velocity = msg.twist.twist.angular
    
    # Copiar acelerações lineares
    imu_msg.linear_acceleration = msg.twist.twist.linear
    
    imu_pub.publish(imu_msg)

rospy.init_node('/odom_to_imu_converter')
imu_pub = rospy.Publisher('/new_imu', Imu, queue_size=10)
rospy.Subscriber('/ground_truth/state', Odometry, odom_callback)

rospy.spin()