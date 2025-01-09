# -*- coding: utf-8 -*-
# FreeWop cabinet workbench for FreeCAD
# (c) 2024 Frank Matzer
#***************************************************************************
#*   (c) Frank Matzer 2024 ; www.cadialog.com                              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License (GPL)            *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/


import FreeCAD as App
if App.GuiUp:
    import FreeCADGui as Gui

import Part
from FreeCAD import Base
import math
from PySide import QtGui, QtCore
from AttachmentEditor import Commands
import shared
import config

__title__ = "FreeWop"
__author__ = "Frank Matzer"
__url__ = "https://www.cadialog.com"
__doc__ = "Board class with dialog"

MSG = App.Console.PrintMessage

class Pocket_Form(QtGui.QWidget):


   def __init__(self, fr_obj) :

      super().__init__()
      self.setWindowTitle("Pocket : "+fr_obj.Name)
      dispo = QtGui.QGridLayout(self)
      ui=Gui.UiLoader()

      dispo.addWidget(QtGui.QLabel('Side of processing', self), 1, 0)
      self.Drilldirection = QtGui.QComboBox(self)
      self.Drilldirection.addItems(['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom'])
      self.Drilldirection.setToolTip("Choose on which side should be the pocket,\nif You look on the side, zero is left bottom")
      dispo.addWidget(self.Drilldirection,1,1)
      self.Drilldirection.setCurrentText(fr_obj.Drilldirection)

      #dispo.addWidget(QtGui.QLabel("corner_or_middle", self),1,0)        
      #self.corner_or_middle = QtGui.QCheckBox(self)
      #dispo.addWidget(self.corner_or_middle, 1, 1)   
      #self.corner_or_middle.setChecked(fr_obj.corner_or_middle)		
      '''
      dispo.addWidget(QtGui.QLabel("overlap %", self),8,0)        
      self.overlap = ui.createWidget("Gui::QuantitySpinBox")
      self.overlap.setToolTip("overlap %")
      self.overlap.setProperty("minimum", 0.0)
      self.overlap.setProperty("maximum", 5000.0)
      self.overlap.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.overlap, 8, 1)   
      self.overlap.setProperty('rawValue',fr_obj.overlap)      
      Gui.ExpressionBinding(self.overlap).bind(fr_obj,"overlap")
      
      '''
      
      dispo.addWidget(QtGui.QLabel("X", self),2,0)        
      self.X = ui.createWidget("Gui::QuantitySpinBox")
      self.X.setToolTip("X of the pocket")
      self.X.setProperty("minimum", 0.0)
      self.X.setProperty("maximum", 5000.0)
      self.X.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.X, 2, 1)   
      self.X.setProperty('rawValue',fr_obj.X)      
      Gui.ExpressionBinding(self.X).bind(fr_obj,"X")

      dispo.addWidget(QtGui.QLabel("Y", self),3,0)        
      self.Y = ui.createWidget("Gui::QuantitySpinBox")
      self.Y.setToolTip("X of the pocket")
      self.Y.setProperty("minimum", 0.0)
      self.Y.setProperty("maximum", 5000.0)
      self.Y.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Y, 3, 1)   
      self.Y.setProperty('rawValue',fr_obj.X)      
      Gui.ExpressionBinding(self.Y).bind(fr_obj,"Y")

      dispo.addWidget(QtGui.QLabel("Angle", self),4,0) 
      self.Angle = QtGui.QDoubleSpinBox(self)
      self.Angle.setToolTip("Angle")
      self.Angle.setDecimals(2)
      self.Angle.setMinimum(0)
      self.Angle.setMaximum(360.0)
      self.Angle.setSingleStep(0.1)
      dispo.addWidget(self.Angle, 4, 1)   
      self.Angle.setValue(fr_obj.Angle)	
	
      dispo.addWidget(QtGui.QLabel("Pocket_length", self),5,0)        
      self.Pocket_length = ui.createWidget("Gui::QuantitySpinBox")
      self.Pocket_length.setToolTip("Length of the pocket")
      self.Pocket_length.setProperty("minimum", 0.0)
      self.Pocket_length.setProperty("maximum", 5000.0)
      self.Pocket_length.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Pocket_length, 5, 1)   
      self.Pocket_length.setProperty('rawValue',fr_obj.Pocket_length)      
      Gui.ExpressionBinding(self.Pocket_length).bind(fr_obj,"Pocket_length")
      
      dispo.addWidget(QtGui.QLabel("Pocket_width", self),6,0)        
      self.Pocket_width = ui.createWidget("Gui::QuantitySpinBox")
      self.Pocket_width.setToolTip("Width of the pocket")
      self.Pocket_width.setProperty("minimum", 0.0)
      self.Pocket_width.setProperty("maximum", 5000.0)
      self.Pocket_width.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Pocket_width, 6, 1)   
      self.Pocket_width.setProperty('rawValue',fr_obj.Pocket_width)      
      Gui.ExpressionBinding(self.Pocket_width).bind(fr_obj,"Pocket_width")      

      dispo.addWidget(QtGui.QLabel("Pocket_depth", self),7,0)        
      self.Depth = ui.createWidget("Gui::QuantitySpinBox")
      self.Depth.setToolTip("Depth of the pocket")
      self.Depth.setProperty("minimum", 0.0)
      self.Depth.setProperty("maximum", 5000.0)
      self.Depth.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Depth, 7, 1)   
      self.Depth.setProperty('rawValue',fr_obj.Depth)      
      Gui.ExpressionBinding(self.Depth).bind(fr_obj,"Depth")

      dispo.addWidget(QtGui.QLabel("Pocket_radius", self),8,0)        
      self.pr = ui.createWidget("Gui::QuantitySpinBox")
      self.pr.setToolTip("Depth of the pocket")
      self.pr.setProperty("minimum", 0.0)
      self.pr.setProperty("maximum", 5000.0)
      self.pr.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.pr, 8, 1)   
      self.pr.setProperty('rawValue',fr_obj.pr)      
      Gui.ExpressionBinding(self.pr).bind(fr_obj,"pr")

      dispo.addWidget(QtGui.QLabel("deep_infeed", self),9,0)        
      self.deep_infeed = ui.createWidget("Gui::QuantitySpinBox")
      self.deep_infeed.setToolTip("Deep infeed")
      self.deep_infeed.setProperty("minimum", 0.0)
      self.deep_infeed.setProperty("maximum", 5000.0)
      self.deep_infeed.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.deep_infeed, 9, 1)   
      self.deep_infeed.setProperty('rawValue',fr_obj.deep_infeed)      
      Gui.ExpressionBinding(self.deep_infeed).bind(fr_obj,"deep_infeed")
		
      dispo.addWidget(QtGui.QLabel("overlap %", self),10,0)        
      self.overlap = ui.createWidget("Gui::QuantitySpinBox")
      self.overlap.setToolTip("overlap %")
      self.overlap.setProperty("minimum", 0.0)
      self.overlap.setProperty("maximum", 5000.0)
      self.overlap.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.overlap, 10, 1)   
      self.overlap.setProperty('rawValue',fr_obj.overlap)      
      Gui.ExpressionBinding(self.overlap).bind(fr_obj,"overlap")


      dispo.addWidget(QtGui.QLabel('Direction', self), 12, 0)
      self.Direction = QtGui.QComboBox(self)
      self.Direction.addItems(['cw','ccw'])
      dispo.addWidget(self.Direction,12,1)
      self.Direction.setCurrentText(fr_obj.Direction)
		 


      #dispo.addWidget(QtGui.QLabel("Zugehoeringkeit", self),15,0)        
      #self.BelongingID = QtGui.QDoubleSpinBox(self)
      #self.BelongingID.setToolTip("Zugehoeringkeit ")
      #self.BelongingID.setDecimals(0)
      #self.BelongingID.setMinimum(1)
      #self.BelongingID.setMaximum(100000.0)
      #self.BelongingID.setSingleStep(1)
      #dispo.addWidget(self.BelongingID, 15, 1)   
      #self.BelongingID.setValue(fr_obj.BelongingID)

      dispo.addWidget(QtGui.QLabel("Save standard", self),16,0)        
      self.saving = QtGui.QPushButton(self)
      self.saving.setText("Save")
      self.saving.setToolTip("Save parameters to config") #Tool tip
      dispo.addWidget(self.saving, 16, 1)   

   

class Pocket_Form_TaskPanel(QtGui.QWidget):
   
   def __init__(self, fr_obj):

      super().__init__(Gui.getMainWindow(), QtCore.Qt.Tool)
      self.fr_obj = fr_obj      
      self.form = Pocket_Form(fr_obj) 
      self.form.X.valueChanged.connect(self.on_X_valueChanged)
      self.form.Y.valueChanged.connect(self.on_Y_valueChanged)
      self.form.pr.valueChanged.connect(self.on_pr_valueChanged)
      self.form.deep_infeed.valueChanged.connect(self.on_deep_infeed_valueChanged)
      #self.form.corner_or_middle.toggled.connect(self.on_corner_or_middle_toggled)
      self.form.Pocket_length.valueChanged.connect(self.on_Pocket_length_valueChanged)
      self.form.overlap.valueChanged.connect(self.on_overlap_valueChanged)
      self.form.Angle.valueChanged.connect(self.on_Angle_valueChanged)
      self.form.Depth.valueChanged.connect(self.on_Depth_valueChanged)
      self.form.Pocket_width.valueChanged.connect(self.on_Pocket_width_valueChanged)
      self.form.Direction.currentIndexChanged.connect(self.on_Direction_valueChanged)
      self.form.Drilldirection.currentIndexChanged.connect(self.on_Drilldirection_valueChanged)

      #self.form.BelongingID.valueChanged.connect(self.on_BelongingID_valueChanged)
      self.form.saving.clicked.connect(self.on_saving_clicked)
          
   def getStandardButtons(self):
      """
      DÃ©finition des boutons Ok / Cancel 
      """
      #return int(QtGui.QDialogButtonBox.Cancel) | int(QtGui.QDialogButtonBox.Ok)
      return int(QtGui.QDialogButtonBox.Ok) | int(QtGui.QDialogButtonBox.Cancel)| int(QtGui.QDialogButtonBox.Apply)

   def accept(self):
      self.finish()
   
   def reject(self):
      self.fr_obj.Document.removeObject(self.fr_obj.Name)
      self.finish()
        
   def finish(self):
        Gui.Control.closeDialog()
        Gui.ActiveDocument.resetEdit()
   def on_X_valueChanged(self,state):
      self.fr_obj.X=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Y_valueChanged(self,state):
      self.fr_obj.Y=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_pr_valueChanged(self,state):
      self.fr_obj.pr=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_deep_infeed_valueChanged(self,state):
      self.fr_obj.deep_infeed=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_overlap_valueChanged(self,state):
      self.fr_obj.overlap=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Depth_valueChanged(self,state):
      self.fr_obj.Depth=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Pocket_width_valueChanged(self,state):
      self.fr_obj.Pocket_width=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Drilldirection_valueChanged(self,state):
      self.fr_obj.Drilldirection=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_BelongingID_valueChanged(self,state):
      self.fr_obj.BelongingID=int(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Angle_valueChanged(self,state):
      self.fr_obj.Angle=state
      self.fr_obj.Document.recompute()  
   def on_corner_or_middle_toggled(self,state):
      self.fr_obj.corner_or_middle=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()
   def on_Pocket_length_valueChanged(self,state):
      self.fr_obj.Pocket_length=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Direction_valueChanged(self,state):
      self.fr_obj.Direction=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()
		
   def on_saving_clicked(self,state):
      config.configwrite_pocket()	
      #print('save')

class ViewProviderPocket:


   def __init__(self, vobj):
     """
     Set this object to the proxy object of the actual view provider
     """
     vobj.Proxy = self

     vobj.hide()
     vobj.show()
     vobj.ShapeColor=(0.6,0.0,0.7)    
     vobj.Transparency = 10
   def attach(self, vobj):
     """
     Setup the scene sub-graph of the view provider, this method is mandatory
     """
     return

   def setEdit(self, vobj, mode=0):
      Gui.Control.showDialog(Pocket_Form_TaskPanel(vobj.Object))	#setzt den Dialog in die ComboBox
      return True

   def unsetEdit(self,vobj,mode=0):
      Gui.Control.closeDialog()

   def getIcon(self):
     """
     Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
     """
     return """
         /* XPM */
static char *_1db616930d5423e8684d19f1e00f4c42J6md11f0o02YGm4[] = {
/* columns rows colors chars-per-pixel */
"16 16 39 1 ",
"  c #7E0000",
". c #694757",
"X c #5D696C",
"o c #66767A",
"O c gray50",
"+ c #970000",
"@ c #980000",
"# c #A40000",
"$ c #BD0000",
"% c #85262C",
"& c #81333B",
"* c #B7262C",
"= c #CA0000",
"- c #C70E0F",
"; c #9A4757",
": c #9B4757",
"> c #306C83",
", c #4D7291",
"< c #737291",
"1 c #2687AE",
"2 c #2688AF",
"3 c #308AAE",
"4 c #398EAF",
"5 c #438EBD",
"6 c #139FDA",
"7 c #1F9FDA",
"8 c #209ED9",
"9 c #0AA5E7",
"0 c #00A2E8",
"q c #0AA5E8",
"w c #26B0E8",
"e c #30B3E9",
"r c #9F9F9F",
"t c gray75",
"y c #C0C0C0",
"u c #D0D0D0",
"i c #DFDFDF",
"p c #EFEFEF",
"a c None",
/* pixels */
"aaaaaaaaaaaaaaaa",
"aaittttttttttpaa",
"aaO422222222>yaa",
"aaOw000000001yaa",
"aaOw00,500001yaa",
"aaOw0<@-50001yaa",
"aaOw<=+=-5001yaa",
"aaOe.+@#=-501yaa",
"aa;eq:=$#=-51yaa",
"aa5e0q;=$ @&3yaa",
"aa5e00q;=@*71yaa",
"aa;w000q;%801yaa",
"aaOw000096001yaa",
"aaOw000000001yaa",
"aaroooooooooXuaa",
"aaaaaaaaaaaaaaaa"
};
         """
   
   def __getstate__(self):
     """
     Called during document saving.
     """
     return None
   
   def __setstate__(self,state):
     """
     Called during document restore.
     """
     return None
   

class Pocket:

   def __init__(self, obj,dir,spx,spy,pl,pw,pd,angle,pr,dinf,dr,cm,ov,cond,bid):
        self.Type = 'Pocket'
        obj.Proxy = self
        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = "pocket"
        obj.addProperty('App::PropertyFloat', 'Pocket_width', 'Dimensions', 'Pocket_width')
        obj.addProperty("App::PropertyBool", "corner_or_middle", "Dimensions","Base" "corner_or_middle")
        obj.addProperty('App::PropertyFloat', 'Pocket_length', 'Dimensions', 'Pocket_length')
        obj.addProperty('App::PropertyFloat', 'Depth', 'Dimensions', 'Depth')
        obj.addProperty('App::PropertyFloat', 'X', 'Dimensions', 'X')
        obj.addProperty('App::PropertyFloat', 'Y', 'Dimensions', 'Y')
        obj.addProperty('App::PropertyFloat', 'pr', 'Dimensions', 'pr')
        obj.addProperty('App::PropertyFloat', 'deep_infeed', 'Dimensions', 'deep_infeed')
        obj.addProperty('App::PropertyFloat', 'Width', 'Dimensions', 'Width')
        obj.addProperty("App::PropertyVectorList","Holes")
        obj.addProperty("App::PropertyEnumeration","Drilldirection","Base","Drilldirection").Drilldirection=['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom']
        obj.addProperty("App::PropertyEnumeration","Direction","Base","Direction").Direction=['cw','ccw']
        obj.addProperty('App::PropertyFloat', 'overlap', 'Dimensions', 'overlap') 
        obj.addProperty("App::PropertyAngle", "Angle", "Dimensions","Base" "Angle of pocket")
        obj.addProperty("App::PropertyString", "Condition", "Dimensions","Base" "Condition")
        obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")
        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 25
        obj.overlap=ov
        obj.X=spx
        obj.Y=spy
        obj.Angle='0.00 deg'
        obj.pr=pr
        obj.deep_infeed=dinf
        obj.Pocket_length=pl
        obj.Depth=pd
        obj.Drilldirection=dir
        obj.Pocket_width=pw
        obj.corner_or_middle=cm
        obj.Drilldirection=dir
        obj.Direction=dr
        obj.Condition=cond
        obj.BelongingID=bid
        obj.addExtension('Part::AttachExtensionPython', obj)

        direction=App.Vector(0,1,0)
        rowdirection=App.Vector(0,0,1)
        obj.Holes=[]
        obj.recompute()
        ViewProviderPocket(obj.ViewObject)
        App.ActiveDocument.recompute()

        
   def execute(self, obj):
        """
        Called on document recompute
        """
        import FreeCAD as App
        import math
        import Draft
        import Part

        l=obj.Pocket_length
        b=obj.Pocket_width
        r=obj.pr
        ti=obj.Depth
        wi=obj.Angle
        #px=obj.X
        #py=obj.Y
		
        if obj.corner_or_middle==True:
         #px=obj.X+obj.Pocket_length/2
         #py=obj.Y+obj.Pocket_width/2
         px=obj.X
         py=obj.Y
         korx=obj.X
         kory=obj.Y
			

         korx=obj.X+obj.Pocket_length/2
         kory=obj.Y+obj.Pocket_width/2
			
        if obj.corner_or_middle==False:
         px=obj.X
         py=obj.Y
         korx=0
         kory=0
		
        for objs in App.ActiveDocument.Objects:
            if objs.ID==obj.BelongingID:
              aa=objs.Length
              bb=objs.Width
              cc=objs.Height
              wpl=float(aa)
              wpw=float(bb)
              wph=float(cc)
              wp=objs
              lab=objs.Label
        obj.Label = lab+"_Pocket_"+obj.Drilldirection				
        if obj.Drilldirection=="Top":
         obj.AttachmentSupport = [(wp,'Vertex1'),(wp,'Vertex5'),(wp,'Vertex3')]
        if obj.Drilldirection=="Front+Y":
         obj.AttachmentSupport = [(wp,'Vertex2'),(wp,'Vertex6'),(wp,'Vertex1')]
        if obj.Drilldirection=="Bottom":
         obj.AttachmentSupport = [(wp,'Vertex4'),(wp,'Vertex8'),(wp,'Vertex2')]
        if obj.Drilldirection=="Rear-Y":
         obj.AttachmentSupport = [(wp,'Vertex8'),(wp,'Vertex4'),(wp,'Vertex7')]
        if obj.Drilldirection=="Left+X":
         obj.AttachmentSupport = [(wp,'Vertex4'),(wp,'Vertex2'),(wp,'Vertex3')]
        if obj.Drilldirection=="Right-X":
         obj.AttachmentSupport = [(wp,'Vertex6'),(wp,'Vertex8'),(wp,'Vertex5')]

        if obj.corner_or_middle==False:		
         obj.AttachmentOffset = App.Placement(App.Vector(px,py,0),App.Rotation(App.Vector(0.00,0.00,1.00),wi))		
        if obj.corner_or_middle==True:		
         #obj.AttachmentOffset = App.Placement(App.Vector(obj.X/2,obj.Y/2,0),App.Rotation(App.Vector(0.00,0.00,1.00),wi))
         obj.AttachmentOffset = App.Placement(App.Vector(px,py,0),App.Rotation(App.Vector(0.00,0.00,1.00),wi))

		
        obj.MapPathParameter = 0.000000
        obj.MapMode = 'OXY'
        shared.pocket_template=[obj.Description,obj.Drilldirection,obj.X,obj.Y,obj.Pocket_length,obj.Pocket_width,obj.Depth,obj.Angle,obj.pr,obj.deep_infeed,obj.Direction,obj.corner_or_middle,obj.overlap,obj.Condition]
        #print('shared')	
        #print (shared.pocket_template[:])
        d=r*math.sin(math.radians(45))
        pl = App.Placement()

        p1=App.Vector(l/2+korx,b/2-r+kory,0)
        p2=App.Vector(l/2-r+korx,b/2-r+kory,0)
        p3=App.Vector(l/2-r+korx,b/2+kory,0)
        p4=App.Vector(-l/2+r+korx,b/2+kory,0)
        p5=App.Vector(-l/2+r+korx,b/2-r+kory,0) 
        p6=App.Vector(-l/2+korx,b/2-r+kory,0)
        p7=App.Vector(-l/2+korx,-b/2+r+kory,0)
        p8=App.Vector(-l/2+r+korx,-b/2+r+kory,0)
        p9=App.Vector(-l/2+r+korx,-b/2+kory,0)
        p10=App.Vector(l/2-r+korx,-b/2+kory,0)
        p11=App.Vector(l/2-r+korx,-b/2+r+kory,0)
        p12=App.Vector(l/2+korx,-b/2+r+kory,0)

        A=App.Vector(l/2-r+d+korx,b/2-r+d+kory,0)
        B=App.Vector(-l/2+r-d+korx,b/2-r+d+kory,0) 
        C=App.Vector(-l/2+r-d+korx,-b/2+r-d+kory,0)
        D=App.Vector(l/2-r+d+korx,-b/2+r-d+kory,0)


        lin1=Part.LineSegment(p3, p4)
        lin2=Part.LineSegment(p6, p7)
        lin3=Part.LineSegment(p9, p10)
        lin4=Part.LineSegment(p12, p1)
		
        parc1=Part.Arc(p1,A,p3)
        parc2=Part.Arc(p4,B,p6)
        parc3=Part.Arc(p7,C,p9)
        parc4=Part.Arc(p10,D,p12)

        S1=Part.Shape([lin1,parc2,lin2,parc3,lin3,parc4,lin4,parc1])
        W = Part.Wire(S1.Edges)
        W1=Part.Face(W)
        P = W1.extrude(App.Vector(0, 0, -ti))
        #Part.show(P)
        obj.Shape=P
        
		

def create_Pocket(obj_name,dir,spx,spy,pl,pw,pd,angle,pr,dinf,dr,cm,ov,cond,bid):
 
    docActif = App.ActiveDocument
    if docActif == None: docActif = App.newDocument()
    fr_obj = docActif.addObject('Part::FeaturePython', obj_name)


    Pocket(fr_obj,dir,spx,spy,pl,pw,pd,angle,pr,dinf,dr,cm,ov,cond,bid)
    docActif.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.Control.showDialog(Pocket_Form_TaskPanel(fr_obj))

    return



def add_pocket():
    sel = Gui.Selection.getSelection()
    list1 = []
    list2 = []
    test=[]
    for obj in sel:
        #if obj.Visibility==True:
          list1.append(obj.ComponentID)
          list2.append(obj.ID)
          test.append(obj)
    #print(list1)

    if (10 not in list1) or len(list1)>1:
     print(' No relevant part is selected, please select a Board')
    else:
     #print (test[0].ID)
     #create_Pocket('Pocket','Top',0,0,200,100,10,0,15,0.8,'ccw',False,80,'1',test[0].ID)
	
     pt=shared.pocket_template[:]	
     pt.append(test[0].ID)
     #print(pt[:])
     create_Pocket(*pt)
		
     #print (test[0].Label)
    #App.ActiveDocument.getObject(test[0].Label).adjustRelativeLinks(App.ActiveDocument.getObject('Part'))
    
     dd=App.ActiveDocument.getObject(test[0].Label).Parents
     ddn=dd[0][0]
     #print(ddn.Name)
     App.ActiveDocument.getObject(ddn.Name).addObject(App.ActiveDocument.getObject(test[0].Label))
    docActif = App.ActiveDocument
    docActif.recompute()
