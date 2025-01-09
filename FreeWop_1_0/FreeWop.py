import FreeCAD, FreeCADGui
from importlib import reload
import corpus_form
import groove_form
import drilling_form
import board_form
import pocket_form
import mpr
import scx
import Workpiece
import shape_export
import cutlist

import os, sys
import fakesmodule
import shared
import config


path = os.path.dirname(fakesmodule.__file__)
iconPath = os.path.join(path, "Icons")
configfile = os.path.join(path, "config.ini")

shared.drill_template=['Drilling',20,20,0,'Top',6,10,True,150,6,32,0,False,False,False,'1',True]
shared.corpus_template=['Corpus',600,400,300,18,18,18,18,0,0,0,0,0,0]
shared.groove_template=['Grooving',0,0,500,100,10,8,'No','Top','1',45,True,'surface']
shared.pocket_template=['Pocket','Top',0,0,199,100,10,0,15,0.8,'ccw',False,80,'1']
shared.mpr_template=['fgdfgdfg','afasdfasd']

FreeCADGui.runCommand('Std_DrawStyle',6)

class ScriptCmd: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Corpus')
       reload(corpus_form)
       reload(Workpiece)
       corpus_form.add_corpus()
   def GetResources(self):
       Icon = os.path.join(iconPath, "Corpus.png")
       return {'Pixmap' : Icon, 'MenuText': 'Corpus', 'ToolTip': 'Build a corpus'} 

class ScriptCmd3: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Drill')
       reload(drilling_form)
       drilling_form.add_drilling()
   def GetResources(self):
       Icon = os.path.join(iconPath, "Drill.png")
       return {'Pixmap' : Icon, 'MenuText': 'Drill', 'ToolTip': 'Make drillings'}

class ScriptCmd4: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Groove')
       reload(groove_form)
       groove_form.add_groove()
   def GetResources(self):
       Icon = os.path.join(iconPath, "Groove.png")
       return {'Pixmap' : Icon, 'MenuText': 'Groove', 'ToolTip': 'Grooving'}

class ScriptCmd2: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Board')
       reload(board_form)
       board_form.add_board()
   def GetResources(self):
       Icon = os.path.join(iconPath, "Board.png")
       return {'Pixmap' : Icon, 'MenuText': 'Board', 'ToolTip': 'Build single boards'}

class ScriptCmd5: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Pocket')
       reload(pocket_form)
       pocket_form.add_pocket()
   def GetResources(self):
       Icon = os.path.join(iconPath, "Pocket.png")
       return {'Pixmap' : Icon, 'MenuText': 'Pocket', 'ToolTip': 'Pockets'}

class ScriptCmd6: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Create_mpr')
       reload(mpr)
       #mpr.run_mpr()
       mpr.test_Boards()
   def GetResources(self):
       Icon = os.path.join(iconPath, "code_1.png")
       return {'Pixmap' : Icon, 'MenuText': 'Run mpr-post', 'ToolTip': 'whole corpus or single board'}

class ScriptCmd7: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('3D_Export')
       reload(shape_export)
       shape_export.make_shape()
   def GetResources(self):
       Icon = os.path.join(iconPath, "3D.png")
       return {'Pixmap' : Icon, 'MenuText': '3D_Export', 'ToolTip': 'whole corpus or single board'}

class ScriptCmd8: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Cutlist')
       reload(cutlist)
       cutlist.cutlist()
   def GetResources(self):
       Icon = os.path.join(iconPath, "List.png")
       return {'Pixmap' : Icon, 'MenuText': 'Cutlist', 'ToolTip': 'More detailed text'}
       
class ScriptCmd9: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Create_scx')
       reload(scx)
       #mpr.run_mpr()
       scx.test_Boards()
   def GetResources(self):
       Icon = os.path.join(iconPath, "code_2.png")
       return {'Pixmap' : Icon, 'MenuText': 'Run scx-post', 'ToolTip': 'whole corpus or single board'}




config.configread_corpus()
config.configread_drill()
config.configread_groove()
config.configread_pocket()
config.configread_mpr()



FreeCADGui.addCommand('Script_Cmd', ScriptCmd())
FreeCADGui.addCommand('Script_Cmd2', ScriptCmd2())
FreeCADGui.addCommand('Script_Cmd3', ScriptCmd3())
FreeCADGui.addCommand('Script_Cmd4', ScriptCmd4())
FreeCADGui.addCommand('Script_Cmd5', ScriptCmd5())
FreeCADGui.addCommand('Script_Cmd6', ScriptCmd6())
FreeCADGui.addCommand('Script_Cmd7', ScriptCmd7())
FreeCADGui.addCommand('Script_Cmd8', ScriptCmd8())
FreeCADGui.addCommand('Script_Cmd9', ScriptCmd9())





