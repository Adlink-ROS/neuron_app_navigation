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
1. Click application in Neuron App to open workspace. It will build the resource at first time it's opened.
     ![](readme_resource/open_app.png)
   
2-1. Click "packages" on the right side.

2-2. Open list by click "RESOURCES" -> "user-workspace" -> "napp_slam"
     ![](readme_resource/click_resourse_nav.png)
     

***NOTE!!! Following instruction would need : Right click desired launch file and click "Run" -> "Run Launch File" as image bellow***

   ![](readme_resource/launch_nav.png)
3. Launch Navigation as well as Rviz with the Gazebo simulation. Launch gazebo_navigation.launch.py

If you haven't finished SLAM to get the map files, no worries, you can use the default maps **mememan** we have built for you.

   ![](readme_resource/mememan_launch_nav.png)
4. Set Estimation


   ![](readme_resource/2d_setestimate.png)


   Click "2D Pose Estimate", and set estimation to the approximate location of robot on the map.
   

   ![](readme_resource/nav_estimate.gif)
5. Set Goal


   ![](readme_resource/2d_nav_goal.png)


   Click "2D Nav Goal", and set goal to any free space on the map.
  
   
   ![](readme_resource/nav_set_goal.gif)

