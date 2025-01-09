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


import os.path
import shared
import config


__title__ = "FreeWop"
__author__ = "Frank Matzer"
__url__ = "https://www.cadialog.com"
__doc__ = "Board class with dialog"
	
save_path = 'C:\\MACHINE1\\Control\\c1\\data\\cnc\\mp4\\'                           #windows
#save_path='/home/mint/.var/app/org.freecadweb.FreeCAD/data/FreeCAD/Mod/FreeWop/cnc'    #linux
#save_path='/home/frm/mprs/'    #linux

class mprFile:
    def __init__(self,mpr_name):
       name_of_file =mpr_name
       completeName = os.path.join(save_path, name_of_file+".mpr")         
       print(completeName)
       self.datei = open(completeName,'w')

    def Data_head(self):
       self.datei.write(
         "[H"
         "\rVERSION=\"4.0 Alpha\""
         #"\rWW=\"6.0.76\""
         "\rOP=\"1\""
         "\rWRK2=\"1\""
         "\rSCHN=\"0\""
         "\rHSP=\"0\""
         "\rO2=\"0\""
         "\rO4=\"0\""
         "\rO3=\"0\""
         "\rO5=\"0\""
         "\rSR=\"0\""
         "\rFM=\"1\""
         "\rML=\"2000\""
         "\rUF=\"STANDARD\""
         "\rDN=\"STANDARD\""
         "\rDST=\"0\""
         "\rGP=\"0\""
         "\rGY=\"0\""
         "\rGXY=\"0\""
         "\rNP=\"1\""
         "\rNE=\"0\""
         "\rNA=\"0\""
         "\rBFS=\"0\""
         "\rUS=\"0\""
         "\rCB=\"0\""
         "\rUP=\"0\""
         "\rDW=\"0\""
         "\rMAT=\"HOMAG\""
         "\rEWL=\"1\""
         "\rINCH=\"0\""
         "\rVIEW=\"NOMIRROR\""
         "\rANZ=\"1\""
         "\rBES=\"0\""
         "\rENT=\"0\""
         "\rMATERIAL=\"\""
         "\rCUSTOMER=\"\""
         "\rORDER=\"\""
         "\rARTICLE=\"\""
         "\rPARTID=\"\""
         "\rPARTTYPE=\"\""
         "\rMPRCOUNT=\"1\""
         "\rMPRNUMBER=\"1\""
         "\rINFO1=\"\""
         "\rINFO2=\"\""
         "\rINFO3=\"\""
         "\rINFO4=\"\""
         "\rINFO5=\"\""
         "\r_BSX=600.000000"
         "\r_BSY=400.000000"
         "\r_BSZ=19.000000"
         "\r_FNX=0.000000"
         "\r_FNY=0.000000"
         "\r_RNX=0.000000"
         "\r_RNY=0.000000"
         "\r_RNZ=0.000000"
         "\r_RX=600.000000"
         "\r_RY=400.000000"
         "\r"
             )       
      
    def Variable_table(self,L,B,D):

       self.datei.write("\r[001\rL=\""+str(L)+"\"\rKM=\"Länge in X\"\rB=\""+str(B)+"\"\rKM=\"Breite in Y\"\rD=\""+str(D)+"\"\rKM=\"Dicke in Z\"\r") 
       #self.datei.write("\r[001\rL=\""+str(L)+"\"\rKM=\"Länge in X\"\rB=\""+str(B)+"\"\rKM=\"Breite in Y\"\rD=\""+str(D)+"\"\rKM=\"Dicke in Z\"\r")   
       #print(L,B,D) 

    def Werkstck(self):

       self.datei.write("\r<100 \\WerkStck\\\rLA=\"L\"\rBR=\"B\"\rDI=\"D\"\rFNX=\"0\"\rFNY=\"0\"\rAX=\"0\"\rAY=\"0\"\r")

    def BohrVert(self,spx,spy,dia,depth):
       self.datei.write(
         "\r<102 \\BohrVert\\"
         "\rXA=\""+str(spx)+"\""#Drill coordinate in X
         "\rYA=\""+str(spy)+"\""#Drill coordinate in Y
         "\rBM=\"LS\""#Drill mode (stringparameter):
         "\rTI=\""+str(depth)+"\""#Depth of drilling
         "\rDU=\""+str(dia)+"\""#Diameter of drilling (alternative DU or TNO)
         "\rAN=\"1\""#Number of drillings (alternative LA or AN)
         "\rMI=\"0\""#Hole row type: 0:start point- 1:center point.
         "\rS_=\"1\""#r.p.m. 0: Slow 1: Normal 2: Fast
         "\rS_P=\"100\""
         "\rAB=\"32\""#Raster distance of drillings
         "\rWI=\"0\""
         "\rZT=\"0\""
         "\rRM=\"0\""
         "\rVW=\"0\""
         "\rHP=\"0\""#Hood position (default=0)
         "\rSP=\"0\""#Spindle controlling (default=0)
         "\rYVE=\"0\""
         "\rWW=\"60,61,62,86,87,88,90,91,92,148,149,150,191,192\""
         "\rASG=\"2\""
         "\rKAT=\"Bohren vertikal\""
         "\rMNM=\"Bohren vertikal\""
         "\rORI=\"1\""
         "\rMX=\"0\""#Processing is depend from previous measures in X (default=0)
         "\rMY=\"0\""#Processing is depend from previous measures in Y (default=0)
         "\rMZ=\"0\""#Processing is depend from previous measures in Z (default=0)
         "\rMXF=\"1\""#Measuring factor in X
         "\rMYF=\"1\""#Measuring factor in Y
         "\rMZF=\"1\""#Measuring factor in Z
         "\rSYA=\"0\""
         "\rSYV=\"0\""
         "\rKO=\"00\""
         "\r"
             )

    def BohrHoriz(self,spx,spy,spz,dia,depth,bm):
       self.datei.write(
         "\r<103 \\BohrHoriz\\"
         "\rXA=\""+str(spx)+"\""#Drill coordinate in X								
         "\rYA=\""+str(spy)+"\""#Drill coordinate in Y								
         "\rZA=\""+str(spz)+"\""#Drill coordinate in Z								++
         "\rTI=\""+str(depth)+"\""#Depth of drilling								
         "\rANA=\"20\"" #Additional start distance									
         "\rDU=\""+str(dia)+"\""#Diameter of drilling (alternative DU or TNO)		
         "\rBM=\""+str(bm)+"\"" #Drill mode(string parameter):XP =0: X-Plus,XM =1: X-Minus,YP =2: Y-Plus,YM =3: Y-Minus,C =4: with free C-angle	++
         "\rAN=\"1\""#Number of drillings (alternative LA or AN)					
         "\rMI=\"0\""#Hole row type: 0:start point- 1:center point.					
         "\rS_=\"STANDARD\""														
         "\rAB=\"32\""#Raster distance of drillings									
         "\rBM2=\STD\""
         "\rWI=\"0\"" #Angle of drilling in X/Y-level. The angle will be declarated in degrees (e.g. 45.0). These parameter ist only necessary by BM=C.
         "\rZT=\"0\""																
         "\rRM=\"0\""																
         "\rVW=\"0\""																
         "\rSM=\"0\""																
         "\rHP=\"0\""#Hood position (default=0)										
         "\rSP=\"0\""#Spindle controlling (default=0)							
         "\rYVE=\"0\""															
         "\rWW=\"50,51,52,53,54,56,60,61,62,93,94,95,153,151,154,155,158,159\""		
         "\rASG=\"2\""															
         "\rKAT=\"Horizontalbohren\""											
         "\rMNM=\"Bohren horizontal\""											
         "\rORI=\"1\""																
         "\rMX=\"0\""#Processing is depend from previous measures in X (default=0)	
         "\rMY=\"0\""#Processing is depend from previous measures in Y (default=0)
         "\rMZ=\"0\""#Processing is depend from previous measures in Z (default=0)
         "\rMXF=\"1\""#Measuring factor in X										
         "\rMYF=\"1\""#Measuring factor in Y									
         "\rMZF=\"1\""#Measuring factor in Z									
         "\rSYA=\"0\""																
         "\rSYV=\"0\""																
         "\rKO=\"00\""																
         "\r"
             )

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
       self.datei.write(
         "\r!"
         "\r"
             )
       self.datei.close()

def run_mpr(selects):
	name_of_mpr_file='testfile'
	#ww=mprFile(name_of_mpr_file)
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
		  #name_of_mpr_file=obj.Label
		  print('\nName of mpr_file',name_of_mpr_file)	
			
		  dd=App.ActiveDocument.getObject(obj.Label).Parents
		  ddn=dd[0][0]
		  print(ddn.Name)
		  name_of_mpr_file=ddn.Name+'_'+obj.Label		
	
	#name_of_mpr_file='testfile'
	ww=mprFile(name_of_mpr_file)
	ww.Data_head()
	ww.Werkstck()
	
	
	
	
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
	       ww.Variable_table(L,B,D)

	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Top'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrVert(h[0],h[1],DU,TI)
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')

	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Left+X'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(h[2],float(B)-h[0],h[1],DU,TI,'0')
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Right-X'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(float(L),h[0],h[1],DU,TI,'1')
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Front+Y'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(h[0],0,h[1],DU,TI,'2')
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Rear-Y'):
	         a=App.ActiveDocument.getObject(myObj.Name).Holes
	         DU=(str(myObj.Diameter))
	         TI=(str(myObj.Depth))
	         for h in a:
	           ww.BohrHoriz(float(L)-h[0],float(B),h[1],DU,TI,'3')
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')
	     if (myObj.ComponentID==20 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Bottom'):
	         print('Bohren Bottom wird noch nicht unterstuetzt!')

	     if (myObj.ComponentID==25 and myObj.Visibility==True):
	       if (myObj.Drilldirection=='Top'):
	         ww.Tasche(myObj.X,myObj.Y,myObj.Pocket_length,myObj.Pocket_width,myObj.pr,(str(myObj.Angle))[:-4], myObj.Depth,myObj.deep_infeed,myObj.overlap)
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')

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
	         print('es wurde ', myObj.Label, ' als mpr-Komponente erzeugt')

			
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
				
	          run_mpr(sellist)
	          #test_list(sellist)         	
	          

	          #print (len(selects))
	        selects=[]
	        sel_names=[]
	print('Files exported to ',save_path)
    
	'''
	shared.mpr_template=['C:\\MACHINE1\\Control\\c1\\data\\cnc\\mp4\\','/home/frm/mprs/']
	config.configwrite_mpr()
    
    writes to paths to the configfile, 
    
    from PySide2 import QtGui, QtCore, QtWidgets
    parent = None
    file = QtWidgets.QFileDialog.getExistingDirectory(parent, "Select Directory")
    print(file)
   
    
    from PySide2.QtWidgets import QFileDialog
    filename = QFileDialog.getOpenFileName(None,"Open Project File")
    
	'''	




	        #print (obj.ID)
def test_list(selects):
	for obj in selects:
		print (obj.Label)
		#print (obj[0].Label)
#test_Boards()
