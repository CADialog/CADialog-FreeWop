import FreeCAD as App
#if App.GuiUp:
#    import FreeCADGui as Gui

def cutlist():
	print('\n')
	for obj in App.ActiveDocument.Objects:

	  if (hasattr(obj, 'ComponentID')) and (obj.Visibility==True):
	    if obj.ComponentID==10:
	      if obj.Grain !=0:
	        print(obj.Label,obj.Length, obj.Width, obj. Height)
	      else:
	        print(obj.Label,obj.Width, obj.Length, obj. Height)


#cutlist()