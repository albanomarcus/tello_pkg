#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Empty, Float32
from nav_msgs.msg import Odometry
from tello_driver.msg import TelloStatus

offset_odom = Odometry()
land_position = Odometry()
offset_z = Float32

first_time = False
land = True
aux_land = False

takeoff_count = 0
takingoff = False

def callback_takeoff(msg):
    global first_time, land, takeoff_count, takingoff
    land = False
    if takeoff_count == 0:
        rospy.sleep(4)
        first_time = True
        takeoff_count = 1
    else: takingoff = True


def callback_offset(msg):
    global offset_z
    offset_z = msg.height_m

def callback_land(msg):
    global land, offset_odom, aux_land
    aux_land = True
    rospy.sleep(5)
    offset_odom.pose.pose.position.z     =   0
    land = True

def callback_odom(msg, callback_args):
    publisher = callback_args
    odom_msg = Odometry()
    global offset_odom, first_time, offset_z, takingoff, aux_land, land_position
    
    if first_time == True and takingoff == False and land == False: #FIRST TIME =
        offset_odom.pose.pose.position.x     =  msg.pose.pose.position.x
        offset_odom.pose.pose.position.y     =  msg.pose.pose.position.y
        offset_odom.pose.pose.position.z     =  msg.pose.pose.position.z - offset_z
        offset_odom.pose.pose.orientation.w  =  msg.pose.pose.orientation.w
        offset_odom.pose.pose.orientation.x  =  msg.pose.pose.orientation.x
        offset_odom.pose.pose.orientation.y  =  msg.pose.pose.orientation.y
        offset_odom.pose.pose.orientation.z  =  msg.pose.pose.orientation.z
        offset_odom.twist.twist.linear.x     =  msg.twist.twist.linear.x
        offset_odom.twist.twist.linear.y     =  msg.twist.twist.linear.y
        offset_odom.twist.twist.linear.z     =  msg.twist.twist.linear.z
        offset_odom.twist.twist.angular.x    =  msg.twist.twist.angular.x
        offset_odom.twist.twist.angular.y    =  msg.twist.twist.angular.y
        offset_odom.twist.twist.angular.z    =  msg.twist.twist.angular.z
        first_time = False
        print("primeira vez")
        publisher.publish(odom_msg)

    elif first_time == False and takingoff == True and land == False: #TAKING OFF = TRUE
        offset_odom.pose.pose.position.x     =  offset_odom.pose.pose.position.x
        offset_odom.pose.pose.position.y     =  offset_odom.pose.pose.position.y
        offset_odom.pose.pose.position.z     =  msg.pose.pose.position.z - offset_z
        offset_odom.pose.pose.orientation.w  =  offset_odom.pose.pose.orientation.w
        offset_odom.pose.pose.orientation.x  =  offset_odom.pose.pose.orientation.x
        offset_odom.pose.pose.orientation.y  =  offset_odom.pose.pose.orientation.y
        offset_odom.pose.pose.orientation.z  =  offset_odom.pose.pose.orientation.z
        offset_odom.twist.twist.linear.x     =  offset_odom.twist.twist.linear.x
        offset_odom.twist.twist.linear.y     =  offset_odom.twist.twist.linear.y
        offset_odom.twist.twist.linear.z     =  offset_odom.twist.twist.linear.z
        offset_odom.twist.twist.angular.x    =  offset_odom.twist.twist.angular.x
        offset_odom.twist.twist.angular.y    =  offset_odom.twist.twist.angular.y
        offset_odom.twist.twist.angular.z    =  offset_odom.twist.twist.angular.z
        takingoff = False
        print("decolando")
        publisher.publish(odom_msg)

    elif first_time == False and takingoff == False and land == True:  #LAND = TRUE
        odom_msg.pose.pose.position.x    =  land_position.pose.pose.position.x
        odom_msg.pose.pose.position.y    =  land_position.pose.pose.position.y
        odom_msg.pose.pose.position.z    =  0
        odom_msg.pose.pose.orientation.w =  land_position.pose.pose.orientation.w
        odom_msg.pose.pose.orientation.x =  land_position.pose.pose.orientation.x
        odom_msg.pose.pose.orientation.y =  land_position.pose.pose.orientation.y
        odom_msg.pose.pose.orientation.z =  land_position.pose.pose.orientation.z
        odom_msg.twist.twist.linear.x    =  msg.twist.twist.linear.x -    offset_odom.twist.twist.linear.x
        odom_msg.twist.twist.linear.y    =  msg.twist.twist.linear.y -    offset_odom.twist.twist.linear.y
        odom_msg.twist.twist.linear.z    =  msg.twist.twist.linear.z -    offset_odom.twist.twist.linear.z
        odom_msg.twist.twist.angular.x   =  msg.twist.twist.angular.x -   offset_odom.twist.twist.angular.x
        odom_msg.twist.twist.angular.y   =  msg.twist.twist.angular.y -   offset_odom.twist.twist.angular.y
        odom_msg.twist.twist.angular.z   =  msg.twist.twist.angular.z -   offset_odom.twist.twist.angular.z   
        print("pousando") 
        publisher.publish(odom_msg)
    
    #TESTAR SE PRECISA INSERIR UMA NOVA CONDIÇÃO PARA QUANDO POUSAR E LEVANTAR VOO DE NOVO
    else:  
        odom_msg.pose.pose.position.x    =  msg.pose.pose.position.x - offset_odom.pose.pose.position.x
        odom_msg.pose.pose.position.y    =  msg.pose.pose.position.y - offset_odom.pose.pose.position.y
        odom_msg.pose.pose.position.z    =  msg.pose.pose.position.z - offset_odom.pose.pose.position.z
        odom_msg.pose.pose.orientation.w =  msg.pose.pose.orientation.w - offset_odom.pose.pose.orientation.w
        odom_msg.pose.pose.orientation.x =  msg.pose.pose.orientation.x - offset_odom.pose.pose.orientation.x
        odom_msg.pose.pose.orientation.y =  msg.pose.pose.orientation.y - offset_odom.pose.pose.orientation.y
        odom_msg.pose.pose.orientation.z =  msg.pose.pose.orientation.z - offset_odom.pose.pose.orientation.z
        odom_msg.twist.twist.linear.x    =  msg.twist.twist.linear.x - offset_odom.twist.twist.linear.x
        odom_msg.twist.twist.linear.y    =  msg.twist.twist.linear.y - offset_odom.twist.twist.linear.y
        odom_msg.twist.twist.linear.z    =  msg.twist.twist.linear.z - offset_odom.twist.twist.linear.z
        odom_msg.twist.twist.angular.x   =  msg.twist.twist.angular.x - offset_odom.twist.twist.angular.x
        odom_msg.twist.twist.angular.y   =  msg.twist.twist.angular.y - offset_odom.twist.twist.angular.y
        odom_msg.twist.twist.angular.z   =  msg.twist.twist.angular.z - offset_odom.twist.twist.angular.z 
        print("rodando no else")
        if aux_land == True:
                land_position.pose.pose.position.x = odom_msg.pose.pose.position.x
                land_position.pose.pose.position.y = odom_msg.pose.pose.position.y
                land_position.pose.pose.orientation.w = odom_msg.pose.pose.orientation.w
                land_position.pose.pose.orientation.x = odom_msg.pose.pose.orientation.x
                land_position.pose.pose.orientation.y = odom_msg.pose.pose.orientation.y
                land_position.pose.pose.orientation.z = odom_msg.pose.pose.orientation.z
                aux_land = False
                print("posicção salva!!!!!!!!!!!!!!!!!!!!!!!!!!")
        publisher.publish(odom_msg)

def main():
    rospy.init_node('aux_odom')

    pub_new_odom = rospy.Publisher('/tello/new_odom', Odometry, queue_size=1)
    
    rospy.Subscriber('/tello/odom', Odometry, callback_odom, callback_args=(pub_new_odom))
    rospy.Subscriber('/tello/takeoff', Empty, callback_takeoff)
    rospy.Subscriber('/tello/land', Empty, callback_land)
    rospy.Subscriber('/tello/status', TelloStatus, callback_offset)
    rospy.spin()

if __name__ == '__main__':
    main()