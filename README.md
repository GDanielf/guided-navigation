# guided-navigation

## Ubuntu Version : 22.02.04 LTS (Jammy)
https://www.releases.ubuntu.com/jammy/

## ROS 2 Humble Hawksbill
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

## Gazebo Fortress
https://gazebosim.org/docs/fortress/install_ubuntu/

### ROS2 and Gazebo Bridge communication: 
sudo apt-get install ros-humble-ros-ign-bridge

https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_bridge

### Colocar isso no bashrc:
export GZ_SIM_RESOURCE_PATH=/home/gdaniel/mestrado_ws/models

### Iniciar o mundo no gazebo:
> ign gazebo ~/mestrado_ws/world/camera_world.sdf

## Como conectar cada camera com o ROS2:

### Checar os topicos do gazebo:
> ign topic -l

### 1a camera:
Em outro terminal:
Fazer a bridge entre o topico da camera 1 do gazebo com ROS2:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/image@sensor_msgs/msg/Image@gz.msgs.Image --ros-args --remap __node:=camera_1_bridge

### 2a camera:
Em outro terminal:
Fazer a bridge entre o topico da camera 2 do gazebo com ROS2:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera_1/link/link_1/sensor/camera_sensor_1/image@sensor_msgs/msg/Image@gz.msgs.Image --ros-args --remap __node:=camera_2_bridge

### 3a camera:
Em outro terminal:
Fazer a bridge entre o topico da camera 3 do gazebo com ROS2:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera_2/link/link_2/sensor/camera_sensor_2/image@sensor_msgs/msg/Image@gz.msgs.Image --ros-args --remap __node:=camera_3_bridge

### Visualizar no rviz:
> ros2 run rqt_image_view rqt_image_view /world/empty/model/rgbd_camera_1/link/link_1/sensor/camera_sensor_1/image
