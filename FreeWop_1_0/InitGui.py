import FreeCADGui

class DropdownWorkbench (Workbench): 
    import os, sys
    
    import fakesmodule
   
    path = os.path.dirname(fakesmodule.__file__)
    iconPath = os.path.join(path, "Icons")
            #translationsPath = os.path.join(path, "translations")
    Icon = os.path.join(iconPath, "FreeWop.png")
    MenuText = "FreeWop"
     

    def Initialize(self):
        #import FreeWop # assuming Scripts.py is your module
        import FreeWop
           
        
        import CommandGroup
        
        list = ["Script_Cmd","Script_Cmd2","Script_Cmd3","Script_Cmd4","Script_Cmd5","Script_Cmd6","Script_Cmd7","Script_Cmd8","Script_Cmd9"]
        self.appendMenu("FreeWop", list) # creates a new menu
        #self.appendMenu(["FreeWop", "My submenu"], list) # appends a submenu to an existing menu
        
        list = ["post"] # That list must contain command names, that can be defined in Scripts.py
        self.appendToolbar("FreeWop",list)
        
        
        
        list=['Script_Cmd', 'Script_Cmd2', 'Script_Cmd3', 'Script_Cmd4', 'Script_Cmd5', 'Script_Cmd7', 'Script_Cmd8']
        self.appendToolbar("FreeWop",list)
        ''' 
        if second pulldown ist wanted, look also CommansGroup post2
        list = ["post2"] # That list must contain command names, that can be defined in Scripts.py
        self.appendToolbar("FreeWop",list)
        
        '''
		        		
FreeCADGui.addWorkbench(DropdownWorkbench())


FreeCADGui.runCommand('Std_DrawStyle',6)