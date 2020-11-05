import maya.cmds as cmds

selectction = cmds.ls(orderedSelection=True, flatten=True)
vertex_names = cmds.filterExpand(selectction, selectionMask=31, expand=True)


object_to_instance = selectction[0]

if cmds.objectType(object_to_instance) == 'transform':
    for vertex in vertex_names:
        new_instance = cmds.instance(object_to_instance)
        position = cmds.pointPosition(vertex, world=True)
        cmds.move(position[0], position[1], position[2],  new_instance, absolute=True, worldSpace=True)
else:
    print("Please ensure the first object you select is a transform.")