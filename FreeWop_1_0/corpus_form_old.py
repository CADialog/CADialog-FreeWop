


import FreeCAD as App

if App.GuiUp:
    import FreeCADGui as Gui

import Part
from FreeCAD import Base
import math
from PySide import QtGui, QtCore
#from fpo.Bohrung import Workpiece
import Workpiece
import shared
import config

MSG = App.Console.PrintMessage

class Corpus_Form(QtGui.QWidget):


   def __init__(self, fr_obj) :

      super().__init__()
      self.setWindowTitle("Corpus : "+fr_obj.Name)
      dispo = QtGui.QGridLayout(self)

      #dispo.addWidget(QtGui.QLabel("ComponentID", self),14,0)        
      #self.ComponentID = QtGui.QLineEdit(self)
      #self.ComponentID.setToolTip("Wie tief bohren")
      #self.maxLength=3
      #dispo.addWidget(self.ComponentID, 14, 1)   
      #self.ComponentID.setText(str(fr_obj.ComponentID))
      
      dispo.addWidget(QtGui.QLabel("Height", self),1,0)        
      self.Height = QtGui.QDoubleSpinBox(self)
      self.Height.setToolTip("Wie tief bohren")
      self.Height.setDecimals(2)
      self.Height.setMinimum(1)
      self.Height.setMaximum(5000.0)
      self.Height.setSingleStep(0.1)
      dispo.addWidget(self.Height, 1, 1)   
      self.Height.setValue(fr_obj.Height)

      dispo.addWidget(QtGui.QLabel("Depth", self),2,0)        
      self.Depth = QtGui.QDoubleSpinBox(self)
      self.Depth.setToolTip("Wie tief bohren")
      self.Depth.setDecimals(2)
      self.Depth.setMinimum(1)
      self.Depth.setMaximum(5000.0)
      self.Depth.setSingleStep(0.1)
      dispo.addWidget(self.Depth, 2, 1)   
      self.Depth.setValue(fr_obj.Depth)

      dispo.addWidget(QtGui.QLabel("Width", self),3,0)        
      self.Width = QtGui.QDoubleSpinBox(self)
      self.Width.setToolTip("Wie tief bohren")
      self.Width.setDecimals(2)
      self.Width.setMinimum(1)
      self.Width.setMaximum(5000.0)
      self.Width.setSingleStep(0.1)
      dispo.addWidget(self.Width, 3, 1)   
      self.Width.setValue(fr_obj.Width)

      dispo.addWidget(QtGui.QLabel("ThicknessL", self),4,0)        
      self.ThicknessL = QtGui.QDoubleSpinBox(self)
      self.ThicknessL.setDecimals(2)
      self.ThicknessL.setMinimum(1)
      self.ThicknessL.setMaximum(5000.0)
      self.ThicknessL.setSingleStep(0.1)
      dispo.addWidget(self.ThicknessL, 4, 1)   
      self.ThicknessL.setValue(fr_obj.ThicknessL)

    
	  
      dispo.addWidget(QtGui.QLabel("ThicknessR", self),5,0)        
      self.ThicknessR = QtGui.QDoubleSpinBox(self)
      self.ThicknessR.setToolTip("Wie tief bohren")
      self.ThicknessR.setDecimals(2)
      self.ThicknessR.setMinimum(1)
      self.ThicknessR.setMaximum(5000.0)
      self.ThicknessR.setSingleStep(0.1)
      dispo.addWidget(self.ThicknessR, 5, 1)   
      self.ThicknessR.setValue(fr_obj.ThicknessR)
	  
      dispo.addWidget(QtGui.QLabel("ThicknessT", self),6,0)        
      self.ThicknessT = QtGui.QDoubleSpinBox(self)
      self.ThicknessT.setToolTip("Wie tief bohren")
      self.ThicknessT.setDecimals(2)
      self.ThicknessT.setMinimum(1)
      self.ThicknessT.setMaximum(5000.0)
      self.ThicknessT.setSingleStep(0.1)
      dispo.addWidget(self.ThicknessT, 6, 1)   
      self.ThicknessT.setValue(fr_obj.ThicknessT)
	  
      dispo.addWidget(QtGui.QLabel("ThicknessB", self),7,0)        
      self.ThicknessB = QtGui.QDoubleSpinBox(self)
      self.ThicknessB.setToolTip("Wie tief bohren")
      self.ThicknessB.setDecimals(2)
      self.ThicknessB.setMinimum(1)
      self.ThicknessB.setMaximum(5000.0)
      self.ThicknessB.setSingleStep(0.1)
      dispo.addWidget(self.ThicknessB, 7, 1)   
      self.ThicknessB.setValue(fr_obj.ThicknessB)

      dispo.addWidget(QtGui.QLabel("offsetTop", self),9,0)        
      self.offsetTop = QtGui.QDoubleSpinBox(self)
      self.offsetTop.setToolTip("Wie tief bohren")
      self.offsetTop.setDecimals(2)
      self.offsetTop.setMinimum(0)
      self.offsetTop.setMaximum(1000.0)
      self.offsetTop.setSingleStep(0.1)
      dispo.addWidget(self.offsetTop, 9, 1)   
      self.offsetTop.setValue(fr_obj.offsetTop)

      dispo.addWidget(QtGui.QLabel("offsetBottom", self),10,0)        
      self.offsetBottom = QtGui.QDoubleSpinBox(self)
      self.offsetBottom.setToolTip("Wie tief bohren")
      self.offsetBottom.setDecimals(2)
      self.offsetBottom.setMinimum(0)
      self.offsetBottom.setMaximum(1000.0)
      self.offsetBottom.setSingleStep(0.1)
      dispo.addWidget(self.offsetBottom, 10, 1)   
      self.offsetBottom.setValue(fr_obj.offsetBottom)

      dispo.addWidget(QtGui.QLabel("offsetFrontTop", self),11,0)        
      self.offsetFrontTop = QtGui.QDoubleSpinBox(self)
      self.offsetFrontTop.setToolTip("Wie tief bohren")
      self.offsetFrontTop.setDecimals(2)
      self.offsetFrontTop.setMinimum(0)
      self.offsetFrontTop.setMaximum(1000.0)
      self.offsetFrontTop.setSingleStep(0.1)
      dispo.addWidget(self.offsetFrontTop, 11, 1)   
      self.offsetFrontTop.setValue(fr_obj.offsetFrontTop)

      dispo.addWidget(QtGui.QLabel("offsetFrontBottom", self),12,0)        
      self.offsetFrontBottom = QtGui.QDoubleSpinBox(self)
      self.offsetFrontBottom.setToolTip("Wie tief bohren")
      self.offsetFrontBottom.setDecimals(2)
      self.offsetFrontBottom.setMinimum(0)
      self.offsetFrontBottom.setMaximum(1000.0)
      self.offsetFrontBottom.setSingleStep(0.1)
      dispo.addWidget(self.offsetFrontBottom, 12, 1)   
      self.offsetFrontBottom.setValue(fr_obj.offsetFrontBottom)

      dispo.addWidget(QtGui.QLabel("offsetBackTop", self),13,0)        
      self.offsetBackTop = QtGui.QDoubleSpinBox(self)
      self.offsetBackTop.setToolTip("Wie tief bohren")
      self.offsetBackTop.setDecimals(2)
      self.offsetBackTop.setMinimum(0)
      self.offsetBackTop.setMaximum(1000.0)
      self.offsetBackTop.setSingleStep(0.1)
      dispo.addWidget(self.offsetBackTop, 13, 1)   
      self.offsetBackTop.setValue(fr_obj.offsetBackTop)

      dispo.addWidget(QtGui.QLabel("offsetBackBottom", self),14,0)        
      self.offsetBackBottom = QtGui.QDoubleSpinBox(self)
      self.offsetBackBottom.setToolTip("Wie tief bohren")
      self.offsetBackBottom.setDecimals(2)
      self.offsetBackBottom.setMinimum(0)
      self.offsetBackBottom.setMaximum(1000.0)
      self.offsetBackBottom.setSingleStep(0.1)
      dispo.addWidget(self.offsetBackBottom, 14, 1)   
      self.offsetBackBottom.setValue(fr_obj.offsetBackBottom)

      dispo.addWidget(QtGui.QLabel("Save standard", self),15,0)        
      self.saving = QtGui.QPushButton(self)
      self.saving.setText("Save")
      self.saving.setToolTip("Save parameters to config") #Tool tip
      dispo.addWidget(self.saving, 15, 1)   




class Corpus_Form_TaskPanel(QtGui.QWidget):
   
   def __init__(self, fr_obj):

      super().__init__(Gui.getMainWindow(), QtCore.Qt.Tool)
      self.fr_obj = fr_obj      
      self.form = Corpus_Form(fr_obj) 
      #self.form.ComponentID.textChanged.connect(self.on_ComponentID_textChanged) 
      self.form.Height.valueChanged.connect(self.on_Height_valueChanged)
      self.form.Width.valueChanged.connect(self.on_Width_valueChanged)
      self.form.Depth.valueChanged.connect(self.on_Depth_valueChanged)

      self.form.ThicknessL.valueChanged.connect(self.on_ThicknessL_valueChanged)
      self.form.ThicknessR.valueChanged.connect(self.on_ThicknessR_valueChanged)
      self.form.ThicknessB.valueChanged.connect(self.on_ThicknessB_valueChanged)
      self.form.ThicknessT.valueChanged.connect(self.on_ThicknessT_valueChanged)

      self.form.offsetTop.valueChanged.connect(self.on_offsetTop_valueChanged)
      self.form.offsetBottom.valueChanged.connect(self.on_offsetBottom_valueChanged)
      self.form.offsetFrontTop.valueChanged.connect(self.on_offsetFrontTop_valueChanged)
      self.form.offsetFrontBottom.valueChanged.connect(self.on_offsetFrontBottom_valueChanged)
      self.form.offsetBackTop.valueChanged.connect(self.on_offsetBackTop_valueChanged)
      self.form.offsetBackBottom.valueChanged.connect(self.on_offsetBackBottom_valueChanged)
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
           
   #def on_ComponentID_textChanged(self,state):
      #self.fr_obj.ComponentID=int(state)
      #self.fr_obj.Document.recompute()  
      #App.ActiveDocument.recompute()  
   def on_Depth_valueChanged(self,state):
      self.fr_obj.Depth=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Height_valueChanged(self,state):
      self.fr_obj.Height=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_Width_valueChanged(self,state):
      self.fr_obj.Width=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_ThicknessL_valueChanged(self,state):
      self.fr_obj.ThicknessL=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_ThicknessR_valueChanged(self,state):
      self.fr_obj.ThicknessR=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_ThicknessT_valueChanged(self,state):
      self.fr_obj.ThicknessT=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_ThicknessB_valueChanged(self,state):
      self.fr_obj.ThicknessB=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  

   def on_offsetTop_valueChanged(self,state):
      self.fr_obj.offsetTop=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_offsetBottom_valueChanged(self,state):
      self.fr_obj.offsetBottom=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_offsetFrontTop_valueChanged(self,state):
      self.fr_obj.offsetFrontTop=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_offsetFrontBottom_valueChanged(self,state):
      self.fr_obj.offsetFrontBottom=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_offsetBackTop_valueChanged(self,state):
      self.fr_obj.offsetBackTop=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  
   def on_offsetBackBottom_valueChanged(self,state):
      self.fr_obj.offsetBackBottom=state
      self.fr_obj.Document.recompute()  
      App.ActiveDocument.recompute()  

   def on_saving_clicked(self,state):
      print('pressed')
      config.configwrite_corpus()	

class ViewProviderCorpus:


   def __init__(self, vobj):
     """
     Set this object to the proxy object of the actual view provider
     """
     vobj.Proxy = self
    
   
   def attach(self, vobj):
     """
     Setup the scene sub-graph of the view provider, this method is mandatory
     """
     return

   def setEdit(self, vobj, mode=0):
      Gui.Control.showDialog(Corpus_Form_TaskPanel(vobj.Object))
      return True

   def unsetEdit(self,vobj,mode=0):
      Gui.Control.closeDialog()

   def getIcon(self):
     """
     Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
     """
     return """
       /* XPM */
		static char *_7ff3bfeb0a34b2aff573c923ab17f10kodDyRuy2O1g8S5u[] = {
		/* columns rows colors chars-per-pixel */
		"16 16 47 1 ",
		"  c #26363B",
		". c #653C41",
		"X c #264B58",
		"o c #3F4F53",
		"O c #3A5258",
		"+ c #306375",
		"@ c #4D595C",
		"# c #53505F",
		"$ c #625C70",
		"% c #57676B",
		"& c #4D6D75",
		"* c #5F707A",
		"= c #62667E",
		"- c #737B7D",
		"; c #916D73",
		": c #987075",
		"> c #CE757D",
		", c #669B75",
		"< c #306D84",
		"1 c #397084",
		"2 c #4D7788",
		"3 c #A17D83",
		"4 c #CB7780",
		"5 c #2687AF",
		"6 c #3A84A1",
		"7 c #368CA0",
		"8 c #308BAF",
		"9 c #3697AF",
		"0 c #569683",
		"q c #7D898C",
		"w c #26A6DB",
		"e c #3AADDB",
		"r c #36B5DA",
		"t c #00A2E8",
		"y c #26B0E9",
		"u c #30B3E9",
		"i c #808080",
		"p c #88989C",
		"a c #839BA1",
		"s c gray75",
		"d c #B9C9CD",
		"f c #BFE8F9",
		"g c #C0C0C0",
		"h c #C3C3C3",
		"j c #C9E1EB",
		"k c #EFEFEF",
		"l c None",
		/* pixels */
		"llllslllllllkhll",
		"lll-;333333:*ill",
		"llqeyyyyyyw<uill",
		"lsX+.%%%%%o5u-ll",
		"ls,r>hhhhhp5y,ll",
		"ls,r>hhhhhp5y3ll",
		"ls7y>hhhhhp5u:ll",
		"ls0r>hhhhhp5y2ll",
		"lg,e4hhhhhp8y2ll",
		"lh6u4hhhhha5y3ll",
		"ls0e4hhddha5y,ll",
		"ls,9$2$22$#8y3ll",
		"ls16tttttt55y2ll",
		"ls &&&&&&&O52kll",
		"ls5ttttttt<&klll",
		"lkjfffffffjkllll"
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
   

class Corpus:

   def __init__(self,obj,height,depth,width,tl,tr,tt,tb,offt,offb,offft,offbt,offtt,offbb):
        self.Type = 'Corpus'
        obj.Proxy = self
        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 100
        obj.addProperty('App::PropertyFloat', 'Height', 'Dimensions', 'Height').Height=800
        obj.addProperty('App::PropertyFloat', 'Width','Dimensions', 'Width').Width=400
        obj.addProperty('App::PropertyFloat', 'Depth', 'Dimensions', 'Depth').Depth=400
        obj.addProperty('App::PropertyFloat', 'ThicknessL', 'Dimensions', 'ThicknessL').ThicknessL=19
        obj.addProperty('App::PropertyFloat', 'ThicknessR', 'Dimensions', 'ThicknessR').ThicknessR=19
        obj.addProperty('App::PropertyFloat', 'ThicknessT', 'Dimensions', 'ThicknessT').ThicknessT=19
        obj.addProperty('App::PropertyFloat', 'ThicknessB', 'Dimensions', 'ThicknessB').ThicknessB=19

        obj.addProperty('App::PropertyFloat', 'offsetTop', 'Dimensions', 'offsetTop').offsetTop=2
        obj.addProperty('App::PropertyFloat', 'offsetBottom', 'Dimensions', 'offsetTop').offsetBottom=2
        obj.addProperty('App::PropertyFloat', 'offsetFrontTop', 'Dimensions', 'offsetFrontTop').offsetFrontTop=2
        obj.addProperty('App::PropertyFloat', 'offsetFrontBottom', 'Dimensions', 'offsetFrontBottom').offsetFrontBottom=2
        obj.addProperty('App::PropertyFloat', 'offsetBackTop', 'Dimensions', 'offsetBackTop').offsetBackTop=2
        obj.addProperty('App::PropertyFloat', 'offsetBackBottom', 'Dimensions', 'offsetBackBottom').offsetBackBottom=2
        obj.addProperty('App::PropertyStringList', 'Boards', 'Dimensions', 'Boards')#.Boards=['gg','gg']

        #obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")=bid
        #obj.BelongingID=bid
        bid=obj.ID
        print('Hallo')
		
        obj.Height=height
        obj.Width=width
        obj.Depth=depth
        obj.ThicknessL=tl
        obj.ThicknessR=tr
        obj.ThicknessT=tt
        obj.ThicknessB=tb		
        obj.offsetTop=offt
        obj.offsetBottom=offb
        obj.offsetFrontTop=offft
        obj.offsetFrontBottom=offbt
        obj.offsetBackTop=offtt
        obj.offsetBackBottom=offbb
		

        xx=App.activeDocument().addObject('App::Part','Part')
        xx.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 2
        #App.ActiveDocument.getObject('Corpus').adjustRelativeLinks(App.ActiveDocument.getObject('Part'))
        #App.ActiveDocument.getObject("Part").addObject(App.ActiveDocument.getObject("Corpus"))
        App.ActiveDocument.getObject(obj.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(obj.Label))
        #print (xx.Label)
       
        lb=Workpiece.create('Left',1,1,1,0,0,0,0,bid)
        rb=Workpiece.create('Right',1,1,1,0,0,0,0,bid)
        bb=Workpiece.create('Bottom',1,1,1,0,0,0,0,bid)
        tb=Workpiece.create('Top',1,1,1,0,0,0,0,bid)


        blist=[xx.Label,lb.Label,rb.Label,bb.Label,tb.Label]
        
        obj.Boards=blist
 
        App.ActiveDocument.getObject(lb.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(lb.Label))
        App.ActiveDocument.getObject(rb.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(rb.Label))
        App.ActiveDocument.getObject(tb.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(tb.Label))
        App.ActiveDocument.getObject(bb.Label).adjustRelativeLinks(App.ActiveDocument.getObject(xx.Label))
        App.ActiveDocument.getObject(xx.Label).addObject(App.ActiveDocument.getObject(bb.Label))
        obj.recompute()
        ViewProviderCorpus(obj.ViewObject)
        App.ActiveDocument.recompute()

        
   def execute(self, obj):
        """
        Called on document recompute
        """
        blist=[]
        blist=obj.Boards
        print(blist[0])

        Left=App.ActiveDocument.getObject(obj.Boards[1])
        Right=App.ActiveDocument.getObject(obj.Boards[2])
        Top=App.ActiveDocument.getObject(obj.Boards[4])
        Bottom=App.ActiveDocument.getObject(obj.Boards[3])


        Left.Length,Left.Width,Left.Height=obj.Height, obj.Depth, obj.ThicknessL
        App.ActiveDocument.getObject(obj.Boards[1]).Placement=App.Placement(App.Vector(0,0,obj.Height),App.Rotation(App.Vector(0.00,1.00,0.00),90.00))

        Right.Length,Right.Width,Right.Height=obj.Height, obj.Depth, obj.ThicknessR
        App.ActiveDocument.getObject(obj.Boards[2]).Placement=App.Placement(App.Vector(obj.Width,0.00,0.00),App.Rotation(App.Vector(0.00,1,0.00),-90.00))

        Bottom.Length,Bottom.Width,Bottom.Height=obj.Width-obj.ThicknessL-obj.ThicknessR, obj.Depth-obj.offsetBackBottom-obj.offsetFrontBottom, obj.ThicknessB
        App.ActiveDocument.getObject(obj.Boards[3]).Placement=App.Placement(App.Vector(obj.ThicknessL,obj.offsetFrontBottom,obj.offsetBottom),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))

        Top.Length,Top.Width,Top.Height=obj.Width-obj.ThicknessL-obj.ThicknessR, obj.Depth-obj.offsetBackTop-obj.offsetFrontTop, obj.ThicknessT
        App.ActiveDocument.getObject(obj.Boards[4]).Placement=App.Placement(App.Vector(obj.Width-obj.ThicknessR,obj.offsetFrontTop,obj.Height-obj.offsetTop),App.Rotation(App.Vector(0.00,1.00,0.00),180.00))

        shared.corpus_template=[obj.Label,obj.Height,obj.Depth,obj.Width,obj.ThicknessL,obj.ThicknessL,obj.ThicknessL,obj.ThicknessL,obj.offsetTop,obj.offsetBottom,obj.offsetFrontTop,obj.offsetFrontBottom,obj.offsetBackTop,obj.offsetBackBottom]

def create_Corpus(obj_name,height,depth,width,tl,tr,tt,tb,offt,offb,offft,offbt,offtt,offbb):
 
    docActif = App.ActiveDocument
    if docActif == None: docActif = App.newDocument()
    fr_obj = docActif.addObject('Part::FeaturePython', obj_name)
    print('ggg')
    Corpus(fr_obj,height,depth,width,tl,tr,tt,tb,offt,offb,offft,offbt,offtt,offbb)
    docActif.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.Control.showDialog(Corpus_Form_TaskPanel(fr_obj))

    return

def add_corpus():
	
     #create_Corpus(obj_name,height,depth,width,tl,tr,tt,tb,offt,offb,offft,offbt,offtt,offbb)
     #create_Corpus('Corpus',600,400,300,18,18,18,18,0,0,0,0,0,0)	

     ct=shared.corpus_template[:]
     print(ct[:])
     create_Corpus(*ct)
     


#create_Corpus('Corpus')

