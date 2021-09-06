#!/usr/bin/python2.7
"""
Write hello world with the current time to the console and publish this string on the rostopic 'chatter'
"""
import rospy
from std_msgs.msg import String
from datetime import datetime


# Define the function to print and publish the string
def talker():

    # Initialize the node
    rospy.init_node('talker', anonymous=True)

    # Define the publisher
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # Define the frequency
    rate = rospy.Rate(10)

    # Loop till stopped by the user
    while not rospy.is_shutdown():

        # Define output string
        hello_str = "hello world " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Print string to console as info
        rospy.loginfo(hello_str)

        # Publish on the rostopic chatter
        pub.publish(hello_str)

        # Sleep for as long as necessary to run at defined frequency. Takes the time till last sleep
        rate.sleep()


# Main loop
if __name__ == '__main__':

    # Function call
    talker()
