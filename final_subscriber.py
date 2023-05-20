
import rospy
from std_msgs.msg import Int64

def callback(data):
    std_id = data.data
    rospy.loginfo(f"Received std_id: {std_id}")

def final_subscriber():
    rospy.init_node('final_subscriber', anonymous=True)
    rospy.Subscriber('/std_id', Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    final_subscriber()