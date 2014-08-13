import rospy
from ardrone_autonomy.msg import Navdata
from nav_msgs.msg import Odometry

class ArdroneAlt():
  def __init__(self):
    # setup rospy and get parameters
    rospy.init_node("ardronealt")
    self.covalt = rospy.get_param("~cov_alt", 0.1)
    # setup main loop
    rospy.Subscriber("ardrone/navdata", Navdata, self.navdata_callback)
    self.pub = rospy.Publisher("odoalt", Odometry, queue_size=10)
    r = rospy.Rate(10)
    # main loop
    while not rospy.is_shutdown():
      r.sleep()
  def navdata_callback(self, data):
    msg = Odometry()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "base_link"
    msg.pose.pose.position.x = 0.0
    msg.pose.pose.position.y = 0.0
    msg.pose.pose.position.z = data.altd * 1e-3
    msg.pose.pose.orientation.x = 1 
    msg.pose.pose.orientation.y = 0 
    msg.pose.pose.orientation.z = 0 
    msg.pose.pose.orientation.w = 0 
    msg.pose.covariance = [99999, 0, 0, 0, 0, 0, 
      0, 99999, 0, 0, 0, 0, 
      0, 0, self.covalt, 0, 0, 0, 
      0, 0, 0, 99999, 0, 0, 
      0, 0, 0, 0, 99999, 0, 
      0, 0, 0, 0, 0, 99999]
    self.pub.publish(msg)
