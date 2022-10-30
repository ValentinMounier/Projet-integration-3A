# Projet-integration-3A
## Setup
- Après avoir téléchargé l'archive, se déplacer dans le répertoire :
```
cd Projet-integration-3A/catkin_ws
```
- Sourcer ROS et build le projet :
```
source /opt/ros/noetic/setup.bash
catkin build
```
- Puis sourcer le projet build 
```
source /devel/setup.bash
```
- Lancer la simulation :

```
roslaunch yaskawa_moveit_config demo.launch
```
- Ouvrir un deuxième terminal, sourcer le projet, puis lancer le script :
```
python3 src/script_python/pick_and_place.py
```
