# Turtlebot-NavigationStack-Fixed-Waypoints
 fixed waypoint(pose) navigation for turtlebot simulation.

# Task Details

- Task Permformed using **Navigation Stack**
- Used Turtlebot3_simualtions as base package
- Removed Map, used empty world.

# Usage
```
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch
rosrun send_goals send_goals.py
```
# Troubleshoot

## Error:
```
libcurl: (51) SSL: no alternative certificate subject name matches target host name ‘api.ignitionfuel.org'”
```
### Solution

Open ~/.ignition/fuel/config.yaml, replace
```
api.ignitionfuel.org
```
with
```
fuel.ignitionrobotics.org
```
