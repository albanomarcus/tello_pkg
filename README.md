# Utilização do veículo aéreo não tripulado Tello para mapeamento, navegação autônoma, detecção e rastreamento de pessoas 

Ubuntu 20.04.5 LTS

ROS Noetic - [Guia de instalação](https://github.com/albanomarcus/tcc_marcus_albano/blob/1f0949a211ce8cd17a3977a1c874e357e6c01436/ROS_Install.md)

## Inicializando
```
cd ~/catkin_ws/src
git clone https://github.com/albanomarcus/tcc_marcus_albano.git
```

## ORB-SLAM3
Para instalar, seguir o [Guia de instalação](https://github.com/albanomarcus/tcc_marcus_albano/blob/eee8ddd550129006369752c2910a9d61d42f0281/ORB-SLAM3_instructions.md)

## Instalação Tello Driver 
Para realizar a comunicação com o drone real.

### Instalando pacotes dependentes
```
sudo apt install ros-noetic-cv-bridge
sudo apt install liburdfdom-tools #gerar arquivos pdf do urdf (Opcional)
```
### Clonar pacotes adaptados para ROS Noetic
```
cd ~/catkin_ws
git clone --recursive https://github.com/albanomarcus/tello_driver.git
git clone https://github.com/albanomarcus/camera_info_manager_py.git
catkin build && source devel/setup.bash
```
## Executando
Para inicializar os tópicos responsáveis pela comunicação com o Tello: 
Terminal #1: 
```
roslaunch tcc_tello tello_node.launch
```
Para inicializar o OrbSlam3:
Terminal #2:
```
roslaunch tcc_tello tello_orb_slam.launch
```
Para teleoperar o Tello utilizando o teclado do computador:
Terminal #3:
```
roslaunch tcc_tello tello_control.launch
```
## Instalação pacotes para executar a simulação

### Clonar pacotes adaptados do Hector Quadrotor para ROS Noetic

```
git clone https://github.com/RAFALAMAO/hector_quadrotor_noetic.git


catkin build && source devel/setup.bash
```
## Executando
Para inicializar os tópicos responsáveis pela simulação do Tello: 
Terminal #1: 
```
roslaunch tcc_tello gazebo_tello_node.launch
```
Para inicializar o OrbSlam3:
Terminal #2:
```
roslaunch tcc_tello tello_orb_slam.launch
```
Para teleoperar o Tello utilizando o teclado do computador:
Terminal #3:
```
roslaunch tcc_tello gazebo_tello_control.launch
```

## Plotando gráficos com PlotJuggler

Para instalar:
```
sudo apt install ros-noetic-plotjuggler-ros
```

Executar:
```
rosrun plotjuggler plotjuggler
```

## Mapeamento

### Aplicando Escala
executar roslaunch gazebo_point_cloud_manipulation.launch apenas quando a execução da rosbag estiver sendo finalizada.
### Octomap
sudo apt install ros-noetic-octomap-*

## Navegação Autônoma

sudo apt install ros-noetic-move-base

sudo apt-get install ros-noetic-global-planner
## Envio de E-mails

## Rosbridge para envio de sinais via Web Socket
sudo apt-get install ros-noetic-rosbridge-suite



### TO DO:
j

Criar novo mapa para simulação e remover os outros que não serão utilizados.

Arrumar esse readme

colocar videos, imagens, etc...

mudar nome do pacote

mudar nome do repositório

adicionar controle de altura pra o drone real









