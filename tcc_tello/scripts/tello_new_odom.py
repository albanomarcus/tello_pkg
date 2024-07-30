#!/usr/bin/env python3

#imports
import rospy
from std_msgs.msg import String, Empty, Float32
from nav_msgs.msg import Odometry
from tello_driver.msg import TelloStatus

#criação de objetos
offset_odom = Odometry()
offset_z = Float32
last_pose = Odometry()

# status possíveis = ["desligado",
#                     "voando",
#                     "pousando"
#                     "decolando"]

status = "desligado"

# Funções:

# Função para alterar variáveis auxiliares após takeoff
def callback_takeoff(msg):
    global status
    if status == "desligado":
        rospy.sleep(4)
        status = "decolando"
    else: status = "voando"

# obtém o valor de offset do eixo Z do /tello/status
def callback_offset(msg):
    global offset_z
    offset_z = msg.height_m

# zera offset do eixo z ao pousar e ataliza variável auxiliar
def callback_land(msg):
    global status
    status = "pousando"


# recebe valores da odometria, realiza o tratamento e publica nova odometria
def callback_odom(msg, callback_args):
    publisher = callback_args
    new_odom = Odometry()

    global offset_odom, offset_z, status, last_pose
    
# executa a primeira vez para definir os offsets    
    if status == "decolando": 
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
        #print("*************************primeira vez*************************")
        status = "voando"

# executa o processo de pouso e remove "impulso" do gráfico.
    elif status == "pousando" and offset_z <0.3: 
        new_odom.pose.pose.position.x    =  msg.pose.pose.position.x - offset_odom.pose.pose.position.x
        new_odom.pose.pose.position.y    =  msg.pose.pose.position.y - offset_odom.pose.pose.position.y
        new_odom.pose.pose.position.z    =  0
        new_odom.pose.pose.orientation.w =  msg.pose.pose.orientation.w - offset_odom.pose.pose.orientation.w
        new_odom.pose.pose.orientation.x =  msg.pose.pose.orientation.x - offset_odom.pose.pose.orientation.x
        new_odom.pose.pose.orientation.y =  msg.pose.pose.orientation.y - offset_odom.pose.pose.orientation.y
        new_odom.pose.pose.orientation.z =  msg.pose.pose.orientation.z - offset_odom.pose.pose.orientation.z
        new_odom.twist.twist.linear.x    =  msg.twist.twist.linear.x -    offset_odom.twist.twist.linear.x
        new_odom.twist.twist.linear.y    =  msg.twist.twist.linear.y -    offset_odom.twist.twist.linear.y
        new_odom.twist.twist.linear.z    =  msg.twist.twist.linear.z -    offset_odom.twist.twist.linear.z
        new_odom.twist.twist.angular.x   =  msg.twist.twist.angular.x -   offset_odom.twist.twist.angular.x
        new_odom.twist.twist.angular.y   =  msg.twist.twist.angular.y -   offset_odom.twist.twist.angular.y
        new_odom.twist.twist.angular.z   =  msg.twist.twist.angular.z -   offset_odom.twist.twist.angular.z   
        #print("--------------------------------pousando--------------------------------")
        
        # armazena os ultimos valores de posição x, y e orientação (verificar necessidade de armazenar a orientação)
        last_pose.pose.pose.position.x = new_odom.pose.pose.position.x
        last_pose.pose.pose.position.y = new_odom.pose.pose.position.y
        last_pose.pose.pose.orientation.w = new_odom.pose.pose.orientation.w
        last_pose.pose.pose.orientation.x = new_odom.pose.pose.orientation.x
        last_pose.pose.pose.orientation.y = new_odom.pose.pose.orientation.y
        last_pose.pose.pose.orientation.z = new_odom.pose.pose.orientation.z
        publisher.publish(new_odom)
        status = "desligado"
    
# garante que o drone está pousado e parado na ultima posição de x e y
    elif status == "desligado": 
        new_odom.pose.pose.position.x    =  last_pose.pose.pose.position.x
        new_odom.pose.pose.position.y    =  last_pose.pose.pose.position.y
        new_odom.pose.pose.position.z    =  0
        new_odom.pose.pose.orientation.w =  last_pose.pose.pose.orientation.w
        new_odom.pose.pose.orientation.x =  last_pose.pose.pose.orientation.x
        new_odom.pose.pose.orientation.y =  last_pose.pose.pose.orientation.y
        new_odom.pose.pose.orientation.z =  last_pose.pose.pose.orientation.z
        new_odom.twist.twist.linear.x    =  0
        new_odom.twist.twist.linear.y    =  0
        new_odom.twist.twist.linear.z    =  0
        new_odom.twist.twist.angular.x   =  0
        new_odom.twist.twist.angular.y   =  0
        new_odom.twist.twist.angular.z   =  0   
        #print("--------------------------------desligado--------------------------------") 
        publisher.publish(new_odom)
        
# publica a odometria durante status = voando.
    else:
        new_odom.pose.pose.position.x    =  msg.pose.pose.position.x - offset_odom.pose.pose.position.x
        new_odom.pose.pose.position.y    =  msg.pose.pose.position.y - offset_odom.pose.pose.position.y
        new_odom.pose.pose.position.z    =  msg.pose.pose.position.z - offset_odom.pose.pose.position.z
        new_odom.pose.pose.orientation.w =  msg.pose.pose.orientation.w - offset_odom.pose.pose.orientation.w
        new_odom.pose.pose.orientation.x =  msg.pose.pose.orientation.x - offset_odom.pose.pose.orientation.x
        new_odom.pose.pose.orientation.y =  msg.pose.pose.orientation.y - offset_odom.pose.pose.orientation.y
        new_odom.pose.pose.orientation.z =  msg.pose.pose.orientation.z - offset_odom.pose.pose.orientation.z
        new_odom.twist.twist.linear.x    =  msg.twist.twist.linear.x - offset_odom.twist.twist.linear.x
        new_odom.twist.twist.linear.y    =  msg.twist.twist.linear.y - offset_odom.twist.twist.linear.y
        new_odom.twist.twist.linear.z    =  msg.twist.twist.linear.z - offset_odom.twist.twist.linear.z
        new_odom.twist.twist.angular.x   =  msg.twist.twist.angular.x - offset_odom.twist.twist.angular.x
        new_odom.twist.twist.angular.y   =  msg.twist.twist.angular.y - offset_odom.twist.twist.angular.y
        new_odom.twist.twist.angular.z   =  msg.twist.twist.angular.z - offset_odom.twist.twist.angular.z 
        publisher.publish(new_odom)

    #print (status)

def main():
# cria node para o script
    rospy.init_node('aux_odom')

# publicada a nova odometria
    pub_new_odom = rospy.Publisher('/tello/new_odom', Odometry, queue_size=1)

# recebe valores para cálculo da nova odometria    
    rospy.Subscriber('/tello/odom', Odometry, callback_odom, callback_args=(pub_new_odom))
    rospy.Subscriber('/tello/takeoff', Empty, callback_takeoff)
    rospy.Subscriber('/tello/land', Empty, callback_land)
    rospy.Subscriber('/tello/status', TelloStatus, callback_offset)
    rospy.spin()

if __name__ == '__main__':
    main()