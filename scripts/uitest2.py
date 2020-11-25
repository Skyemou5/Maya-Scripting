import maya.cmds as cmds
#import pymel.core as pm
import random
window_id = 'coolwindow'

class MainUI():
    def __init__(self):
        self.my_window = window_id
    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)
    def create(self):
        self.delete() # delete if UI already in memory

        self.my_window = cmds.window( title=window_id, iconName='Short Name', widthHeight=(200, 55) )
        self.cmds.columnLayout( adjustableColumn=True )


my_window = MainUI()
my_window.create()