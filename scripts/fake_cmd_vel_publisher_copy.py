#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(data):
    # 수신한 메시지에서 angular.z 값을 3배로 증폭
    data.angular.z *= 3.0
    data.angular.z = round(data.angular.z, 2)
    # 증폭된 메시지를 다시 cmd_vel 토픽으로 게시
    cmd_vel_publisher.publish(data)

if __name__ == '__main__':
    rospy.init_node('cmd_vel_amplifier', anonymous=True)
    
    # /cmd_vel 토픽에서 메시지를 받는 subscriber 생성
    rospy.Subscriber('fake_cmd_vel', Twist, cmd_vel_callback)
    
    # /cmd_vel 토픽으로 메시지를 게시하는 publisher 생성
    cmd_vel_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # 노드를 실행
    rospy.spin()