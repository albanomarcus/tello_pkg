# Overview
These instructions are for installing a version of ORB-SLAM3 that is more ROS friendly, i.e., exposes data extracted from the camera in ROS topics. Tested in Ubuntu 20.04 and ROS Noetic.

# Basic resources
- [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3): original implementation. Has some optional integration with ROS for getting image data, but does not expose extracted SLAM/odom information back to ROS.
- [ORB-SLAM3 ROS wrapper](https://github.com/thien94/orb_slam3_ros_wrapper): A wrapper that can be used together with a stand-alone installation of the above to expose SLAM/odom data back to ROS.
- [ORB-SLAM3 ROS](https://github.com/thien94/orb_slam3_ros): a custom implementation of ORB-SLAM3 that is more ROS friendly. Sort of a combination of the above. This is the approach we'll be following.

# Installation
We mostly just follow the instructions at [ORB-SLAM3 ROS](https://github.com/thien94/orb_slam3_ros).

## Pre-requisites
```
# Eigen3 should already be installed, but if not:
sudo apt install libeigen3-dev
#
# Install Pangolin (this should take a while)
cd ~
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build && cd build
cmake ..
make
sudo make install
# If you wish you can now remove the downloaded and built files with:
# cd ~ && rm -r Pangolin
#
# OpenCV should already be installed
#
# Optionally install hector-trajectory-server
sudo apt install ros-noetic-hector-trajectory-server
```

## Catkin build and installation
```
cd ~/catkin_ws/src
git clone https://github.com/thien94/orb_slam3_ros.git
cd ../
catkin build
```
## Post installation
```
# Update installed libraries
sudo ldconfig
```

# Testing with bag for monocular camera
Download and unzip [this file](https://researchdata.ntu.edu.sg/api/access/datafile/68133) somewhere (e.g. the Downloads folder). WARNING: this is a large file (~4.2 Gb).
```
# In one terminal:
roslaunch orb_slam3_ros ntuviral_mono.launch
# In another terminal:
cd ~/Downloads/eee_01
rosbag play eee_01.bag -s 50 # The UAV starts moving at t~50s
```

Current pose of the camera with respect to `world` is published in `/orb_slam3/camera_pose` and the extracted PointCloud2 in `/orb_slam3/all_points`.
