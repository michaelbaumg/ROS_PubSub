# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/mike/motius/devel;/home/mike/db020/devel_isolated/nateplanner;/home/mike/controller_sim/devel_isolated/xil_simulation;/home/mike/controller_sim/devel_isolated/perception_sim;/home/mike/db020/devel_isolated/triplanner;/home/mike/db020/devel_isolated/superbasicsim;/home/mike/db020/devel_isolated/statemachine;/home/mike/db020/devel_isolated/stateestimation;/home/mike/db020/devel_isolated/stanleycontroller;/home/mike/db020/devel_isolated/socketcan_bridge;/home/mike/db020/devel_isolated/socketcan_interface;/home/mike/db020/devel_isolated/sensors;/home/mike/db020/devel_isolated/remotecontroller;/home/mike/db020/devel_isolated/projections2;/home/mike/db020/devel_isolated/planning;/home/mike/db020/devel_isolated/planner;/home/mike/db020/devel_isolated/perception;/home/mike/db020/devel_isolated/oxford_gps_eth;/home/mike/db020/devel_isolated/ground_filter;/home/mike/db020/devel_isolated/ouster_ros;/home/mike/db020/devel_isolated/ouster_viz;/home/mike/db020/devel_isolated/ouster_client;/home/mike/db020/devel_isolated/minkindr_python;/home/mike/db020/devel_isolated/numpy_eigen;/home/mike/db020/devel_isolated/minkindr_conversions;/home/mike/db020/devel_isolated/minkindr;/home/mike/db020/devel_isolated/mapping;/home/mike/db020/devel_isolated/lidar_cone_detection_clustering;/home/mike/db020/devel_isolated/lap_counter;/home/mike/db020/devel_isolated/db_image_undistort;/home/mike/db020/devel_isolated/image_undistort;/home/mike/db020/devel_isolated/hesai_lidar;/home/mike/db020/devel_isolated/eigen_checks;/home/mike/db020/devel_isolated/glog_catkin;/home/mike/db020/devel_isolated/gflags_catkin;/home/mike/db020/devel_isolated/fastslam;/home/mike/db020/devel_isolated/eigen_catkin;/home/mike/db020/devel_isolated/dnb_msgs;/home/mike/db020/devel_isolated/darknet_ros;/home/mike/db020/devel_isolated/darknet_ros_msgs;/home/mike/db020/devel_isolated/conearray_viz;/home/mike/db020/devel_isolated/custom_msgs;/home/mike/db020/devel_isolated/curvatureoptimized;/home/mike/db020/devel_isolated/coremodules;/home/mike/db020/devel_isolated/controller;/home/mike/db020/devel_isolated/config;/home/mike/db020/devel_isolated/catkin_boost_python_buildtool_test;/home/mike/db020/devel_isolated/catkin_simple;/home/mike/db020/devel_isolated/catkin_boost_python_buildtool;/home/mike/db020/devel_isolated/can_msgs;/home/mike/db020/devel_isolated/camera_control_msgs;/home/mike/db020/devel_isolated/basicstateestimation;/home/mike/db020/devel_isolated/accel_planner;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/mike/motius/devel/env.sh')

output_filename = '/home/mike/motius/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
