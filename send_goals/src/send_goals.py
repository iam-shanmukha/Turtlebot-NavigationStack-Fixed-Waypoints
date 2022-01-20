#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

goals = [[10,3,50],[-10,3,50],[-10,-3,50],[10,-3,50]]

def movebase_client():
    while not rospy.is_shutdown():
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()
        # -10,3,50
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "odom"
        '''
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = -10.0
        goal.target_pose.pose.position.y = 3.0
        goal.target_pose.pose.orientation.z = 50.0
        '''
        for i in range(4):
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = goals[i][0]
            goal.target_pose.pose.position.y = goals[i][1]
            goal.target_pose.pose.orientation.z = goals[i][2]
            print("Moving to Goal {},{},{}".format(goals[i][0],goals[i][1],goals[i][2]))
            client.send_goal(goal)
            wait = client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
            else:
                #return client.get_result()
                print("Goal {} Reached".format(i))

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
