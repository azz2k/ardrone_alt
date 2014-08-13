cmake_minimum_required(VERSION 2.8.3)
project(ardrone_alt)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  nav_msgs
  ardrone_autonomy
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS message_runtime
  CATKIN_DEPENDS rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  bin/ardrone_alt
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
