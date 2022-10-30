

from simulation import *
import numpy as np

#Init ros node :
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_python_interface_tutorial", anonymous=True)


if __name__ == '__main__':
    print("START SIMULATION")
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "yaskawa_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    (planning_frame,eef_link,group_names) = get_robot_status(robot,move_group,display=False)

    vue1 = np.radians([-12, 47, 116, -22, -112, 23])    
    vue2= np.radians([86, 37, 192, 75, -149, -85])      
    pose_exploration_cube = [vue1, vue2]

    #Perform trajectory to acquire box with the Kinect:
    for (i, pose) in enumerate(pose_exploration_cube):
        print(f"go to position n°{i}")
        go_to_target_joints_values(move_group, pose)
    print("END OF THE SIMULATION")
