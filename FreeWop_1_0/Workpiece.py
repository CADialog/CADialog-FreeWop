import FreeCAD as App
import Part

def create(obj_name,lx,ly,lz,mx,my,mz,ma,bid):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)

    box(obj,lx,ly,lz,mx,my,mz,ma,bid)

    ViewProviderBox(obj.ViewObject)

    App.ActiveDocument.recompute()

    return obj

class box():

    def __init__(self, obj,lx,ly,lz,mx,my,mz,ma,bid):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self

        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
        obj.addProperty('App::PropertyFloat', 'Length', 'Dimensions', 'Box length').Length = 10.0
        obj.addProperty('App::PropertyFloat', 'Width', 'Dimensions', 'Box width').Width = 10
        obj.addProperty('App::PropertyFloat', 'Height', 'Dimensions', 'Box height').Height = 10

        obj.addProperty("App::PropertyInteger","ComponentID","WoodWop","ComponentID").ComponentID = 10
        obj.addProperty("App::PropertyString","GComment","WoodWop","Font name").GComment = "Comment here"           
        obj.addProperty("App::PropertyFloat", "LA", "WoodWop", "Length of finished part. (global variable _BSX)")
        obj.addProperty("App::PropertyInteger", "BelongingID", "Dimensions", "BelongingID")
        obj.addProperty("App::PropertyInteger", "Grain", "Dimensions", "Grain").Grain=0 ## '0' means like Length direction

        obj.Placement=App.Placement(App.Vector(mx,my,mz),App.Rotation(App.Vector(0.00,1.00,0.00),ma))
     
        obj.Length=lx
        obj.Width=ly
        obj.Height=lz
        obj.BelongingID=bid


    def execute(self, obj):
        """
        Called on document recompute
        """

        import FreeCAD as App
        import Draft
        import Part
        
#        p1=App.Vector(0,0,0)
#        p2=App.Vector(10,10,0)
#        lin1=Part.LineSegment(p1, p2)
#        S1=Part.Shape([lin1])   
#        W = Part.Wire(S1.Edges)
#        obj.Shape=P
#        P = W.extrude(App.Vector(0, 0, 1))
        
        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
        obj.ViewObject.ShapeColor = (0.0,0.0,0.5)

class ViewProviderBox:

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """

        obj.Proxy = self
        
        obj.Transparency = 80
        obj.hide()
        obj.show()

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """

        #App.Console.PrintMessage("Change property: " + str(prop) + "\n")

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

