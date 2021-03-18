#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import math
import numpy as np
import matplotlib.pyplot as plt

scan_data = None
def scan_callback(data):
    global scan_data
    scan_data = data
	
def lidar_visualization():
    rospy.Subscriber('scan', LaserScan, scan_callback)
    rospy.init_node('lidar_visualization')

    FREQ = 20
    rate = rospy.Rate(FREQ)

    while scan_data is None:
        print 'Waiting for LaserScan data'
        rospy.sleep(1)

    while not rospy.is_shutdown():
        dist_array = np.array(scan_data.ranges, copy=True)
        num_distances = len(dist_array)
        XY = np.zeros((num_distances,2))

        for i, distance in enumerate(dist_array):

            if np.isinf(distance):
                continue

            #############
            # Your code (find x and y. Units are in cm) 
            x = 0
            y = 0
            #############

            XY[i,:]=(x,y)

        plt.cla()
        plt.plot(XY[:,0],XY[:,1], ".g")
        plt.grid(True)
        plt.xlim(-500,500)
        plt.ylim(-500,500)
        plt.pause(0.001)
        rate.sleep()
        
if __name__ == '__main__':
        print("lidar_visualization")
        lidar_visualization()
