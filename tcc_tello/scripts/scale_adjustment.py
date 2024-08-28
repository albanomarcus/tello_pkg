#!/usr/bin/env python3
"""
Utilizar esse script após ter o valor da escala definida.
"""
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import numpy as np


def scale_point_cloud(point_cloud, scale_factor):
    """
    Escala a nuvem de pontos pelo fator de escala fornecido.
    """
    points = np.array(list(pc2.read_points(point_cloud,field_names=("x", "y", "z"), skip_nans=True)))
    points[:, :3] *= scale_factor
    modified_points = [(x + 3.0, y, z + 1.0) for x, y, z in points]
    scaled_point_cloud = pc2.create_cloud(point_cloud.header, point_cloud.fields, modified_points)
    return scaled_point_cloud
    

def callback(point_cloud):
    """
    Callback para processar a nuvem de pontos recebida.
    """
    # Colocar o valor da escala calculada 
    scale_factor = 3.8455560957865367 #rosbag = subset.bag
    # scale_factor = 8.384939138795436 #rosbag = subset2.bag

    # Escalar a nuvem de pontos
    scaled_cloud = scale_point_cloud(point_cloud, scale_factor)
    pub.publish(scaled_cloud)

if __name__ == '__main__':
    rospy.init_node('scale_point_cloud_node', anonymous=True)
    rospy.Subscriber('/orb_slam3/all_points', PointCloud2, callback)
    pub = rospy.Publisher('/scaled_point_cloud', PointCloud2, queue_size=10)
    rospy.spin()
