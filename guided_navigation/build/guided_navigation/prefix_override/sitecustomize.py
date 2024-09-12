import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/gdaniel/ros2_ws/src/guided_navigation/install/guided_navigation'
