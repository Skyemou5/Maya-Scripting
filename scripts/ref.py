import maya.cmds as cmds


class RenamerUI():
    def __init__(self):
        self.my_window = 'clCoolToolWindow'

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Super Cool Tool Window',
                                     widthHeight=(200,200))

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout,
                                         placeholderText='Name of new object...')
        self.size_slider = cmds.intSliderGrp(parent=self.col_layout,
                                             minValue=0,
                                             maxValue=25)

        cmds.button(parent=self.col_layout, label='Sphere', c=lambda *x: self.createSphere())
        cmds.button(parent=self.col_layout, label='Cube', c=lambda *x: self.createCube())
        cmds.button(parent=self.col_layout, label='Torus', c=lambda *x: self.createTorus())
        cmds.button(parent=self.col_layout, label='Print field',
                    c='print cmds.textField(name_field, q=True, text=True)')

        cmds.showWindow(self.my_window)


    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


    def createSphere(self):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        size_value = cmds.intSliderGrp(self.size_slider, q=True, value=True)
        cmds.polySphere(name=field_value, r=size_value)

    def createCube(self):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        size_value = cmds.intSliderGrp(self.size_slider, q=True, value=True)
        cmds.polyCube(name=field_value, width=size_value, height=size_value, depth=size_value)

    def createTorus(self):
        pass


my_window = RenamerUI()
my_window.create()
