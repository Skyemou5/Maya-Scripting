import maya.cmds as cmds


class MyUI():
    def create(self,windowTitle,callback):
        windowID = 'mywindow'
        if cmds.window(windowID,exists = True):
            cmds.deleteUI(windowID)

        cmds.window(windowID,title=windowTitle,sizeable=True,resizeToFitChildren = True)

        cmds.rowColumnLayout(columnWidth=[ (1,75), (2,60), (3,60) ],columnOffset = [ (1,'right',3) ])
        cmds.text(label='Time Range')
        startFrameNum = cmds.intField(value = cmds.playbackOptions(q=True,minTime=True))
        timeField = cmds.intField(value=cmds.playbackOptions(q=True, maxTime=True))
        cmds.text(label='Attribute')
        targetAttributeField = cmds.textField(text='rotateY')
        cmds.separator(h=10, style ='none')
        cmds.separator(h=10, style='none')
        cmds.separator(h=10, style='none')
        cmds.separator(h=10, style='none')

        cmds.button(label='Apply',command=callback)

        def cancelCallback(self,*pArgs):
            if cmds.window(windowID,exists=True):
                cmds.deleteUI(windowID)

        cmds.button(label='Cancel',command=cancelCallback)

        cmds.showWindow()

    def applyCallback(self,*pArgs):
        print 'apply button pressed'
my_window = MyUI()
my_window.create('my title', applyCallback)



# widgets = {}
#
# def UI():
#     if cmds.window('exampleToolbar' , exists = True):
#         cmds.deleteUI('exampleToolbar')
#
#     widgets['window'] = cmds.window('exampleToolbar',w = 150, h = 700, mhb = False, mxb = False, title = 'Toolbar')
#
#     cmds.showWindow(widgets['window'])