# 2 Möglichkeiten
#es muss das part:fearture PArt ausgewÃ¤hlt sein  componentID = 1, dann werden alle Bearbeitungen von des EinzelBoards"Board" abgezogen und ein 3D-Brett erzeugt
#es muss das part:fearture PArt ausgewÃ¤hlt sein  componentID = 2, dann wird ein 3D Korpus erzeugt

#rgebnis ist eine Shape, der NAme ist noch nicht richtig

import FreeCAD as App
if App.GuiUp:
    import FreeCADGui as Gui
import Part

def make_shape():
	sel = Gui.Selection.getSelection()
	list1=[]
	list2=[]
	list3=[]
	list4=[]

	for obj in sel:
	  if ((obj.Visibility==True) and (obj.ComponentID==1)) :
	    list1.append(obj)
	    ll=list1[0].Group
	    print(obj.Label)
	    print (ll[0].Label)
	    print (ll[1].Label)

	    result=ll[0].Shape

	    sh=[]
	    del ll[0]
	    for obj in ll:
	      sh.append(obj.Shape)
	    result=result.cut(sh)
	    #print(type(result2))
	    #Part.show(result)


	for obj in sel:
	  if ((obj.Visibility==True) and (obj.ComponentID==2)) :
	    list1.append(obj)
	    ll=list1[0].Group
	    result=ll[0].Shape
	    for obj in ll:
	      if obj.ComponentID==10:
	        list3.append(obj)
	      if obj.ComponentID!=10:
	        list4.append(obj)

	    for i in range(len(list3)):
	      if i<(len(list3)):
	        result=result.fuse(list3[i].Shape)

	    for i in range(len(list4)):
	      if i<(len(list4)):
	        result=result.cut(list4[i].Shape)

	Part.show(result)

