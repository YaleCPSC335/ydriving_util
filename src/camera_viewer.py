#!/usr/bin/env python
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

topic_name = 'camera'

image = None
bridge = CvBridge()

def image_callback(ros_image):
    global image
    image = bridge.imgmsg_to_cv2(ros_image, "bgr8")

    cv2.imshow('camera', image)

    #Some image processing code
    #[Example] 
    #gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray_img', gray_img)

    cv2.waitKey(1)

if __name__ == '__main__':
    camera_sub = rospy.Subscriber(topic_name, Image, image_callback)
    rospy.init_node('camera_viewer', anonymous=True)
    rospy.spin()



