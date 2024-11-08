# Instalação ROS Noetic

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
### Instalando Catkin_tools para usar catkin build (opcional, caso não deseje utilizar o comando catkin build, substituir pelo comando catkin_make nas próximas etapas)
```
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-catkin-tools
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
catkin build
```		

### Criando um package
```
cd ~/catkin_ws/src
catkin_create_pkg tcc_marcus_albano std_msgs rospy roscpp
```

### Após a criação executar:
```
cd ~/catkin_ws/ 		
catkin build
. ~/catkin_ws/devel/setup.bash
```
