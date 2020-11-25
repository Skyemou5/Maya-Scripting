import sys, os
import pymel.core as pm
import maya.cmds as cmds


# from PySide import QtCore, QtGui, QtUiTools
# import shiboken

import maya.cmds as cmds
import maya.OpenMayaUI as MayaUI

"""
    Code template for loading .ui files into Maya courtesy of Brian Kortbus
    http://www.briankortbus.com/single-post/2016/11/09/UI-Files-in-Maya-2016-PySide—Part-2
"""

# Where is this script?
SCRIPT_LOC = os.path.split(__file__)[0]


def loadUiWidget(uifilename, parent=None):
    """Properly Loads and returns UI files – by BarryPye on stackOverflow"""
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


# Call this function inside of Maya to run the script:
def runMayaTemplateUi():
    """Command within Maya to run this script"""
    if not (cmds.window("templateUi", exists=True)):
        TemplateUi()
    else:
        sys.stdout.write("Tool is already open!\n")


class TemplateUi(QtGui.QMainWindow):
    """A bare minimum UI class – showing a .ui file inside Maya 2016"""

    def __init__(self):
        mainUI = SCRIPT_LOC + "\\qtDesignerDoc.ui"
        MayaMain = shiboken.wrapInstance(long(MayaUI.MQtUtil.mainWindow()), QtGui.QWidget)
        super(TemplateUi, self).__init__(MayaMain)

        # main window load / settings
        self.MainWindowUI = loadUiWidget(mainUI, MayaMain)
        self.MainWindowUI.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.MainWindowUI.destroyed.connect(self.onExitCode)
        self.MainWindowUI.show()

        self.makeConnections()

    def makeConnections(self):
        # the lambda: is (in my words) a handy way to pass an argument to our function without python running it.
        self.MainWindowUI.addCube_btn.clicked.connect(lambda: self.someFunction("I'm a function!"))

    def onExitCode(self):
        """Do this when the script is closed"""
        sys.stdout.write("UI successfully closed\n")

    def someFunction(self, someArg):
        print someArg