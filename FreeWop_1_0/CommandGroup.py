import FreeCADGui
import os
import fakesmodule



class CommandGroup:
    def __init__(self, cmdlist, menu, TypeId=None, tooltip=None):
        self.cmdlist = cmdlist
        self.menu = menu
        self.TypeId = TypeId
        if tooltip is None:
            self.tooltip = menu
        else:
            self.tooltip = tooltip

    def GetCommands(self):
        return tuple(self.cmdlist)

    def GetResources(self):
        #return {'MenuText': self.menu, 'ToolTip': self.tooltip}

        path = os.path.dirname(fakesmodule.__file__)
        iconPath = os.path.join(path, "Icons")


        return {"MenuText": self.menu, 
                "ToolTip": "Generate machine programs",
                "Pixmap": os.path.join(iconPath, "code.png")
                       
        }

commandList= ['Script_Cmd6', 'Script_Cmd9']

commandList2= ['Script_Cmd9', 'Script_Cmd6']

FreeCADGui.addCommand('post',CommandGroup(commandList, 'Postprocessors for machines'))

FreeCADGui.addCommand('post2',CommandGroup(commandList2, 'Postprocessors for machines'))
