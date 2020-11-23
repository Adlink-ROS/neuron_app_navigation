# Neuron APP: Navigation

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage
Once users obtain the map, pgm file, and yaml file, navigation is good to go.

1. Launch Navigation as well as Rviz while the Gazebo simulation is running. If you haven't finished SLAM to get the map files, no worries, you can use the default maps **mememan** and **phenix** we have built for you.

   * Bringup all navigation nodes with specific parameters
   ```
   ros2 launch neuronbot2_nav bringup_launch.py map:=$HOME/neuronbot2_ros2_ws/src/neuronbot2/neuronbot2_nav/map/mememan.yaml open_rviz:=true use_sim_time:=true   
   ```

   * Try navigation on your own map. ***Put the <map_name>.yaml and <map_name>.pgm into " ~/neuronbot2_ros2_ws/src/neuronbot2/neuronbot2_nav/map/ "***

   ```
   ros2 launch neuronbot2_nav bringup_launch.py map:=<map_name>.yaml open_rviz:=true use_sim_time:=true
   ```
   * Supported parameters and its value for launch files

      **map**: phenix.yaml | mememan.yaml (default)

      **open_rviz**: true | false (default)

      **use_sim_time**: true | false (default) # if you run navigation in simulation, then use_sim_time must be set to true

   * You can also run localization and navigation in separate terminals.

   ```
   # terminal 1
   ros2 launch neuronbot2_nav localization_launch.py use_sim_time:=true
   # terminal 2
   ros2 launch neuronbot2_nav navigation_launch.py use_sim_time:=true
   # terminal 3
   ros2 launch neuronbot2_nav rviz_view_launch.py use_sim_time:=true
   ```

    ![](readme_resource/mememan_launch_nav.png)
2. Set Estimation
   
   Click "2D Pose Estimate", and set estimation to the approximate location of robot on the map.
   ![](readme_resource/2d_setestimate.png)   

   ![](readme_resource/nav_estimate.gif)
3. Set Goal

   Click "2D Nav Goal", and set goal to any free space on the map.
   ![](readme_resource/2d_nav_goal.png)
   
   ![](readme_resource/nav_set_goal.gif)

