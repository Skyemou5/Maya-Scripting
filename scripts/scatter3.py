import maya.cmds as cmds
import random as rand

selectction = cmds.ls(orderedSelection=True, flatten=True)
vertex_names = cmds.filterExpand(selectction, selectionMask=31, expand=True)


object_to_instance = selectction[0]
rand_pos = [0,0,0]

for object in object_to_instance:
    rand_pos = [rand.randrange(-5,5),rand.randrange(-5,5),0]
    new_instance = cmds.instance(object_to_instance)
    cmds.move(rand_pos[0],rand_pos[1],rand_pos[2], absolute=True)




