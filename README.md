# Detecção e rastreamento de pessoas por veículos aéreos não tripulados

## Sistema Operacional utilizado
Ubuntu 20.04.5 LTS

## Guia de instalação ROS Noetic (wiki.ros.org/noetic/Installarion/Ubuntu)

### Configurar o computador para que ele aceite softwares de packages.ros.org

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

### Configurar chaves
```
sudo apt install curl # caso não tenha curl instalado
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -	
```

### Instalando ROS Noetic
Verificar se o sistema está atualizado
```
sudo apt update
```	

### Instalar a versão Full do ROS Noetic
```
sudo apt install ros-noetic-desktop-full
```

### Configurando o ambiente (modificando o bash de forma automática)	
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Adicionando as dependências e ferramentas 
```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```	
### Inicializar rosdep
```
sudo rosdep init
rosdep update
```

## Criando um ROS Workspace
### Criar um catkin workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/		
catkin_make
```		

### Criando um package
```
cd ~/catkin_ws/src
catkin_create_pkg tcc_marcus_albano std_msgs rospy roscpp
```

### Após a criação executar:
```
cd ~/catkin_ws/ 		
catkin_make
. ~/catkin_ws/devel/setup.bash
```

## Instalando pacotes necessários para execução do gazebo com drone - hector_quadrotor (baseado em: https://github.com/RAFALAMAO/hector-quadrotor-noetic)
Antes de instalar o hector_quadrotor_noetic, é necessário instalar outros 2 pacotes.
 - unique_identifier: 
```
git clone https://github.com/ros-geographic-info/unique_identifier.git
``` 

 - geographic_info: 
```
git clone https://github.com/ros-geographic-info/geographic_info.git
```

Executar o build:

```
cd ~/catkin_ws && catkin_make
```

Então clonar o hector_quadrotor_noetic:

```
cd src
git clone https://github.com/RAFALAMAO/hector_quadrotor_noetic.git
```

Executar o build novamente:

```
cd ~/catkin_ws && catkin_make
```

## Instalando e executando o pacote do TCC no ROS.
```
cd src
git clone https://github.com/albanomarcus/TCC_Marcus_Albano.git
```
Executar o build novamente:

```
cd ~/catkin_ws && catkin_make
```

### Executando o projeto
Esse launch file iniciará o gazebo com o DJI Tello em um mundo vazio.
```
roslaunch tcc_marcus_albano spawn_tello_drone.launch
```

### Tele operação
O comando a seguir abrirá uma inteface de controles via botões. Essa interface será refeita futuramente.
```
rosrun hector_ui ui_hector_quad.py
```
