
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
MSG = App.Console.PrintMessage

class Grooving_Form(QtGui.QWidget):


   def __init__(self, fr_obj) :

      super().__init__()
      self.setWindowTitle("Grooving : "+fr_obj.Name)
      dispo = QtGui.QGridLayout(self)


      dispo.addWidget(QtGui.QLabel('Drilldirection', self), 0, 0)
      self.Drilldirection = QtGui.QComboBox(self)
      self.Drilldirection.addItems(['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom'])
      dispo.addWidget(self.Drilldirection,0,1)
      self.Drilldirection.setCurrentText(fr_obj.Drilldirection)

      dispo.addWidget(QtGui.QLabel("Nutbreite", self),1,0)        
      self.Width = QtGui.QDoubleSpinBox(self)
      self.Width.setToolTip("Nutbreite")
      self.Width.setDecimals(2)
      self.Width.setMinimum(1)
      self.Width.setMaximum(100.0)
      self.Width.setSingleStep(0.1)
      dispo.addWidget(self.Width, 1, 1)   
      self.Width.setValue(fr_obj.Width)

      dispo.addWidget(QtGui.QLabel("Nuttiefe", self),2,0)        
      self.Depth = QtGui.QDoubleSpinBox(self)
      self.Depth.setToolTip("Nuttiefe ")
      self.Depth.setDecimals(2)
      self.Depth.setMinimum(1)
      self.Depth.setMaximum(500.0)
      self.Depth.setSingleStep(0.1)
      dispo.addWidget(self.Depth, 2, 1)   
      self.Depth.setValue(fr_obj.Depth)

      dispo.addWidget(QtGui.QLabel("StartX", self),4,0)        
      self.StartX = QtGui.QDoubleSpinBox(self)
      self.StartX.setToolTip("Wie tief bohren")
      self.StartX.setDecimals(2)
      self.StartX.setMinimum(0)
      self.StartX.setMaximum(5000.0)
      self.StartX.setSingleStep(0.1)
      dispo.addWidget(self.StartX, 4, 1)   
      self.StartX.setValue(fr_obj.StartX)

      dispo.addWidget(QtGui.QLabel("StartY", self),5,0)        
      self.StartY = QtGui.QDoubleSpinBox(self)
      self.StartY.setToolTip("StartY")
      self.StartY.setDecimals(2)
      self.StartY.setMinimum(0)
      self.StartY.setMaximum(5000.0)
      self.StartY.setSingleStep(0.1)
      dispo.addWidget(self.StartY, 5, 1)  
		
      self.StartY.setValue(fr_obj.StartY)
      dispo.addWidget(QtGui.QLabel("Winkel_und_Laenge", self),6,0)        
      self.Winkel_und_Laenge = QtGui.QCheckBox(self)
      dispo.addWidget(self.Winkel_und_Laenge, 6, 1)   
		
      self.Winkel_und_Laenge.setChecked(fr_obj.Winkel_und_Laenge)	
	
      dispo.addWidget(QtGui.QLabel("Angle", self),7,0) 


		
      self.Angle = QtGui.QDoubleSpinBox(self)
      self.Angle.setToolTip("Angle")
      self.Angle.setDecimals(2)
      self.Angle.setMinimum(0)
      self.Angle.setMaximum(360.0)
      self.Angle.setSingleStep(0.1)
      dispo.addWidget(self.Angle, 7, 1)   
      self.Angle.setValue(fr_obj.Angle)
		
      dispo.addWidget(QtGui.QLabel("Laenge", self),8,0)        
      self.Laenge = QtGui.QDoubleSpinBox(self)
      self.Laenge.setToolTip("Laenge")
      self.Laenge.setDecimals(2)
      self.Laenge.setMinimum(1)
      self.Laenge.setMaximum(5000.0)
      self.Laenge.setSingleStep(0.1)
      dispo.addWidget(self.Laenge, 8, 1)   
      self.Laenge.setValue(fr_obj.Laenge)

      dispo.addWidget(QtGui.QLabel("EndX", self),9,0)        
      self.EndX = QtGui.QDoubleSpinBox(self)
      self.EndX.setToolTip("EndX")
      self.EndX.setDecimals(2)
      self.EndX.setMinimum(0)
      self.EndX.setMaximum(5000.0)
      self.EndX.setSingleStep(0.1)
      dispo.addWidget(self.EndX, 9, 1)   
      self.EndX.setValue(fr_obj.EndX)

      dispo.addWidget(QtGui.QLabel("EndY", self),10,0)        
      self.EndY = QtGui.QDoubleSpinBox(self)
      self.EndY.setToolTip("EndY")
      self.EndY.setDecimals(2)
      self.EndY.setMinimum(0)
      self.EndY.setMaximum(5000.0)
      self.EndY.setSingleStep(0.1)
      dispo.addWidget(self.EndY, 10, 1)   
      self.EndY.setValue(fr_obj.EndY)

      dispo.addWidget(QtGui.QLabel('RadiusCorrection', self), 11, 0)
      self.RadiusCorrection = QtGui.QComboBox(self)
      self.RadiusCorrection.addItems(['No','Left','Right'])
      dispo.addWidget(self.RadiusCorrection,11,1)
      self.RadiusCorrection.setCurrentText(fr_obj.RadiusCorrection)
		
      dispo.addWidget(QtGui.QLabel('Mode', self), 12, 0)
      self.Mode = QtGui.QComboBox(self)
      self.Mode.addItems(['surface','ground','through'])
      dispo.addWidget(self.Mode,12,1)
      self.Mode.setCurrentText(fr_obj.Mode)
 


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

   

class Grooving_Form_TaskPanel(QtGui.QWidget):
   
   def __init__(self, fr_obj):

      super().__init__(Gui.getMainWindow(), QtCore.Qt.Tool)
      self.fr_obj = fr_obj      
      self.form = Grooving_Form(fr_obj) 
      self.form.StartX.valueChanged.connect(self.on_StartX_valueChanged)
      self.form.StartY.valueChanged.connect(self.on_StartY_valueChanged)
      self.form.EndX.valueChanged.connect(self.on_EndX_valueChanged)
      self.form.EndY.valueChanged.connect(self.on_EndY_valueChanged)
      self.form.Winkel_und_Laenge.toggled.connect(self.on_Winkel_und_Laenge_toggled)
      self.form.Laenge.valueChanged.connect(self.on_Laenge_valueChanged)

      self.form.Angle.valueChanged.connect(self.on_Angle_valueChanged)
      self.form.Depth.valueChanged.connect(self.on_Depth_valueChanged)
      self.form.Width.valueChanged.connect(self.on_Width_valueChanged)

      self.form.Drilldirection.currentIndexChanged.connect(self.on_Drilldirection_valueChanged)
      self.form.RadiusCorrection.currentIndexChanged.connect(self.on_RadiusCorrection_valueChanged)
      self.form.Mode.currentIndexChanged.connect(self.on_Mode_valueChanged)
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
   def on_StartX_valueChanged(self,state):
      self.fr_obj.StartX=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_StartY_valueChanged(self,state):
      self.fr_obj.StartY=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_EndX_valueChanged(self,state):
      self.fr_obj.EndX=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_EndY_valueChanged(self,state):
      self.fr_obj.EndY=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Depth_valueChanged(self,state):
      self.fr_obj.Depth=int(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Width_valueChanged(self,state):
      self.fr_obj.Width=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  

   def on_Drilldirection_valueChanged(self,state):
      self.fr_obj.Drilldirection=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_RadiusCorrection_valueChanged(self,state):
      self.fr_obj.RadiusCorrection=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Mode_valueChanged(self,state):
      self.fr_obj.Mode=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute() 
   def on_BelongingID_valueChanged(self,state):
      self.fr_obj.BelongingID=int(state)
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Angle_valueChanged(self,state):
      self.fr_obj.Angle=state
      self.fr_obj.Document.recompute()  
   def on_Winkel_und_Laenge_toggled(self,state):
      self.fr_obj.Winkel_und_Laenge=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()
   def on_Laenge_valueChanged(self,state):
      self.fr_obj.Laenge=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
		
   def on_saving_clicked(self,state):
      config.configwrite_groove()	

class ViewProviderGrooving:


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
      Gui.Control.showDialog(Grooving_Form_TaskPanel(vobj.Object))	#setzt den Dialog in die ComboBox
      return True

   def unsetEdit(self,vobj,mode=0):
      Gui.Control.closeDialog()

   def getIcon(self):
     """
     Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
     """
     return """
         /* XPM */
            static const char *R3Jvb3ZlXzE2[] = {
            /* columns rows colors chars-per-pixel */
            "16 16 5 1 ",
            "  c black",
            ". c #ED1C24",
            "X c #00A2E8",
            "o c #0AA6E8",
            "O c None",
            /* pixels */
            "OOOOOOOOOOO   OO",
            "OOOOOOO    XX OO",
            "OOOO    XXX.X OO",
            "OOO XoXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXX.X OO",
            "OOO XXXXXXXXX OO",
            "OOO XXXXX     OO",
            "OOO      OOOOOOO",
            "OOO OOOOOOOOOOOO"
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
   

class Grooving:

   def __init__(self, obj,spx,spy,epx,epy,depth,wi,rc,dir,cond,angle,com,mode,bid):
        self.Type = 'Nut'
        obj.Proxy = self
        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = "row_of_holes"
        obj.addProperty('App::PropertyLength', 'Nutbreite', 'Dimensions', 'Nutbreite')
        obj.addProperty("App::PropertyBool", "Winkel_und_Laenge", "Dimensions","Base" "Winkel_und_Laenge")
        obj.addProperty('App::PropertyFloat', 'Laenge', 'Dimensions', 'Laenge')
        obj.addProperty('App::PropertyFloat', 'Depth', 'Dimensions', 'Depth')
        obj.addProperty('App::PropertyFloat', 'StartX', 'Dimensions', 'StartX')
        obj.addProperty('App::PropertyFloat', 'StartY', 'Dimensions', 'StartY')
        obj.addProperty('App::PropertyFloat', 'EndX', 'Dimensions', 'EndX')
        obj.addProperty('App::PropertyFloat', 'EndY', 'Dimensions', 'EndY')
        obj.addProperty('App::PropertyFloat', 'Width', 'Dimensions', 'Width')
        obj.addProperty("App::PropertyVectorList","Holes")
        obj.addProperty("App::PropertyEnumeration","Drilldirection","Base","Drilldirection").Drilldirection=['Top','Left+X','Right-X','Front+Y','Rear-Y','Bottom']
        obj.addProperty("App::PropertyEnumeration","RadiusCorrection","Base","RadiusCorrection").RadiusCorrection=['No','Left','Right']
        obj.addProperty("App::PropertyEnumeration","Mode","Base","Mode").Mode=['surface','ground','through']

        obj.addProperty("App::PropertyAngle", "Angle", "Dimensions","Base" "Angle of groove")
        obj.addProperty("App::PropertyString", "Condition", "Dimensions","Base" "Condition")
        obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")
        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 30


        obj.Mode=mode
        obj.StartX=spx
        obj.StartY=spy
        obj.Angle=angle
        obj.Winkel_und_Laenge=com
        obj.EndX=epx
        obj.EndY=epy
        obj.Laenge=100
        obj.Depth=depth
        obj.Drilldirection=dir
        obj.Width=wi
        obj.RadiusCorrection=rc
        obj.Drilldirection=dir
        obj.Condition=cond
        obj.BelongingID=bid
        obj.addExtension('Part::AttachExtensionPython', obj)

        direction=App.Vector(0,1,0)
        rowdirection=App.Vector(0,0,1)
        obj.Holes=[]
        obj.recompute()
        ViewProviderGrooving(obj.ViewObject)
        App.ActiveDocument.recompute()

        
   def execute(self, obj):
        """
        Called on document recompute
        """
        import FreeCAD as App
        import math
        import Draft
        import Part

        direction=App.Vector(0,0,-1)
        z=0
        obj.Holes=[]
        vlist=[]   

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
				
        winkel=obj.Angle
		
        if obj.Winkel_und_Laenge==True:
            gl=obj.Laenge
        if obj.Winkel_und_Laenge==False:
            gl=math.sqrt(math.pow((obj.EndY-obj.StartY),2)+math.pow((obj.EndX-obj.StartX),2))
            winkel=math.degrees(math.atan((obj.EndY-obj.StartY)/(obj.EndX-obj.StartX)))
            if (obj.EndY-obj.StartY==0):
              print('null')
        #gl=obj.EndX-obj.StartX
        gd=obj.Depth
        gw=obj.Width
        gr=30
        s=2*math.sqrt((2*gr*gd)-(gd*gd))	# Sehnenlaenge

        korr=gl/2	
        
        if obj.Mode=='ground':
         #gl=gl+s
         korr=gl/2
        startY=obj.StartY
        startX=obj.StartX
       
		

        korx=math.sin(math.radians((winkel)))*gw*0.5
		
        if ((obj.Angle!=0) and (obj.EndY-obj.StartY!=0)):
            kory=korx/(math.tan(math.radians((winkel))))
        else:
            kory=gw/2

        obj.Label =  lab+"_Grooving_"+obj.Drilldirection
		
        if obj.Drilldirection=="Top":
         obj.Support = [(wp,'Vertex1'),(wp,'Vertex5'),(wp,'Vertex3')]
        if obj.Drilldirection=="Front+Y":
         obj.Support = [(wp,'Vertex2'),(wp,'Vertex6'),(wp,'Vertex1')]
        if obj.Drilldirection=="Bottom":
         obj.Support = [(wp,'Vertex4'),(wp,'Vertex8'),(wp,'Vertex2')]
        if obj.Drilldirection=="Rear-Y":
         obj.Support = [(wp,'Vertex8'),(wp,'Vertex4'),(wp,'Vertex7')]
        if obj.Drilldirection=="Left+X":
         obj.Support = [(wp,'Vertex4'),(wp,'Vertex2'),(wp,'Vertex3')]
        if obj.Drilldirection=="Right-X":
         obj.Support = [(wp,'Vertex6'),(wp,'Vertex8'),(wp,'Vertex5')]

		
		
		
        obj.MapPathParameter = 0.000000
        obj.MapMode = 'OXY'
		
        if obj.RadiusCorrection=='No':
         obj.AttachmentOffset = App.Placement(App.Vector(gl/2+startX-korr,startY,-gd),App.Rotation(App.Vector(1.00,0.00,0.00),90)).multiply(App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),winkel)))     
		
        if obj.RadiusCorrection=='Left':
         obj.AttachmentOffset = App.Placement(App.Vector(gl/2+startX-korr-korx,startY+kory,-gd),App.Rotation(App.Vector(1.00,0.00,0.00),90)).multiply(App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),winkel)))

        if obj.RadiusCorrection=='Right':
         obj.AttachmentOffset = App.Placement(App.Vector(gl/2+startX-korr+korx,startY-kory,-gd),App.Rotation(App.Vector(1.00,0.00,0.00),90)).multiply(App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),winkel)))

        vec=App.Vector(obj.StartX,startY,0)
        pr=[Part]
        pl = App.Placement()
        s=2*math.sqrt((2*gr*gd)-(gd*gd))	# Sehnenlaenge
        sina=(s/2)/gr
        wi=math.asin(sina)
        print(math.degrees(wi))
        ww=math.degrees(wi)
        dx=gr*math.sin(math.radians(ww/2))		# 
        dy=gr-(math.cos(math.radians(ww/2))*gr)	# Verlängerung durch Saegenradius
        print(dx,dy)
        
        korr2=App.Vector(korr,0,0)		
		
        p1=App.Vector(s*0.5-gl/2, 0, 0).add(korr2)
        p2=App.Vector(gl/2-0.5*s, 0, 0).add(korr2)
        p3=App.Vector(gl/2-0.5*s+dx, dy, 0).add(korr2)
        p4=App.Vector(gl/2, gd, 0).add(korr2)
        p5=App.Vector(-gl/2, gd, 0).add(korr2)
        p6=App.Vector(-gl/2+0.5*s-dx, dy, 0).add(korr2)
		
        if obj.Mode=='ground':
         #gl=gl+s
         korr2=App.Vector(korr,0,0)
         p1=App.Vector(s*0.5-gl/2-s/2, 0, 0).add(korr2)#
         p2=App.Vector(gl/2-0.5*s+s/2, 0, 0).add(korr2)
         p3=App.Vector(gl/2-0.5*s+dx+s/2, dy, 0).add(korr2)
         p4=App.Vector(gl/2+s/2, gd, 0).add(korr2)
         p5=App.Vector(-gl/2-s/2, gd, 0).add(korr2)#
         p6=App.Vector(-gl/2+0.5*s-dx-s/2, dy, 0).add(korr2)#
		
        shared.groove_template=[obj.Description, obj.StartX,obj.StartY,obj.EndX,obj.EndY,obj.Depth,obj.Width,obj.RadiusCorrection,obj.Drilldirection,obj.Condition,obj.Angle,obj.Winkel_und_Laenge,obj.Mode]
        print('shared')		
		
        bogen1=[p2,p3,p4] #linker Bogen
        bogen2=[p5,p6,p1] #rechter Bogen
        lin1=Part.LineSegment(p1, p2)
        parc1=Part.Arc(p2,p3,p4)
        lin2=Part.LineSegment(p4, p5)
        parc2=Part.Arc(p5,p6,p1)
        S1=Part.Shape([lin1,parc1,lin2,parc2])

		
        W = Part.Wire(S1.Edges)
        W1=Part.Face(W)
        p1=W1.extrude(App.Vector(0, 0, gw/2))
        p2=W1.extrude(App.Vector(0, 0, -gw/2))
        P=p1.fuse(p2)

        if obj.Mode=='ground':
         obj.Shape=P
        if obj.Mode=='surface':
         obj.Shape=P
		
        if obj.Mode=='through':
         if obj.RadiusCorrection=='No':
           obj.AttachmentOffset = App.Placement(App.Vector(0,startY-gw/2,-gd),App.Rotation(App.Vector(0.00,0.00,1.00),0))	#hier Drehwinkel
         if obj.RadiusCorrection=='Right':
           obj.AttachmentOffset = App.Placement(App.Vector(0,startY-gw,-gd),App.Rotation(App.Vector(0.00,0.00,1.00),0))		#hier Drehwinkel
         if obj.RadiusCorrection=='Left':
           obj.AttachmentOffset = App.Placement(App.Vector(0,startY,-gd),App.Rotation(App.Vector(0.00,0.00,1.00),0))		#hier Drehwinkel
         obj.Shape=Part.makeBox(wpl,obj.Width,obj.Depth)



def create_Grooving(obj_name,spx,spy,epx,epy,depth,wi,rc,dir,cond,angle,com,mode,bid):
 
    docActif = App.ActiveDocument
    if docActif == None: docActif = App.newDocument()
    fr_obj = docActif.addObject('Part::FeaturePython', obj_name)


    Grooving(fr_obj,spx,spy,epx,epy,depth,wi,rc,dir,cond,angle,com,mode,bid)
    docActif.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.Control.showDialog(Grooving_Form_TaskPanel(fr_obj))

    return

#shared.groove_template=[obj.Description, obj.StartY,obj.StartY,obj.EndX,obj.EndY,obj.Depth,obj.Width,obj.RadiusCorrection,obj.Drilldirection,obj.Condition]


def add_groove():
    print('dgfsdffg')
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
     print('Keine eindeutige Auswahl!!! Bitte wählen Sie ein Workpiece')
    else:
     print (test[0].ID)
     #create_Grooving('Grooving',0,0,500,100,10,8,'No','Top','1',45,True,'surface',test[0].ID)
     gt=shared.groove_template[:]	
     gt.append(test[0].ID)
     print(gt[:])
     create_Grooving(*gt)
		
     print (test[0].Label)
    #App.ActiveDocument.getObject(test[0].Label).adjustRelativeLinks(App.ActiveDocument.getObject('Part'))
    
     dd=App.ActiveDocument.getObject(test[0].Label).Parents
     ddn=dd[0][0]
     print(ddn.Name)
     App.ActiveDocument.getObject(ddn.Name).addObject(App.ActiveDocument.getObject(test[0].Label))
    docActif = App.ActiveDocument
    docActif.recompute()