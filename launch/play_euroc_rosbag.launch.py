from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    bag_path = '/home/user/euroc_scripts/V1_01_easy_bag'
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', bag_path],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
        ExecuteProcess(
            cmd=['rqt'],
            output='screen'
        )
    ])
