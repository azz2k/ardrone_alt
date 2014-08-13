import rospy
from ardrone_autonomy.msg import Navdata
from nav_msgs.msg import Odometry

class ArdroneAlt():
  def __init__(self):
    # setup rospy and get parameters
    rospy.init_node("ardronealt")
    self.adapter = rospy.get_param("~cov_alt", 0.1)
    # setup main loop
    rospy.Subscriber("ardrone/navdata", Navdata, self.navdata_callback)
    self.pub = rospy.Publisher("odoalt", Odometry, queue_size=10)
    r = rospy.Rate(10)
    # main loop
    while not rospy.is_shutdown():
      r.sleep()
  def navdata_callback(self, data):
    print data.altd
