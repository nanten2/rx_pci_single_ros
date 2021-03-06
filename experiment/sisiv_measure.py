#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/rx_pci_single_ros/scripts/')
import sisbb_controller as ctrl
import rospy
from rx_pci_single_ros.msg import logger_high_flag_msg

initial_voltage = -7 # mV
final_voltage = 7    # mV
step = 0.1          # mV
interval = 0.1         # sec.
roop = int((final_voltage - initial_voltage) / step)

tname = 'logger_controller'
pub = rospy.Publisher(tname, logger_high_flag_msg, queue_size=1)

msg = logger_high_flag_msg()
msg.timestamp = str(time.time())
time.sleep(0.1)
print(msg)
pub.publish(msg)

try:
    for i in range(roop+1):
        ctrl.sisbb_set_voltage(ch=0, voltage=i*step-final_voltage, interval=0.1) # all ch set voltage
        time.sleep(interval)
    pass
except KeyboardInterrupt:
    ctrl.sisbb_set_voltage(ch=0, voltage=0, interval=0.1) # all ch set voltage
    msg = logger_high_flag_msg()
    msg.timestamp = ''
    time.sleep(0.1)
    pub.publish(msg)    
    sys.exit()

ctrl.sisbb_set_voltage(ch=0, voltage=0, interval=0.1)

msg = logger_high_flag_msg()

msg = logger_high_flag_msg()
msg.timestamp = ''
print(msg)
time.sleep(0.1)
pub.publish(msg)
