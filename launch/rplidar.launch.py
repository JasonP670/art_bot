# I had to run the following commands in the terminal to be able to connect to the lidar
# sudo adduser $USER dialout
# sudo chmod 666 /dev/ttyUSB0 
# This has to be done each time a session is started, unless you make a udev rule


import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                # 'serial_port': '/dev/serial/by-path/platform-fd500000.pci-0000:00:1a.0-usb-0:1.2:1.0-port0',
                'serial_port': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',
                'frame_id': 'laser_frame',
                # 'angle_compensate': True,
                'scan_mode': 'Standard',
                'baud_rate': 115200
            }]
        )
    ])