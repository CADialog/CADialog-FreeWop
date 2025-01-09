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

MSG = App.Console.PrintMessage

class Board_Form(QtGui.QWidget):
   "Board_Form"


   def __init__(self, fr_obj) :

      super().__init__()
      self.setWindowTitle("Board : "+fr_obj.Name)
      dispo = QtGui.QGridLayout(self)

      dispo.addWidget(QtGui.QLabel("Length", self),1,0)        
      self.Length = QtGui.QDoubleSpinBox(self)
      self.Length.setToolTip("Length")
      self.Length.setDecimals(2)
      self.Length.setMinimum(1)
      self.Length.setMaximum(5000.0)
      self.Length.setSingleStep(0.1)
      dispo.addWidget(self.Length, 1, 1)   
      self.Length.setValue(fr_obj.Length)
	
      dispo.addWidget(QtGui.QLabel("Width", self),2,0)        
      self.Width = QtGui.QDoubleSpinBox(self)
      self.Width.setToolTip("Width")
      self.Width.setDecimals(2)
      self.Width.setMinimum(1)
      self.Width.setMaximum(5000.0)
      self.Width.setSingleStep(0.1)
      dispo.addWidget(self.Width, 2, 1)   
      self.Width.setValue(fr_obj.Width)
		
      dispo.addWidget(QtGui.QLabel("Height", self),3,0)        
      self.Height = QtGui.QDoubleSpinBox(self)
      self.Height.setToolTip("Height")
      self.Height.setDecimals(2)
      self.Height.setMinimum(1)
      self.Height.setMaximum(5000.0)
      self.Height.setSingleStep(0.1)
      dispo.addWidget(self.Height, 3, 1)   
      self.Height.setValue(fr_obj.Height)

      dispo.addWidget(QtGui.QLabel("Gaind like width", self),4,0)        
      self.Grain = QtGui.QCheckBox(self)
      dispo.addWidget(self.Grain, 4, 1)   
      self.Grain.setChecked(fr_obj.Grain)




class Board_Form_TaskPanel(QtGui.QWidget):
   
   def __init__(self, fr_obj):

      super().__init__(Gui.getMainWindow(), QtCore.Qt.Tool)
      self.fr_obj = fr_obj      
      self.form = Board_Form(fr_obj) 
      self.form.Length.valueChanged.connect(self.on_Length_valueChanged) 
      self.form.Width.valueChanged.connect(self.on_Width_valueChanged)
      self.form.Height.valueChanged.connect(self.on_Height_valueChanged)
      self.form.Grain.toggled.connect(self.on_Grain_toggled)
          
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
           
   def on_Length_valueChanged(self,state):
      self.fr_obj.Length=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Width_valueChanged(self,state):
      self.fr_obj.Width=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Height_valueChanged(self,state):
      self.fr_obj.Height=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Grain_toggled(self,state):
      self.fr_obj.Grain=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  

class Board:

    def __init__(self, obj,lx,ly,lz,mx,my,mz,ma,bid):
        """
        Default constructor
        """

        self.Type = 'Board'

        obj.Proxy = self

        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Board description').Description = ""
        obj.addProperty('App::PropertyFloat', 'Length', 'Dimensions', 'Board length').Length = 10.0
        obj.addProperty('App::PropertyFloat', 'Width', 'Dimensions', 'Board width').Width = 10
        obj.addProperty('App::PropertyFloat', 'Height', 'Dimensions', 'Board height').Height = 10

        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 10
        obj.addProperty("App::PropertyString","GComment","WoodWop","Font name").GComment = "Comment here"           
        obj.addProperty("App::PropertyFloat", "LA", "WoodWop", "Length of finished part. (global variable _BSX)")
        obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")
        obj.addProperty("App::PropertyInteger", "Grain", "Dimensions", "Grain").Grain=0 ## '0' means like Length direction
        obj.addProperty("App::PropertyInteger", "Grainsymbol", "Dimensions", "Grainsymbol").Grain=0 ##show Grainsymbol 0=no

        obj.Placement=App.Placement(App.Vector(mx,my,mz),App.Rotation(App.Vector(0.00,1.00,0.00),ma))
     
        obj.Length=lx
        obj.Width=ly
        obj.Height=lz
        obj.BelongingID=bid
		
        xx=App.activeDocument().addObject('App::Part','Boards')
        xx.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 1
        App.ActiveDocument.getObject(obj.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(obj.Label))

		
		
        obj.recompute()
        ViewProviderBoard(obj.ViewObject)
        App.ActiveDocument.recompute()

    def execute(self, obj):
        """
        Called on document recompute
        """

        import FreeCAD as App
        import Draft
        import Part
        

		
        #gx=obj.Length/5
        #gy=obj.Width/3
        gx=60
        gy=15
        gsl=50
        gsh=15
        gsz=obj.Height
        grain=obj.Grain


        if grain==0:
          p5=App.Vector(gx,gsh/2+gy,gsz)
          p6=App.Vector(gsl/2+gx,gy,gsz)
          p7=App.Vector(gsl+gx,gsh/2+gy,gsz)
          p8=App.Vector(gsl/2+gx,gsh+gy,gsz)
        if grain==1:
          p5=App.Vector(gsh/2+gx,gy,gsz)
          p6=App.Vector(gx,gsl/2+gy,gsz)
          p7=App.Vector(gsh/2+gx,gsl+gy,gsz)
          p8=App.Vector(gsh+gx,gsl/2+gy,gsz)

        lin5=Part.LineSegment(p5, p6)
        lin6=Part.LineSegment(p6, p7)
        lin7=Part.LineSegment(p7, p8)
        lin8=Part.LineSegment(p8, p5)
		
        P=Part.makeBox(obj.Length, obj.Width, obj.Height)
		
        if obj.Grainsymbol !=0:
          S2=Part.Shape([lin5,lin6,lin7,lin8])
          WG = Part.Wire(S2.Edges)
          WG1=Part.Face(WG)   
          G=WG1.extrude(App.Vector(0,0,-0.2))
          TT=Part.Compound([P,G])
          obj.Shape=TT

        
        #P=P.fuse(G)    #hier wird auch die MAserrichtung angezeigt, allerdings passen dann die Eckenebezeichnungen nicht mehr
        #Part.show(P)
        if obj.Grainsymbol ==0:
		
          obj.Shape=P
        #obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
        obj.ViewObject.ShapeColor = (0.0,0.0,0.5)

class ViewProviderBoard:
   def __init__(self, vobj):
     """
     Set this object to the proxy object of the actual view provider
     """
     vobj.Proxy = self

     vobj.hide()
     vobj.show()
     vobj.ShapeColor=(1.0,1.0,1.0)    
     vobj.Transparency = 80
   
   def attach(self, vobj):
     """
     Setup the scene sub-graph of the view provider, this method is mandatory
     """
     return

   def setEdit(self, vobj, mode=0):
      Gui.Control.showDialog(Board_Form_TaskPanel(vobj.Object))	#setzt den Dialog in die ComboBox
      return True

   def unsetEdit(self,vobj,mode=0):
      Gui.Control.closeDialog()

   def getIcon(self):
     """
     Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
     """
     return """
        /* XPM */
		static const char *V29ya3BpZWNlXzE2[] = {
		/* columns rows colors chars-per-pixel */
		"16 16 4 1 ",
		"  c black",
		". c #00A2E8",
		"X c #99D9EA",
		"o c None",
		/* pixels */
		"oooooooooooooooo",
		"oo            oo",
		"oo XXXXXXXXXX oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo X........X oo",
		"oo XXXXXXXXXX oo",
		"oo            oo",
		"oooooooooooooooo"
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
   

def create_Board(obj_name,lx,ly,lz,mx,my,mz,ma,bid):
    """
    Object creation method
    """
	
    docActif = App.ActiveDocument
    if docActif == None: docActif = FreeCAD.newDocument()
    fr_obj = docActif.addObject('Part::FeaturePython', obj_name)


    

    Board(fr_obj,lx,ly,lz,mx,my,mz,ma,bid)

    docActif.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    #Gui.Control.showDialog(Board_Form_TaskPanel(fr_obj))    # zeigt den Dialog nach dem Erstellen an

    return


#Gui.addCommand('Board_Form',Board_Form())


def add_board():
	create_Board('Board',600,200,19,0,0,0,0,1212)
	
	
	