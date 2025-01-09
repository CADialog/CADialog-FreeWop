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
from importlib import reload
import shared
import config

__title__ = "FreeWop"
__author__ = "Frank Matzer"
__url__ = "https://www.cadialog.com"
__doc__ = "Board class with dialog"

MSG = App.Console.PrintMessage

class Drilling_Form(QtGui.QWidget):


   def __init__(self, fr_obj) :

      super().__init__()
      self.setWindowTitle("Drilling : "+fr_obj.Name)
      dispo = QtGui.QGridLayout(self)
      ui=Gui.UiLoader()


      dispo.addWidget(QtGui.QLabel('Side of processing', self), 0, 0)
      self.Drilldirection = QtGui.QComboBox(self)
      self.Drilldirection.setToolTip("Choose on which side should be drilled,\nif You look on the side, zero is left bottom,\nthe mirror functions turn this")
      self.Drilldirection.addItems(['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom'])
      dispo.addWidget(self.Drilldirection,0,1)
      self.Drilldirection.setCurrentText(fr_obj.Drilldirection)

      dispo.addWidget(QtGui.QLabel("Diameter", self),1,0)        
      self.Diameter = ui.createWidget("Gui::QuantitySpinBox")
      self.Diameter.setToolTip("Diameter of the hole(s)")
      self.Diameter.setProperty("minimum", 0.0)
      self.Diameter.setProperty("maximum", 5000.0)
      self.Diameter.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Diameter, 1, 1)   
      self.Diameter.setProperty('rawValue',fr_obj.Diameter)      
      Gui.ExpressionBinding(self.Diameter).bind(fr_obj,"Diameter")

      dispo.addWidget(QtGui.QLabel("Number", self),2,0)        
      self.Anzahl = ui.createWidget("Gui::QuantitySpinBox")
      self.Anzahl.setToolTip("Number of the drillings")
      self.Anzahl.setProperty("minimum", 0)
      self.Anzahl.setProperty("maximum", 500)
      self.Anzahl.setProperty("setSingleStep" , 1)
      dispo.addWidget(self.Anzahl, 2, 1)   
      self.Anzahl.setProperty('rawValue',fr_obj.Anzahl)      
      Gui.ExpressionBinding(self.Anzahl).bind(fr_obj,"Anzahl")
      
      dispo.addWidget(QtGui.QLabel("Start X", self),3,0)        
      self.StartX = ui.createWidget("Gui::QuantitySpinBox")
      self.StartX.setToolTip("Start X-Position depend on drilldirection and mirroring")
      self.StartX.setProperty("minimum", 0.0)
      self.StartX.setProperty("maximum", 5000.0)
      self.StartX.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.StartX, 3, 1)   
      self.StartX.setProperty('rawValue',fr_obj.StartX)      
      Gui.ExpressionBinding(self.StartX).bind(fr_obj,"StartX")

      dispo.addWidget(QtGui.QLabel("Start Y", self),4,0)        
      self.StartY = ui.createWidget("Gui::QuantitySpinBox")
      self.StartY.setToolTip("Start Y-Position depend on drilldirection and mirroring")
      self.StartY.setProperty("minimum", 0.0)
      self.StartY.setProperty("maximum", 5000.0)
      self.StartY.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.StartY, 4, 1)   
      self.StartY.setProperty('rawValue',fr_obj.StartY)      
      Gui.ExpressionBinding(self.StartY).bind(fr_obj,"StartY")
      
      dispo.addWidget(QtGui.QLabel("drilling-depth", self),5,0)        
      self.Depth = ui.createWidget("Gui::QuantitySpinBox")
      self.Depth.setToolTip("Depth of the drilling(s)")
      self.Depth.setProperty("minimum", 0.0)
      self.Depth.setProperty("maximum", 5000.0)
      self.Depth.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Depth, 5, 1)   
      self.Depth.setProperty('rawValue',fr_obj.Depth)      
      Gui.ExpressionBinding(self.Depth).bind(fr_obj,"Depth")

      dispo.addWidget(QtGui.QLabel("drilling-distance", self),6,0)        
      self.Abstand = ui.createWidget("Gui::QuantitySpinBox")
      self.Abstand.setToolTip("Distance of the drilling(s)")
      self.Abstand.setProperty("minimum", 0.0)
      self.Abstand.setProperty("maximum", 5000.0)
      self.Abstand.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Abstand, 6, 1)   
      self.Abstand.setProperty('rawValue',fr_obj.Abstand)      
      Gui.ExpressionBinding(self.Abstand).bind(fr_obj,"Abstand")

      '''     
      dispo.addWidget(QtGui.QLabel("Angle", self),7,0)        
      self.Angle = ui.createWidget("Gui::QuantitySpinBox")
      self.Angle.setToolTip("Angle of the drillings")
      self.Angle.setProperty("minimum", 0.0)
      self.Angle.setProperty("maximum", 360.0)
      self.Angle.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Angle, 7, 1)   
      self.Angle.setProperty('rawValue',fr_obj.Angle)      
      Gui.ExpressionBinding(self.Angle).bind(fr_obj,"Angle")
      '''
      
      dispo.addWidget(QtGui.QLabel("Angle", self),7,0)        
      self.Angle = QtGui.QDoubleSpinBox(self)
      self.Angle.setToolTip("Angle of the drill-row")
      self.Angle.setDecimals(2)
      self.Angle.setMinimum(0)
      self.Angle.setMaximum(360.0)
      self.Angle.setSingleStep(0.1)
      dispo.addWidget(self.Angle, 7, 1)   
      self.Angle.setValue(fr_obj.Angle)

      dispo.addWidget(QtGui.QLabel("Number or Length", self),8,0)        
      self.Anzahl_oder_Laenge = QtGui.QCheckBox(self)
      self.Anzahl_oder_Laenge.setToolTip("Number or length is defining the drill-row,\nchecked means numbers")
      dispo.addWidget(self.Anzahl_oder_Laenge, 8, 1)   
      self.Anzahl_oder_Laenge.setChecked(fr_obj.Anzahl_oder_Laenge)

      dispo.addWidget(QtGui.QLabel("Length of row", self),9,0)        
      self.Laenge = ui.createWidget("Gui::QuantitySpinBox")
      self.Laenge.setToolTip("Length of row if more than one and checkbox is checked")
      self.Laenge.setProperty("minimum", 0.0)
      self.Laenge.setProperty("maximum", 5000.0)
      self.Laenge.setProperty("setSingleStep" , 0.1)
      dispo.addWidget(self.Laenge, 9, 1)   
      self.Laenge.setProperty('rawValue',fr_obj.Laenge)      
      Gui.ExpressionBinding(self.Laenge).bind(fr_obj,"Laenge")

      dispo.addWidget(QtGui.QLabel("MiddlePoint", self),10,0)
      self.MiddlePoint = QtGui.QCheckBox(self)
      self.MiddlePoint.setToolTip("if checked, Start X/Y is the middle of the row")
      dispo.addWidget(self.MiddlePoint, 10, 1)   
      self.MiddlePoint.setChecked(fr_obj.MiddlePoint)

      dispo.addWidget(QtGui.QLabel("MirrorX", self),11,0)        
      self.MirrorX = QtGui.QCheckBox(self)
      self.MirrorX.setToolTip("if checked, mirrored in X-direction")
      dispo.addWidget(self.MirrorX, 11, 1)   
      self.MirrorX.setChecked(fr_obj.MirrorX)

      dispo.addWidget(QtGui.QLabel("MirrorY", self),12,0)        
      self.MirrorY = QtGui.QCheckBox(self)
      self.MirrorY.setToolTip("if checked, mirrored in Y-direction")
      dispo.addWidget(self.MirrorY, 12, 1)   
      self.MirrorY.setChecked(fr_obj.MirrorY)

      dispo.addWidget(QtGui.QLabel("Save standard", self),14,0)        
      self.saving = QtGui.QPushButton(self)
      self.saving.setText("Save")
      self.saving.setToolTip("Save parameters to config") #Tool tip
      dispo.addWidget(self.saving, 14, 1)   

		




class Drilling_Form_TaskPanel(QtGui.QWidget):
   
   def __init__(self, fr_obj):

      super().__init__(Gui.getMainWindow(), QtCore.Qt.Tool)
      self.fr_obj = fr_obj      
      self.form = Drilling_Form(fr_obj) 
      self.form.Depth.valueChanged.connect(self.on_Depth_valueChanged) 
      self.form.Abstand.valueChanged.connect(self.on_Abstand_valueChanged)
      self.form.Laenge.valueChanged.connect(self.on_Laenge_valueChanged)
      self.form.Angle.valueChanged.connect(self.on_Angle_valueChanged)
      self.form.StartX.valueChanged.connect(self.on_StartX_valueChanged)
      self.form.StartY.valueChanged.connect(self.on_StartY_valueChanged)
      self.form.Anzahl.valueChanged.connect(self.on_Anzahl_valueChanged)
      self.form.Diameter.valueChanged.connect(self.on_Diameter_valueChanged)
      self.form.MiddlePoint.toggled.connect(self.on_MiddlePoint_toggled)
      self.form.Anzahl_oder_Laenge.toggled.connect(self.on_Anzahl_oder_Laenge_toggled)
      self.form.MirrorX.toggled.connect(self.on_MirrorX_toggled)
      self.form.MirrorY.toggled.connect(self.on_MirrorY_toggled)
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
           
   def on_Depth_valueChanged(self,state):
      self.fr_obj.Depth=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Abstand_valueChanged(self,state):
      self.fr_obj.Abstand=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Laenge_valueChanged(self,state):
      self.fr_obj.Laenge=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Angle_valueChanged(self,state):
      self.fr_obj.Angle=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_StartX_valueChanged(self,state):
      self.fr_obj.StartX=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_StartY_valueChanged(self,state):
      self.fr_obj.StartY=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Anzahl_valueChanged(self,state):
      self.fr_obj.Anzahl=int(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Diameter_valueChanged(self,state):
      self.fr_obj.Diameter=float(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_MiddlePoint_toggled(self,state):
      self.fr_obj.MiddlePoint=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Anzahl_oder_Laenge_toggled(self,state):
      self.fr_obj.Anzahl_oder_Laenge=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_MirrorX_toggled(self,state):
      self.fr_obj.MirrorX=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_MirrorY_toggled(self,state):
      self.fr_obj.MirrorY=state
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
   def on_saving_clicked(self,state):
      config.configwrite_drill()	
      #print('save')

class ViewProviderDrilling:


   def __init__(self, vobj):
     """
     Set this object to the proxy object of the actual view provider
     """
     vobj.Proxy = self

     vobj.hide()
     vobj.show()
     vobj.ShapeColor=(1.0,1.0,1.0)    
     vobj.Transparency = 10
   
   def attach(self, vobj):
     """
     Setup the scene sub-graph of the view provider, this method is mandatory
     """
     return

   def setEdit(self, vobj, mode=0):
      Gui.Control.showDialog(Drilling_Form_TaskPanel(vobj.Object))	#setzt den Dialog in die ComboBox
      return True

   def unsetEdit(self,vobj,mode=0):
      Gui.Control.closeDialog()

   def getIcon(self):
     """
     Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
     """
     return """
         /* XPM */
            static const char *RHJpbGxfMTY_[] = {
            /* columns rows colors chars-per-pixel */
            "16 16 5 1 ",
            "  c black",
            ". c #FFF200",
            "X c #10A7DA",
            "o c #00A2E8",
            "O c None",
            /* pixels */
            "OOOOOOOOOOOO OOO",
            "OOOOOOOO     OOO",
            "OOOO    oooo OOO",
            "OOO oooooooo OOO",
            "OOO oooooooo OOO",
            "OOO oo..oooo OOO",
            "OOO oo..oooo OOO",
            "OOO oooooooo OOO",
            "OOO oooooooo OOO",
            "OOO oooo..oX OOO",
            "OOO oooo..oo OOO",
            "OOO ooooooXo OOO",
            "OOO oooooooo OOO",
            "OOO oooooo   OOO",
            "OOO o      OOOOO",
            "OOO   OOOOOOOOOO"
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
   

class Drilling:

   def __init__(self, obj,spx,spy,spz,dir,dia,depth,aol,lae,anz,abst,angle,mirx,miry,mp,cond,sh,bid):
        self.Type = 'Bohrung'
        obj.Proxy = self
        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = "row_of_holes"
        obj.addProperty('App::PropertyFloat', 'Diameter', 'Dimensions', 'Box diameter')
        obj.addProperty('App::PropertyFloat', 'Depth', 'Dimensions', 'Box Depth')
        obj.addProperty("App::PropertyBool", "Anzahl_oder_Laenge", "Dimensions","Base" "Anzahl_oder_Laenge")
        obj.addProperty('App::PropertyFloat', 'Laenge', 'Dimensions', 'Laenge')
        obj.addProperty('App::PropertyInteger', 'Anzahl', 'Dimensions', 'Anzahl')
        obj.addProperty('App::PropertyFloat', 'Abstand', 'Dimensions', 'Abstand')
        obj.addProperty('App::PropertyFloat', 'StartX', 'Dimensions', 'StartX')
        obj.addProperty('App::PropertyFloat', 'StartY', 'Dimensions', 'StartY')
        obj.addProperty("App::PropertyBool", "MiddlePoint", "Dimensions","Base" "Middle-Point of row")
        obj.addProperty("App::PropertyAngle", "Angle", "Dimensions","Base" "Angle of row").Angle='0.00 deg'
        obj.addProperty("App::PropertyVectorList","Holes")
        obj.addProperty("App::PropertyEnumeration","Drilldirection","Base","Drilldirection").Drilldirection=['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom']
        obj.addProperty("App::PropertyBool", "MirrorX", "Dimensions","Base" "Mirror in X Direction")
        obj.addProperty("App::PropertyBool", "MirrorY", "Dimensions","Base" "Mirror in Y Direction")
        obj.addProperty("App::PropertyString", "Condition", "Dimensions","Base" "Condition")
        obj.addProperty("App::PropertyBool", "single_holes", "Dimensions","Base" "single_holes")
        obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")
        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 20
        obj.addProperty("App::PropertyStringList","Speicher","WoodWop","Speicher")
        obj.StartX=spx
        obj.StartY=spy
        obj.Drilldirection=dir
        obj.Diameter=dia
        obj.Depth=depth
        obj.Anzahl_oder_Laenge=aol
        obj.Laenge=lae
        obj.Anzahl=anz
        obj.Abstand=abst
        obj.Angle=angle
        obj.Drilldirection=dir
        obj.MirrorX=mirx
        obj.MirrorY=miry
        obj.MiddlePoint=mp
        obj.Condition=cond
        obj.single_holes=sh
        obj.BelongingID=bid
        
        
        obj.Speicher=[str(spx),str(spy),str(dir),str(dia),str(depth)]

        #Commands.editAttachment(obj)

        obj.addExtension('Part::AttachExtensionPython', obj)

        direction=App.Vector(0,1,0)
        rowdirection=App.Vector(0,0,1)
        obj.Holes=[]
        obj.recompute()
        ViewProviderDrilling(obj.ViewObject)
        App.ActiveDocument.recompute()

        
   def execute(self, obj):
        """
        Called on document recompute
        """
        import FreeCAD as App
        import math
        import Draft

        direction=App.Vector(0,0,-1)
        z=0
        holel=(obj.Anzahl-1)*obj.Abstand
        obj.Holes=[]
        vlist=[]   
        #wpl=float(App.ActiveDocument.getObject('Workpiece').Length)        

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
              #print(lab)
 
        #print(wpl)
        #print(wpw)
        obj.Label= lab+"_Drilling_"+obj.Drilldirection
        obj.Description= lab+"_Drilling_"+obj.Drilldirection
        vec=App.Vector(obj.StartX,obj.StartY,0)
        dist=obj.Abstand
        pr=[Part]

        if obj.Anzahl_oder_Laenge==False:
          #dist=obj.Laenge/(obj.Anzahl-1)
          obj.Anzahl=int(round(obj.Laenge/dist,0))


        while z<obj.Anzahl+1:


          if obj.Drilldirection=="Top":
            #obj.Label = obj.Label+"_holes_Top"
            obj.AttachmentSupport = [(wp,'Vertex1'),(wp,'Vertex5'),(wp,'Vertex3')]
          if obj.Drilldirection=="Rear-Y":
            #obj.Label = obj.Label+"_holes_Rear-Y"
            obj.AttachmentSupport = [(wp,'Vertex8'),(wp,'Vertex4'),(wp,'Vertex7')]
          if obj.Drilldirection=="Left+X":
            #obj.Label = obj.Label+"_holes_Left+X"
            obj.AttachmentSupport = [(wp,'Vertex4'),(wp,'Vertex2'),(wp,'Vertex3')]
          if obj.Drilldirection=="Right-X":
            #obj.Label = obj.Label+"_holes_Right-X"
            obj.AttachmentSupport = [(wp,'Vertex6'),(wp,'Vertex8'),(wp,'Vertex5')]
          if obj.Drilldirection=="Bottom":
            #obj.Label = obj.Label+"_holes_Bottom"
            obj.AttachmentSupport = [(wp,'Vertex4'),(wp,'Vertex8'),(wp,'Vertex2')]
          if obj.Drilldirection=="Front+Y":
            #obj.Label = obj.Label+"_holes_Front+Y"
            obj.AttachmentSupport = [(wp,'Vertex2'),(wp,'Vertex6'),(wp,'Vertex1')]

          obj.MapPathParameter = 0.000000
          obj.MapMode = 'OXY'
          obj.AttachmentOffset = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0.00,0.00,1.00),0))# Versatz um Startpunkt und Drehwinkel
          if z<obj.Anzahl:

                if obj.MiddlePoint==True:
                  v2=App.Vector(obj.StartX,obj.StartY,0)
                  vs=App.Vector((math.cos(math.radians(obj.Angle))*(z*dist)-(math.cos(math.radians(obj.Angle))*(dist*(obj.Anzahl-1)/2))),(math.sin(math.radians(obj.Angle))*dist*z)-(math.sin(math.radians(obj.Angle))*(dist*(obj.Anzahl-1)/2)),0.00)# auf nÃ¤chstes Loch springen
                if obj.MiddlePoint==False:
                  v2=App.Vector(obj.StartX,obj.StartY,0)
                  vs=App.Vector(math.cos(math.radians(obj.Angle))*(z*dist),math.sin(math.radians(obj.Angle))*dist*z,0.00)# auf nÃ¤chstes Loch springen
                v3=vs.add(v2)
                vlist.insert(z,v3)
          obj.Holes=vlist

          z=z+1

        if obj.MirrorX==True and (obj.Drilldirection=="Top" or obj.Drilldirection=="Bottom"):
         for lo in range(len(vlist)):
           vlist[lo][0]=wpl-vlist[lo][0]
           obj.Holes=vlist

        if obj.MirrorY==True and (obj.Drilldirection=="Top" or obj.Drilldirection=="Bottom"):
         for lo in range(len(vlist)):
           vlist[lo][1]=wpw-vlist[lo][1]
           obj.Holes=vlist

        if obj.MirrorX==True and (obj.Drilldirection=="Left+X" or obj.Drilldirection=="Right-X"):
         for lo in range(len(vlist)):
           vlist[lo][0]=wpw-vlist[lo][0]
           obj.Holes=vlist

        if obj.MirrorY==True and (obj.Drilldirection=="Left+X" or obj.Drilldirection=="Right-X"):
         for lo in range(len(vlist)):
           vlist[lo][1]=wph-vlist[lo][1]
           obj.Holes=vlist

        if obj.MirrorX==True and (obj.Drilldirection=="Front+Y" or obj.Drilldirection=="Rear-Y"):
         for lo in range(len(vlist)):
           vlist[lo][0]=wpl-vlist[lo][0]
           obj.Holes=vlist

        if obj.MirrorY==True and (obj.Drilldirection=="Front+Y" or obj.Drilldirection=="Rear-Y"):
         for lo in range(len(vlist)):
           vlist[lo][1]=wph-vlist[lo][1]
           obj.Holes=vlist


# hier werden die Cylinder erzeugt
        b3=Part.makeCylinder(obj.Diameter/2,obj.Depth, App.Vector(vlist[0]), direction) # erstes Loch
        for lo in range(len(vlist)-1):
          #print(vlist[lo+1])
          pr.append(Part.makeCylinder(obj.Diameter/2,obj.Depth, App.Vector(vlist[lo+1]), direction)) # alle weiteren LÃ¶cher
        for i in range(len(pr)):
              if i<(len(pr)-1):
                b3=b3.fuse(pr[i+1])
                
        obj.Shape=b3
        #print('execute')
        shared.drill_template=[obj.Description,obj.StartX,obj.StartY,0,obj.Drilldirection,obj.Diameter,obj.Depth,obj.Anzahl_oder_Laenge,obj.Laenge,obj.Anzahl,obj.Abstand,obj.Angle,obj.MirrorX,obj.MirrorY,obj.MiddlePoint,obj.Condition,obj.single_holes]
#create_Drilling('Drilling',20,20,0,'Top',6,10,True,150,6,34,0,False,False,False,'1',True,test[0].ID)
        #print(shared.drill_template)
        return obj

#obj.Shape=Part.makeBox(obj.Depth,obj.Depth,obj.Depth)

def create_Drilling(obj_name,spx,spy,spz,dir,dia,depth,aol,lae,anz,abst,angle,mirx,miry,mp,cond,sh,bid):
 
    docActif = App.ActiveDocument
    if docActif == None: docActif = FreeCAD.newDocument()
    fr_obj = docActif.addObject('Part::FeaturePython', obj_name)


    Drilling(fr_obj,spx,spy,spz,dir,dia,depth,aol,lae,anz,abst,angle,mirx,miry,mp,cond,sh,bid)
    docActif.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.Control.showDialog(Drilling_Form_TaskPanel(fr_obj))    # zeigt den Dialog nach dem Erstellen an

    return

def add_drilling():
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
     
     #create_Drilling('Drilling',20,20,0,'Top',6,10,True,150,6,34,0,False,False,False,'1',True,test[0].ID)
     dt=shared.drill_template[:]
     dt.append(test[0].ID)
     #print(dt[:])
     create_Drilling(*dt)
     #dt.pop()
     #print (test[0].Label)
    #App.ActiveDocument.getObject(test[0].Label).adjustRelativeLinks(App.ActiveDocument.getObject('Part'))
    
     dd=App.ActiveDocument.getObject(test[0].Label).Parents
     ddn=dd[0][0]
     #print(ddn.Name)
     App.ActiveDocument.getObject(ddn.Name).addObject(App.ActiveDocument.getObject(test[0].Label))
    docActif = App.ActiveDocument
    docActif.recompute()