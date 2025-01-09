import FreeCAD as App
if App.GuiUp:
    import FreeCADGui as Gui


import os.path
	
save_path = 'C:\\Test'                           #windows
#save_path='/home/mint/.var/app/org.freecadweb.FreeCAD/data/FreeCAD/Mod/FreeWop/cnc'    #linux
#save_path='/home/mint/scxs/'    #linux

class flc(float):
    def __str__(self):
        return self.__repr__().replace(".",",") # make comma instead of point if needed (".",",")


class scxFile:
    def __init__(self,scx_name):
       name_of_file =scx_name
       completeName = os.path.join(save_path, name_of_file+".scx")         
       print(completeName)
       self.datei = open(completeName,'w')

    def Data_head(self):
       self.datei.write(
"""<?xml version="1.0" encoding="utf-8"?>
<Root Cad="BuiltInCad" version="2.0">
    <Project>\n"""
             )       
      
    def Variable_table(self,L,B,D,name_of_scx_file): #withou function

        self.datei.write("<Panel IsProduce=\"true\" ID=\""+str(name_of_scx_file)+"\" Name=\"Test\" Length=\""+str(flc(L))+"\" Width=\""+flc(str(B))+"\" Thickness=\""+flc(str(D))+"\" MachiningPoint=\"1\">")


    def Werkstck(self,L,B,D,name_of_scx_file):
       self.datei.write("\t\t<Panels>")

       self.datei.write("\n\t\t\t<Panel IsProduce=\"true\" ID=\""+str(name_of_scx_file)+"\" Name=\"Test\" Length=\""+str(flc(L))+"\" Width=\""+str(flc(B))+"\" Thickness=\""+str(flc(D))+"\" MachiningPoint=\"1\">")
 
       self.datei.write("\n\t\t\t\t<Outline>")
       self.datei.write("\n\t\t\t\t\t<Point X=\""+str(flc(L))+"\" Y=\""+str(flc(B))+"\" />")
       self.datei.write("\n\t\t\t\t\t<Point X=\"0\" Y=\""+str(flc(B))+"\" />")
       self.datei.write("\n\t\t\t\t\t<Point X=\"0\" Y=\"0\" />")
       self.datei.write("\n\t\t\t\t\t<Point X=\""+str(flc(L))+"\" Y=\"0\" />")
       self.datei.write("\n\t\t\t\t</Outline>")
       self.datei.write("\n\t\t\t\t<Machines>")

    def BohrVert(self,spx,spy,dia,depth,bm):
                
        self.datei.write("\n\t\t\t\t\t<Machining Type=\"2\" IsGenCode=\"2\" Face=\""+str(bm)+"\" X=\""+str(flc(round(spx,2)))+"\" Y=\""+str(flc(round(spy,2)))+"\" Diameter=\""+str(flc(dia))+"\" Depth=\""+str(flc(depth))+"\" />")


    def BohrHoriz(self,spx,spy,spz,dia,depth,bm):

        self.datei.write("\n\t\t\t\t\t<Machining Type=\"1\" IsGenCode=\"2\" Face=\""+str(bm)+"\" X=\""+str(flc(round(spx,2)))+"\" Y=\""+str(flc(round(spy,2)))+"\" Z=\""+str(flc(round(spz,2)))+"\" Diameter=\""+str(flc(dia))+"\" Depth=\""+str(flc(depth))+"\" />")

    def Tasche(self,spx,spy,pl,pw,pr,angle,pd,dinf,ov):
       self.datei.write(
         "\r<112 \Tasche\\"
         "\rXA=\""+str(spx)+"\""
         "\rYA=\""+str(spy)+"\""
         "\rLA=\""+str(pl)+"\""
         "\rBR=\""+str(pw)+"\""
         "\rRD=\""+str(pr)+"\""
         "\rWI=\""+str(angle)+"\""
         "\rTI=\""+str(pd)+"\""
         "\rZT=\""+str(dinf)+"\""
         "\rXY=\""+str(ov)+"\""
         "\rT_=\"101\""
         "\rF_=\"5\""
         "\rDS=\"1\""
         "\rHP=\"0\""
         "\rSP=\"0\""
         "\rYVE=\"0\""
         "\rWW=\"1,2,3,401,402,403\""
         "\rASG=\"2\""
         "\rKAT=\"Tasche\""
         "\rMNM=\"Tasche\""
         "\rMX=\"0\""
         "\rMY=\"0\""
         "\rMZ=\"0\""
         "\rMXF=\"1\""
         "\rMYF=\"1\""
         "\rMZF=\"1\""
         "\r"
             )

    def Nuten(self,spx,spy,epx,epy,nb,rk,md,ti,xy):
       self.datei.write(
         "\r<109 \\Nuten\\"
         "\rXA=\""+str(spx)+"\""
         "\rYA=\""+str(spy)+"\""
         "\rWI=\"0\""
         "\rXE=\""+str(epx)+"\""
         "\rYE=\""+str(epy)+"\""
         "\rNB=\""+str(nb)+"\""
         "\rRK=\""+str(rk)+"\"" #NOWRK, WRKL, WRKR
         "\rEM=\""+str(md)+"\"" #MOD 0 1 2
         "\rAD=\"0\""
         "\rTV=\"0\""
         "\rMV=\"GL\""
         "\rTI=\""+str(ti)+"\""
         "\rXY=\"100\""
         "\rMN=\"GL\""
         "\rOP=\"0\""
         "\rAN=\"0\""
         "\rHP=\"0\""
         "\rSP=\"0\""
         "\rYVE=\"0\""
         "\rWW=\"40,41,42,45,141,142,144,145,146\""
         "\rASG=\"2\""
         "\rKAT=\"Nuten\""
         "\rMNM=\"Nuten\""
         "\rMX=\"0\""
         "\rMY=\"0\""
         "\rMZ=\"0\""
         "\rMXF=\"1\""
         "\rMYF=\"1\""
         "\rMZF=\"1\""
         "\r"		            
             )



    def End_of_file(self):
       self.datei.write("\n\t\t\t\t</Machines>")
       self.datei.write("\n\t\t\t\t<EdgeGroup X1=\"0\" Y1=\"0\">")
       self.datei.write("\n\t\t\t\t\t<Edge Face=\"2\" Thickness=\"0\" Pre_Milling=\"0\" X=\"0\" Y=\"0\" CentralAngle=\"0\" />")
       self.datei.write("\n\t\t\t\t\t<Edge Face=\"1\" Thickness=\"0\" Pre_Milling=\"0\" X=\"0\" Y=\"0\" CentralAngle=\"0\" />")
       self.datei.write("\n\t\t\t\t\t<Edge Face=\"4\" Thickness=\"0\" Pre_Milling=\"0\" X=\"0\" Y=\"0\" CentralAngle=\"0\" />")
       self.datei.write("\n\t\t\t\t\t<Edge Face=\"3\" Thickness=\"0\" Pre_Milling=\"0\" X=\"0\" Y=\"0\" CentralAngle=\"0\" />")
       self.datei.write("\n\t\t\t\t</EdgeGroup>")
       self.datei.write("\n\t\t\t</Panel>")
       self.datei.write("\n\t\t</Panels>")
       self.datei.write("\n\t</Project>")
       self.datei.write("\n</Root>")
       self.datei.close()

def run_scx(selects):
	name_of_scx_file='testfile'
	#ww=scxFile(name_of_scx_file)
	#ww.Data_head()
	#ww.Werkstck()

	b=[]

	sel = Gui.Selection.getSelection()
	print(type(sel))
	#print(sel)
	sel=list(selects[:])
	print(type(sel))

	
	for obj in sel:
		if obj.ComponentID==10:
		  #name_of_scx_file=obj.Label
		  print('\nName of scx_file',name_of_scx_file)	
			
		  dd=App.ActiveDocument.getObject(obj.Label).Parents
		  ddn=dd[0][0]
		  print(ddn.Name)
		  name_of_scx_file=ddn.Name+'_'+obj.Label		
	
	#name_of_scx_file='testfile'
	ww=scxFile(name_of_scx_file)
	ww.Data_head()

    
	#ww.Werkstck(	)
	
	
	
	
	list1=[]
	#list1 =sel
	print(sel)
	#for obj in FreeCAD.ActiveDocument.Objects:
	#    if obj.Visibility==True:
	#      list1.append(obj.ComponentID)
	#print(list1)

	for obj in sel:
		if obj.Visibility==True:
		  list1.append(obj.ComponentID)
	print(list1)

	if (10 not in list1) or (20 not in list1):
	 print('Es ist kein \"Workpiece\" oder \"Variables\" enthalten')

	#if ((10 in list1) and (20 in list1)) or ((10 in list1) and (25 in list1)) or ((10 in list1) and (30 in list1)) :
	if (True) :
	  #for myObj in FreeCAD.ActiveDocument.Objects:
	   for myObj in sel:
	     if (myObj.ComponentID==10 and myObj.Visibility==True):
	       L=(str(myObj.Length))
	       B=(str(myObj.Width))
	       D=(str(myObj.Height))
	       #ww.Variable_table(L,B,D,name_of_scx_file)
	       ww.Werkstck(L,B,D,name_of_scx_file)

	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Top'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrVert(h[0],h[1],DU,TI,'5')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')

	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Left+X'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           #ww.BohrHoriz(h[2],float(B)-h[0],h[1],DU,TI,'3')
	           ww.BohrHoriz(float(L)-h[2],h[0],h[1],DU,TI,'3')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Right-X'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(0,float(B)-h[0],h[1],DU,TI,'4')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Front+Y'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(h[0],0,h[1],DU,TI,'1')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Rear-Y'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(h[0],0,h[1],DU,TI,'2')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Bottom'):
	         #print('Bohren Bottom wird noch nicht unterstuetzt!')

	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrVert(h[0],h[1],DU,TI,'6')
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')


	     if (myObj.ComponentID==25 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Top'):
	         ww.Tasche(myObj.X,myObj.Y,myObj.Pocket_length,myObj.Pocket_width,myObj.pr,(str(myObj.Angle))[:-4], myObj.Depth,myObj.deep_infeed,myObj.overlap)
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')

	     if (myObj.ComponentID==30 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Top'):
	         if myObj.RadiusCorrection=='No':
	           rk='NOWRK'
	         if myObj.RadiusCorrection=='Left':
	           rk='WRKL'
	         if myObj.RadiusCorrection=='Right':
	           rk='WRKR'
	         if myObj.Mode=='surface':
	           md='Mod1'
	         if myObj.Mode=='ground':
	           md='Mod0'
	         if myObj.Mode=='through':
	           md='Mod2'
	     #ww.Nuten(myObj.StartX,myObj.StartY,myObj.EndX,myObj.EndY,myObj.Width,rk,md,myObj.Depth,100)
	         #ww.Nuten(0,20,300,20,12,'WRKR','Mod0',12,100)
	         ww.Nuten(myObj.StartX,myObj.StartY,myObj.EndX,myObj.EndY,myObj.Width,rk,md,myObj.Depth,100)
	         print('es wurde ', myObj.Label, ' als scx-Komponente erzeugt')

			
	ww.End_of_file()

def test_Boards():
	selects=[]
	sel_names=[]
	for obj in App.ActiveDocument.Objects:
	  if (hasattr(obj, 'ComponentID')) and (obj.Visibility==True):
	    if obj.ComponentID==10:
	        #print (obj.Label )
	        bid=obj.ID
	        sel_names.append(obj.Label)
	        selects.append(obj)
	        for obj in App.ActiveDocument.Objects:
	        	  if (hasattr(obj, 'BelongingID'))  and (obj.Visibility==True):
	        	    if obj.BelongingID==bid:
	        	      #print (obj.Label )
	        	      sel_names.append(obj.Label)
	        	      selects.append(obj)
	        if len(selects)>1:
	          #print(selects)
	          print(sel_names)
				
	          sellist=list(selects)
				
	          run_scx(sellist)
	          #test_list(sellist)         	
	          

	          #print (len(selects))
	        selects=[]
	        sel_names=[]
	print('Files exported to ',save_path)

	        #print (obj.ID)
def test_list(selects):
	for obj in selects:
		print (obj.Label)
		#print (obj[0].Label)
#test_Boards()
