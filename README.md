# Detecção e rastreamento de pessoas por veículos aéreos não tripulados

Ubuntu 20.04.5 LTS
ROS Noetic (Guia de instalação: https://github.com/albanomarcus/tcc_marcus_albano/blob/1f0949a211ce8cd17a3977a1c874e357e6c01436/ROS_Install.md)


## Inicializando
```
cd ~/catkin_ws/src
git clone https://github.com/albanomarcus/tcc_marcus_albano.git
```

## ORB-SLAM3
Seguir as instruções para instalação: https://github.com/albanomarcus/tcc_marcus_albano/blob/eee8ddd550129006369752c2910a9d61d42f0281/ORB-SLAM3_instructions.md

## Instalação Tello Driver 
Para realizar a comunicação com o drone real.

### Instalando pacotes dependentes
```
sudo apt install ros-noetic-cv-bridge
sudo apt install ros-noetic-image-transport
sudo apt install ros-noetic-camera-info-manager
sudo apt install ros-noetic-codec-image-transport
```
### Clonar pacotes adaptados para ROS Noetic
```
cd ~/catkin_ws
git clone https://github.com/albanomarcus/tello_driver.git
git clone https://github.com/albanomarcus/camera_info_manager_py.git
catkin build
source devel/setup.bash
```
## Executando

Terminal #1:
```
roslaunch tello_driver tello_node_2.launch
```
Terminal #2:
```
roslaunch orb_slam3_ros ntuviral_mono.launch
```
Terminal #3:
```
cd ~/catkin_ws/src/tcc_marcus_albano && python3 tello_control.py 
```


