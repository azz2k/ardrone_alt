#!/usr/bin/env python

import rospy

class ArdroneAlt():
  def __init__(self):
    # setup rospy and get parameters
    rospy.init_node("ardronealt")
    # setup main loop
    #self.pub = rospy.Publisher("rssi", RssiMulti, queue_size=10)
    r = rospy.Rate(self.rate)
    # main loop
    while not rospy.is_shutdown():
      pass
