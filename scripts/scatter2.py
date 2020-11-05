import maya.cmds as cmds
import random


def scatter_objects(rand_trans, rand_rot, rand_scale):
    """
    Take the user's current selection and scatter the first item in it onto the
    vertexes in the rest of the selection.
    :param tuple(float) rand_trans: The maximum + minimum random positional offset to apply.
    :param tuple(float) rand_rot: The maximum + minimum random rotational offset to apply.
    :param tuple(float) rand_scale: The maximum + minimum random scale offset to apply.
    """
    selectction = cmds.ls(orderedSelection=True, flatten=True)
    vertex_names = cmds.filterExpand(selectction, selectionMask=31, expand=True)

    # Create a group to add the new objects to later
    scatter_grp = cmds.group(em=True, n='scatter_grp')

    object_to_instance = selectction[0]
    if cmds.objectType(object_to_instance) == 'transform':
        for vertex in vertex_names:
            new_instance = cmds.instance(object_to_instance)
            position = cmds.pointPosition(vertex, world=True)

            # Using list comprehension, apply the random offset to the position.
            new_position = [x + random.uniform(rand_trans[0], rand_trans[1]) for x in position]
            new_rotation = [random.uniform(rand_rot[0], rand_rot[1]) for _ in range(3)]
            new_scale = [random.uniform(rand_scale[0], rand_scale[1]) for _ in range(3)]

            # Set the position
            cmds.move(new_position[0],
                      new_position[1],
                      new_position[2],
                      new_instance,
                      absolute=True,
                      worldSpace=True)

            # Set the rotation
            cmds.rotate(new_rotation[0],
                        new_rotation[1],
                        new_rotation[2],
                        new_instance,
                        relative=True,
                        objectSpace=True)

            # Set the scale
            cmds.scale(new_scale[0],
                       new_scale[1],
                       new_scale[2],
                       new_instance,
                       relative=True)

            # Parent into the group
            cmds.parent(new_instance, scatter_grp)

    else:
        print("Please ensure the first object you select is a transform.")


# Call the scatter objects definition. Each argument is passed in with the min and max random values.
# In the case where you want noting to happen pass both min and max in as 0. scale will be 1.
scatter_objects((0, 10), (0, 360), (0.5, 1.5))