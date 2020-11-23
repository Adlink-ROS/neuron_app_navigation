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

1. Launch Navigation as well as Rviz with the Gazebo simulation. If you haven't finished SLAM to get the map files, no worries, you can use the default maps **mememan** we have built for you.

   ```
   ros2 launch napp_navigation gazebo_navigation.launch.py
   ```
   ![](readme_resource/mememan_launch_nav.png)
2. Set Estimation


   ![](readme_resource/2d_setestimate.png)


   Click "2D Pose Estimate", and set estimation to the approximate location of robot on the map.
   

   ![](readme_resource/nav_estimate.gif)
3. Set Goal


   ![](readme_resource/2d_nav_goal.png)


   Click "2D Nav Goal", and set goal to any free space on the map.
  
   
   ![](readme_resource/nav_set_goal.gif)

