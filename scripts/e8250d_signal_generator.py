#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64

import sys
import time
import threading
import NASCORX_System.device.E8257D as E8257D

nname = 'e8257d'

class e8257d_controller(object):

    def __init__(self):
        self.pinterval = 0.1
        self.host = rospy.get_param('~host')
        self.port = rospy.get_param('~port')
        self.sg = E8257D.e8257d(self.host, self.port)
        self.pub_freq = rospy.Publisher('lo_1st_freq', Float64, quere_size=1)
        self.pub_power = rospy.Publisher('lo_1st_power', Float64, quere_size=1)
        self.pub_onoff = rospy.Publisher('lo_1st_onoff', Float64, quere_size=1)
        self.sub_freq.rospy.Subscriber('lo_1st_freq.cmd', lo_1st_freq_msg, _set_freq)
        self.sub_power.rospy.Subscriber('lo_1st_power.cmd', lo_1st_power_msg, _set_power)
        self.rospy.Subscriber('lo_1st_onoff.cmd', lo_1st_onoff_msg, _set_onoff)

    def _set_freq(self, q):
        target = q.lo_1st_freq
        self.sg.set_freq(target, 'GHz')

        while True:
            current = self.sg.query_freq()

            if target != cuurent:
                self.pub_freq.publish(current)
                time.sleep(self.pinterval)
                pass

            elif target == cuurent:
                self.pub_freq.publish(curent)
                time.sleep(self.pinterval)
                break

    def _set_power(self, q):
        self.sg.set_power(target)

        while True:
            current = self.sg.query_power()

            if target != cuurent:
                self.pub_power.publish(current)
                time.sleep(self.pinterval)
                pass

            elif target == cuurent:
                self.pub_power.publish(cuurent)
                time.sleep(self.pinterval)
                break

    def _set_onoff(self, q):
        target = q.lo_1st_onoff
        self.sg.set_onoff(target)

        while True:
            current = self.sg.query_onoff()
            msg.lo_1st_onoff_msg = current

            if target != cuurent:
                self.pub_onoff.publish(current)
                time.sleep(self.pinterval)
                pass

            elif target == cuurent:
                self.pub_onoff.publish(current)
                time.sleep(self.pinterval)
                break

if __name__ == '__main__':
    rospy.init_node(nname)
    sg_ctrl = e8257d_controller()
    sg_ctrl.start_thread_ROS()
    print('[e8257d_signal_generetor] : START SUBSCRIBER ... ')
    rospy.spin()