#! /usr/bin/env python3

import rospy
import std_msgs
from rx_pci_single_ros.msg import pfeiffer_tpg261_msg

import sys
import time
import threading
import NASCORX_System.device.TPG261 as TPG261

if __name__=='__main__':
    # initialize parameters
    # ---------------------
    nodename = 'pfeiffer_tpg261'
    topicname = 'pfeiffer_tpg261'
    rospy.init_node(nodename)
    host = rospy.get_param('~host')
    rate = rospy.get_param('~rate')

    # setup devices
    # -------------
    try:
        vaccume = TPG261.tpg261(host)
    except OSError as e:
        rospy.logerr("{e.strerror}. host={host}".format(**locals()))
        sys.exit()

    # setup ros
    # ---------
    pub = rospy.Publisher(topicname, pressure.msg.tpg261_values, queue_size=1)

    # start loop
    # ----------
    while not rospy.is_shutdown():
        ret = pfeiffer.query_pressure()

        msg = pressure.msg.tpg261_values()
        msg.timestamp = time.time()
        msg.ch1_value = ret
        pub.publish(d)

        time.sleep(rate)
        continue
