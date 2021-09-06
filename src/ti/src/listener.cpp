/*
Reads the message from rostopic 'chatter' and calls for every message the chatterCallback function.
In this function it prints "I heard " and the received string
*/
#include "ros/ros.h"
#include "std_msgs/String.h"

// Callback function
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  // Print string to terminal
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  // Initialize
  ros::init(argc, argv, "listener");

  // Defines the node
  ros::NodeHandle n;

  // Call the subscriber. This calls the callback function for every message newly published on "chatter"
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  // Keeps the subscriber alive
  ros::spin();

  return 0;
}
