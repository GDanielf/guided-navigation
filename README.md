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
> ign gazebo ~/mestrado_ws/worlds/camera_world.sdf

Em outro terminal

> ign topic -l
/clock
/gazebo/resource_paths
/gui/camera/pose
/sensors/marker
/stats
/world/empty/clock
/world/empty/dynamic_pose/info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_back/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_back/image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_front/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_front/image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_left/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_left/image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_right/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/camera_right/image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/front_laser/scan
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/front_laser/scan/points
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/planar_laser/scan
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/planar_laser/scan/points
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_left/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_left/depth_image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_left/depth_image/points
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_right/camera_info
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_right/depth_image
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/tof_right/depth_image/points
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/vert_laser/scan
/world/empty/model/marble_husky_sensor_config_5/link/base_link/sensor/vert_laser/scan/points
/world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/camera_info
/world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/image
/world/empty/pose/info
/world/empty/scene/deletion
/world/empty/scene/info
/world/empty/state
/world/empty/stats

Em outro terminal:
Visualizar a imagem da camera:
> ros2 run ros_gz_bridge parameter_bridge /world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/image@sensor_msgs/msg/Image@gz.msgs.Image

