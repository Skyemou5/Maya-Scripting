import maya.cmds as cmds
#import pymel.core as pm
import random

########## tool test ###########

class MainUI():
    #string window_id = 'cool window'
    def __init__(self):
        self.my_window = 'toolWindow'

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title = 'coolWindow',
                                     widthHeight=(200,200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.col_layout,
                                         placeholderText='Name of new obj')
        cmds.button(parent=self.col_layout,label='sphere',
                    c=lambda *x: self.createSphere())
        cmds.button(parent=self.col_layout, label='sphere',
                    c='print cmds.textField(name_field, q=True, text=true')

        cmds.showWindow(self.my_window) # create window

    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)

    def createSphere(self):
        field_val = cmds.textField(self.name_field, q=True, text=True)
        cmds.polySphere(name=field_val)

def rename():
    name_string = 'Cube_###_Obj'

    char_list = list(name_string)

    sels = cmds.ls(sl=True)

    # returns the number of '#'
    hash_num = name_string.count('#')

    # returns ('Cube_', '###', '_Obj')
    parts = name_string.partition('#' * hash_num)

    # returns the first instances index 5
    piece = name_string.find("#")
    print 'piece starts as ', piece

    # returns last index location of # 7
    index_num = (piece + hash_num)
    print 'index number: ', index_num

    hash_list = []
    end_hash = index_num - 1

    for i in range(piece, end_hash, 1):
        hash = char_list.pop(i)
        hash_list.extend(hash)
        print 'i is', i, 'popped characters ', hash

    new_name_string = ''.join(char_list)
    print new_name_string

    replace_num_string = '1'
    replace_num_int = 1
    # replace_index = (name_string[piece : index_num])
    # print 'replace index ', replace_index

    if parts[1]:
        print 'Characters are sequential'
        for s in sels:
            new_num = replace_num_string.zfill(hash_num)
            print 'the new num is', new_num
            new_name_string = new_name_string.replace('#', new_num)
            print 'the new name is ', new_name_string
            print 'the replace num is ', type(replace_num_int)
            replace_num_int += 1
            print 'the replace num is ', replace_num_int
            replace_num_string = str(replace_num_int)
            cmds.rename(new_name_string)
            # replace_num = str(replace_num)
    else:
        cmds.error('Characters are not sequential. Input another string.')\

def scatter(rand_trans, rand_rot, rand_scale):

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

my_window = MainUI()
my_window.create()