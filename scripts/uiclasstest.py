import maya.cmds as cmds

class RenamerUI():
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
        cmds.button(parent=self.col_layout,label='sphere', c='createSphere()')
        cmds.button(parent=self.col_layout, label='sphere',
                    c='print cmds.textField(name_field, q=True, text=true')

    def delete(self):
        if cmds.window(self.my_window, exists = True):
            cmds.deleteUI(self.my_window)

    def createSphere(self):
        field_val = cmds.textField(self.name_field, q=True, text=True)
        cmds.polySphere(name=field_val)

# MY_WINDOW = RenamerUI()
# # MY_WINDOW.create()