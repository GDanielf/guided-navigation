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

### Comandos para teste:
> ign gazebo ~/mestrado_ws/world/camera_world.sdf

## Como conectar cada camera com o ROS2:

### Checar os topicos do gazebo:
> ign topic -l

### 1a camera:
Em outro terminal:
Visualizar a imagem da camera:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/image@sensor_msgs/msg/Image@gz.msgs.Image

### 2a camera:
Em outro terminal:
Visualizar a imagem da camera:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera_1/link/link_1/sensor/camera_sensor_1/image@sensor_msgs/msg/Image@gz.msgs.Image

### 3a camera:
Em outro terminal:
Visualizar a imagem da camera:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera_2/link/link_2/sensor/camera_sensor_2/image@sensor_msgs/msg/Image@gz.msgs.Image

### Visualizar no rviz:
> ros2 run rqt_image_view rqt_image_view /world/empty/model/rgbd_camera_1/link/link_1/sensor/camera_sensor_1/image
