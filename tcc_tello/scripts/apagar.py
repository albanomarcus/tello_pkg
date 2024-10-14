#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def twist_callback(msg):
    # Cria uma nova mensagem Twist
    new_twist = Twist()

    # Inverte os valores de linear.x e linear.y
    new_twist.linear.x = msg.linear.y
    new_twist.linear.y = -msg.linear.x
    new_twist.linear.z = msg.linear.z  # mantém o valor de z

    # Mantém os valores da rotação angular
    new_twist.angular = msg.angular

    # Publica a nova mensagem Twist com os valores invertidos
    pub.publish(new_twist)

if __name__ == '__main__':
    # Inicializa o nó ROS
    rospy.init_node('twist_inverter')

    # Cria o publicador para o novo tópico
    pub = rospy.Publisher('/tello/cmd_vel2', Twist, queue_size=10)

    # Cria o assinante que recebe as mensagens Twist
    rospy.Subscriber('/tello/cmd_vel', Twist, twist_callback)

    # Mantém o nó rodando
    rospy.spin()