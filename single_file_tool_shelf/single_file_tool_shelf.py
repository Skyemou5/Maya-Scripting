#region ------------ imports ------------

import maya.cmds as cmds
#import pymel.core as pm
import random
from maya.OpenMaya import MVector

#endregion

#region ------------ global vars ------------
window_id = 'ToolShelf'
#endregion

#region ------------ UI Classes ------------

#region ### main UI Tool shelf == #####

class ToolShelfUI():
    def __init__(self):
        self.my_window = window_id
    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)
    def create(self):
        self.delete()

        self.my_window = cmds.window(title = 'TS',
                                     iconName = 'Short Name',
                                     widthHeight=(200,600) )
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        #region ======== Toolshelf buttons ==========
        #region ------- These open new windows -------
        cmds.separator(h=10, style='none')

        cmds.text("Tool Shelf")############ label ############

        cmds.separator(h=20, style='double')
        cmds.separator(h=10, style='double')
        cmds.separator(h=10, style='none')

        cmds.text("Complex Tools")############ label ############

        cmds.separator(h=10, style='none')
        cmds.button(parent=self.col_layout, label='Rename Tool', height = 50,
                    c=lambda *x: self.createRenamerWindow())

        cmds.separator(h=10, style='none')

        cmds.button(parent=self.col_layout, label='Scatter Tool', height = 50,
                    c=lambda *x: self.createScatterWindow())

        cmds.separator(h=10, style='double')
        cmds.separator(h=10, style='double')
        cmds.separator(h=20, style='none')

        #endregion
        #region ------ Non classes tools -------
        cmds.text("Quick Tools")
        cmds.separator(h=20, style='none')
        cmds.button(parent=self.col_layout, label='Freeze Transforms', height = 50,
                    c=lambda *x: freeze_transforms())

        cmds.separator(h=10, style='none')
        cmds.button(parent=self.col_layout, label='Delete Selected History', height = 50,
                    c=lambda *x: delete_selected_history())

        cmds.separator(h=10, style='none')
        cmds.button(parent=self.col_layout, label='Parent Group', height = 50,
                    c=lambda *x: parent_group())

        cmds.separator(h=10, style='none')
        cmds.button(parent=self.col_layout, label='Parent Scale Constrain', height = 50,
                    c=lambda *x: parent_scale_constrain())

        cmds.separator(h=10, style='none')
        cmds.button(parent=self.col_layout, label='Toggle Local Axis Vis', height = 50,
                    c=lambda *x: toggle_local_axis_vis())

        cmds.separator(h=10, style='none')
        #endregion
        #endregion


        cmds.showWindow(self.my_window)

    def createScatterWindow(self):
        my_window = ScatterUI()
        my_window.create()

    def createRenamerWindow(self):
        my_window = RenameUI()
        my_window.create()
#endregion

#region ------------ Sub tool UIs ------------

class RenameUI():
    def __init__(self):
        self.my_window = window_id

    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)
    def create(self):
        self.delete() # delete if UI already in memory

        self.my_window = cmds.window( title=window_id,
                                     iconName='Short Name',
                                     widthHeight=(250, 300) )
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        ### rename text ####
        cmds.separator(h=10, style='none')
        cmds.text("Renamer")
        cmds.separator(h=40, style='none')

        cmds.separator(h=10, style='none')

        ### Input Fields ###
        cmds.text("Prefix")
        self.prefix_field = cmds.textField(placeholderText='cube',text='cube')
        cmds.separator(h=10, style='none')
        cmds.text("Suffix")
        self.suffix_field = cmds.textField(placeholderText='obj',text='obj')
        ### button ###
        cmds.separator(h=20, style='none')
        cmds.button(parent=self.col_layout, label='Rename Selection', height = 40,
                    c=lambda *x: self.rename_button_call())

        cmds.showWindow(self.my_window) # draw window

    def rename_button_call(self):
        prefix_val = cmds.textField(self.prefix_field, editable = True, query = True, text=True)
        suffix_val = cmds.textField(self.suffix_field, editable = True, query = True, text=True)
        RenameTool.rename(RenameTool(), prefix_val, suffix_val)

class ScatterUI():
    def __init__(self):
        self.window_id = 'scatter tool'
        self.my_window = self.window_id
        self.scatter_amount = ''
        self.random_translation_amount = ''
        #self.scatter_class = ScatterObjects()
    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)
    def get_values(self):
        pass
    def create(self):
        self.delete() # delete if UI already in memory

        self.my_window = cmds.window(title=self.window_id,
                                    iconName='Short Name',
                                    widthHeight=(250, 300) )
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        ### random tool label ###
        cmds.separator(h=10, style='none')
        cmds.text("Scatter Tool")
        cmds.separator(h=10, style='none')


        # cmds.button(parent=self.col_layout, label='Scatter Objects', height = 40,
        #             c=lambda *x: scatterObjects(self.random_trans_field, self.scatter_amount_field))
        cmds.button(parent=self.col_layout, label='Scatter Objects', height = 40,
                    c=lambda *x: self.scatter_button_call())

        cmds.separator(h=20, style='none')
        cmds.text("Random_Translation")
        self.random_trans_field = cmds.floatField(value = 5.0)
        cmds.separator(h=20, style='none')
        cmds.text("Scatter Amount")
        self.scatter_amount_field = cmds.intField(value = 5)


        cmds.separator(h=10, style='none')

        cmds.showWindow(self.my_window) # draw window

    def scatter_button_call(self):
        random_trans = cmds.floatField(self.random_trans_field, q=True, value=True)
        num_of_dupes = cmds.intField(self.scatter_amount_field, q=True, value=True)
        ScatterObjects.scatter(ScatterObjects(), random_trans, num_of_dupes)

#endregion

#endregion

#region ============= Subtools ==============


#region ------------ Subtool Work Classes ------------

class RenameTool():
    def __init__(self):
        pass
    def rename(self,prefix,suffix):
        #name_string = 'Cube_###_Obj'
        print prefix


        self.name_string = '%s_###_%s' % (prefix,suffix)

        print 'Name String = %s' %(self.name_string)

        self.char_list = list(self.name_string)

        self.sels = cmds.ls(sl=True)

        # returns the number of '#'
        self.hash_num = self.name_string.count('#')

        # returns ('Cube_', '###', '_Obj')
        self.parts = self.name_string.partition('#' * self.hash_num)

        # returns the first instances index 5
        self.piece = self.name_string.find("#")
        print 'piece starts as ', self.piece

        # returns last index location of # 7
        self.index_num = (self.piece + self.hash_num)
        print 'index number: ', self.index_num

        self.hash_list = []
        self.end_hash = self.index_num - 1

        for self.i in range(self.piece, self.end_hash, 1):
            self.hash = self.char_list.pop(self.i)
            self.hash_list.extend(self.hash)
            print 'i is', self.i, 'popped characters ', self.hash

        self.new_name_string = ''.join(self.char_list)
        print self.new_name_string

        self.replace_num_string = '1'
        self.replace_num_int = 1
        # replace_index = (name_string[piece : index_num])
        # print 'replace index ', replace_index

        if self.parts[1]:
            print 'Characters are sequential'
            for self.s in self.sels:
                self.new_num = self.replace_num_string.zfill(self.hash_num)
                print 'the new num is', self.new_num
                self.new_name_string = self.new_name_string.replace('#', self.new_num)
                print 'the new name is ', self.new_name_string
                print 'the replace num is ', type(self.replace_num_int)
                self.replace_num_int += 1
                print 'the replace num is ', self.replace_num_int
                self.replace_num_string = str(self.replace_num_int)
                cmds.rename(self.new_name_string)
                # replace_num = str(replace_num)
        else:
            cmds.error('Characters are not sequential. Input another string.')\

class ScatterObjects():
    """
    Take the user's current selection and scatter the first item in it onto the
    vertexes in the rest of the selection.
    """
    def __init__(self):
        pass

    def get_values(self,one,two):
        print(one,two)
    # print('random amt $s'(random_amount))
    # print('random area $s'(random_area))
    #     selection = cmds.ls(orderedSelection=True, flatten=True)
    #     for obj in range(10):
    #         print(obj)
    def scatter(self,random_area,random_amount):


        for self.i in range(random_amount):
            self.x = random.randrange(0, random_area)
            #y = random.randrange(0,random_area)
            self.z = random.randrange(0, random_area)
            self.y = 0
            self.position_vector = MVector(self.x, self.y, self.z)
            print(self.x, self.y, self.z)
            cmds.instance()
            cmds.move(self.x, self.y, self.z,
                      absolute = True,
                      worldSpace = True)



            #print(selection)

#endregion

#region ----- NON classed funtions ------

def freeze_transforms():
    sels = cmds.ls(sl=True)
    print sels
    #performFreezeTransformations(0);
    cmds.makeIdentity(sels, apply=True, translate=True, rotate=True, scale=True)


def delete_selected_history():
    sels = cmds.ls(sl=True)
    print(sels)
    cmds.delete(sels,constructionHistory = True)

def parent_group():
    sels = cmds.ls(sl=True)
    cmds.Group(sels)

def parent_scale_constrain():
    sels = cmds.ls(orderedSelection=True, flatten=True)
    cmds.scaleConstraint(sels[0], sels[1])

def toggle_local_axis_vis():
    sels = cmds.ls(sl=True)
    cmds.toggle(sels, localAxis=True)

#endregion

#endregion

#region ################# ================ create first window ================ #################
my_window = ToolShelfUI()
my_window.create()
#endregion