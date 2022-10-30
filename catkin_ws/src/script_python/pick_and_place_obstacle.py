
from simulation import *


#Init ros node :
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group_python_interface_tutorial", anonymous=True)



robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "yaskawa_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

cube1 = "box1"
cube2 = "box2"
sol = "floor"
cubeObstacle = "obstacle1"


BOX_1_POSE = [0.5, 0.5, 0.2, 0, 3.1415, 0]
BOX_2_POSE = [-0.5, -0.5, 0.4, 0, 3.1415, 0]
PARKING_POSE = [0, 0, 3.1415, 0, 0, 0]


display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=50
)

if __name__ == '__main__':
    print("START OF THE SIMULATION")

    move_group.set_goal_tolerance(0.005)
    (planning_frame,eef_link,group_names) = get_robot_status(robot,move_group,display=False)

    #Go to the parking position :
    go_to_target_joints_values(move_group, PARKING_POSE)

    #Add some boxes to the scene :
    add_box(scene, "world", sol, 0, 0, -0.08, 5, 5, 0.1)                           
    add_box(scene, "world", cube1, BOX_1_POSE[0], BOX_1_POSE[1], 0.2, 0.1, 0.2, 0.2)     
    add_box(scene, "world", cube2, BOX_2_POSE[0], BOX_2_POSE[1], 0.1, 0.2, 0.2, 0.2)    
    add_box(scene, "world", cubeObstacle, 0.5, 0.72, 0.6, 0.3, 0.3, 0.3)                    

    go_to_target(move_group, BOX_1_POSE)
    print(f"robot above the box {cube1}")
    attach_box(scene, robot, eef_link, cube1, "hand")
    go_to_target_joints_values(move_group, PARKING_POSE)
    go_to_target(move_group, BOX_2_POSE)
    detach_box(scene, eef_link, cube1)


    print("END OF THE SIMULATION")
