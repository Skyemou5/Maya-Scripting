import maya.cmds as cmds
import random

class MainTool():
    def __init__(self):
        self.my_window = "tool window"
    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)
    def create(self):
        self.delete()
        self.my_window = cmds.window( title=window_id,
                                     iconName='Short Name',
                                     widthHeight=(250, 300) )
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
    cmds.text("Tool Shelf")
    cmds.separator(h=10, style='none')
    cmds.button(parent=self.col_layout, label='Scatter Tool', height = 50,
                c=lambda *x: self.createScatterWindow())




    ##### put your functions here #######

my_window = MainTool()
MainTool.create()
