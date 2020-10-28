import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess
from launch.actions import GroupAction
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    world = [get_package_share_directory('neuronbot2_gazebo'), '/worlds/']
    world.append(LaunchConfiguration('world_model', default='mememan_world.model'))
    gazebo_launch_dir = os.path.join(get_package_share_directory('neuronbot2_gazebo'), 'launch')
    gazebo_model_path = os.path.join(get_package_share_directory('neuronbot2_gazebo'), 'models')

    if 'GAZEBO_MODEL_PATH' in os.environ:
        os.environ['GAZEBO_MODEL_PATH'] += ":" + gazebo_model_path
    else :
        os.environ['GAZEBO_MODEL_PATH'] = gazebo_model_path

    gazebo_bringup = GroupAction([
        ExecuteProcess(
            cmd=['gzserver', '--verbose', world , '-s', 'libgazebo_ros_init.so'],
            output='screen'),

        ExecuteProcess(
            cmd=['gzclient'],
            output='screen'),

        ExecuteProcess(
            cmd=['ros2', 'param', 'set', '/gazebo', 'use_sim_time', use_sim_time],
            output='screen'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(gazebo_launch_dir, 'robot_state_publisher.launch.py')),
            launch_arguments={'use_sim_time': use_sim_time}.items()),
    ])
    ld = LaunchDescription()
    ld.add_action(gazebo_bringup)
    return ld
