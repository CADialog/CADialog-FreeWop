# ***************************************************************************
# *   Copyright (c) 2023 CADialog <info@cadialog.com>                       *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************/
# *                                                                         *
# *   The post processor is made up of various elements of                  *
# *   existing post processors and is therefore based on                    *
# *   the know-how of others, thanks!                                       *
# *   There is no experience from real production yet.                      *
# *   Maybe it is necessary to adjust the ouput-path.                       *
# *                                                                         *
# ***************************************************************************/
"""Postprocessor to output *.ktr for WoodWop."""
import FreeCAD
import Path.Post.Utils as PostUtils
import PathScripts.PathUtils as PathUtils
import datetime
import math

global counter
counter=0


TOOLTIP = """
This is a postprocessor file for the Path workbench. It is used to 
create a contour list for importing into WoodWop.

"""

MACHINE_NAME = """WoodWop"""


TOOL_CHANGE = """"""

HEADER = """[H
VERSION="Konturzugliste WoodWOP 4.0 Alpha
]1"""


if FreeCAD.ActiveDocument:
    cam_file = FreeCAD.ActiveDocument.FileName
else:
    cam_file = "<None>"

def angleUnder180(command, lastX, lastY, x, y, i, j):
    # radius R can be used iff angle is < 180.
    # This is the case
    #   if the previous point is left of the current and the center is below (or on) the connection line
    # or if the previous point is right of the current and the center is above
    # (or on) the connection line
    middleOfLineY = (lastY + y) / 2
    centerY = lastY + j
    if (
        command == "G2"
        and (
            (lastX == x and ((lastY < y and i >= 0) or (lastY > y and i <= 0)))
            or (lastX < x and centerY <= middleOfLineY)
            or (lastX > x and centerY >= middleOfLineY)
        )
    ) or (
        command == "G3"
        and (
            (lastX == x and ((lastY < y and i <= 0) or (lastY > y and i >= 0)))
            or (lastX < x and centerY >= middleOfLineY)
            or (lastX > x and centerY <= middleOfLineY)
        )
    ):
        return True
    else:
        return False


def export(objectslist, filename, argstring):

    gcode = ""
    nextgcode=""
    lastgcode=""
    coordx=0
    coordy=0
    coordz=0
    coordi=0
    coordj=0
    lastcoordx=0
    lastcoordy=0
    lastcoordz=0
    lastcoordi=0
    lastcoordj=0
    global counter
    counter=0

    gcode = HEADER
    
    
    
    for obj in objectslist:
        for command in PathUtils.getPathWithPlacement(obj).Commands:
            if (command.Name=="G1" or command.Name=="G0") :
                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, 5)
                        if "Y"== parameter:
                            coordy=round(value, 5)                            
                        if "Z"== parameter:
                            coordz=round(value, 5)
                wi=0
                dx=float(coordx)-float(lastcoordx)
                dy=float(coordy)-float(lastcoordy)
                dz=float(coordz)-float(lastcoordz)
                if dx !=0:
                    wi=math.atan(dy/dx)
                    
                if dx ==0 and dy >0:   
                    wi=1.5707963
                print(dx,dy,dz,wi)

                if counter==0:
                    nextgcode="\n\n$E"+str(counter)+"\n"+"KP\n"+"X="+(str(coordx))+"\n"+"Y="+(str(coordy))+"\n"+"Z="+(str(coordz))\
                    +"\n.KO=00"+"\n.X="+(str(coordx))+"\n"+".Y="+(str(coordy))+"\n"+".Z="+(str(coordz))+"\n.KO=00"
                    if nextgcode!=lastgcode:
                        gcode=gcode+nextgcode
                        lastgcode=nextgcode
                  
                    lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj
                    counter=counter+1
                else:

                    nextgcode="KL\n"+"X="+(str(coordx))+"\n"+"Y="+(str(coordy))+"\n"+"Z="+(str(coordz))\
                    +"\n.X="+(str(coordx))+"\n"+".Y="+(str(coordy))+"\n"+".Z="+(str(coordz))+"\n.WI="+str(wi)+"\n.WZ=0.0" 
                                       
                    if (nextgcode!=lastgcode)and ((lastcoordx!=coordx)or (lastcoordy!=coordy)or (lastcoordz!=coordz)):
                        gcode=gcode+"\n\n$E"+str(counter)+"\n"+nextgcode
                        lastgcode=nextgcode
                        counter=counter+1
                    lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj

            if command.Name=="G3":

                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, 5)
                        if "Y"== parameter:
                            coordy=round(value, 5)                            
                        if "Z"== parameter:
                            coordz=round(value, 5)
                        if "I"== parameter:
                            coordi=round(value, 5)
                        if "J"== parameter:
                            coordj=round(value, 5)                            
                
                rarc=angleUnder180("G3",lastcoordx,lastcoordy,coordx,coordy,coordi,coordj,)
                if rarc==True:
                    ds="1"
                else:
                    ds="3"
                absi=lastcoordx+coordi
                absj=lastcoordy+coordj

                wi=0
                dx=float(coordx)-float(lastcoordx)
                dy=float(coordy)-float(lastcoordy)
                dz=float(coordz)-float(lastcoordz)
                if dx !=0:
                    wi=math.atan(dy/dx)
                    
                if dx ==0 and dy >0:   
                    wi=1.5707963

                gcode += "\n"
                nextgcode ="KA\n"+"X="+str(coordx)+"\n"+"Y="+str(coordy)+"\n"+"Z="+str(coordz)+"\nDS="+ds+"\nR="+str(round(math.sqrt(coordi**2 + coordj**2),5))+"\n.X="+str(coordx)+"\n"+".Y="+str(coordy)+"\n"+".Z="+str(coordz)+"\n.I="+str(coordi)+"\n.J.="+str(coordj)+"\n.DS="+ds+"\n.R="+str(round(math.sqrt(coordi**2 + coordj**2),5))+"\n.WI="+str(wi)
                if nextgcode!=lastgcode:
                        gcode=gcode+"\n$E"+str(counter)+"\n"+nextgcode
                        lastgcode=nextgcode
                        lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj
                gcode += "\n"
            if command.Name=="G2":
                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, 5)
                        if "Y"== parameter:
                            coordy=round(value, 5)                            
                        if "Z"== parameter:
                            coordz=round(value, 5)
                        if "I"== parameter:
                            coordi=round(value, 5)
                        if "J"== parameter:
                            coordj=round(value, 5)                            
                
                rarc=angleUnder180("G2",lastcoordx,lastcoordy,coordx,coordy,coordi,coordj,)
                if rarc==True:
                    ds="0"
                else:
                    ds="2"
                absi=lastcoordx+coordi
                absj=lastcoordy+coordj          
                wi=0
                dx=float(coordx)-float(lastcoordx)
                dy=float(coordy)-float(lastcoordy)
                dz=float(coordz)-float(lastcoordz)
                if dx !=0:
                    wi=math.atan(dy/dx)
                    
                if dx ==0 and dy >0:   
                    wi=1.5707963
                gcode += "\n"
                nextgcode ="KA\n"+"X="+str(coordx)+"\n"+"Y="+str(coordy)+"\n"+"Z="+str(coordz)+"\nDS="+ds+"\nR="+str(round(math.sqrt(coordi**2 + coordj**2),5))+"\n.X="+str(coordx)+"\n"+".Y="+str(coordy)+"\n"+".Z="+str(coordz)+"\n.I="+str(coordi)+"\n.J.="+str(coordj)+"\n.DS="+ds+"\n.R="+str(round(math.sqrt(coordi**2 + coordj**2),5))+"\n.WI="+str(wi)
                if nextgcode!=lastgcode:
                        gcode=gcode+"\n$E"+str(counter)+"\n"+nextgcode
                        lastgcode=nextgcode
                        lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj
                gcode += "\n"

    gcode += "\n!\n"

    # Open editor window
    if FreeCAD.GuiUp:
        dia = PostUtils.GCodeEditorDialog()
        dia.editor.setText(gcode)
        result = dia.exec_()
        if result:
            gcode = dia.editor.toPlainText()
        gfile = open("C:\\MACHINE1\\Control\\c1\\data\\cnc\\ml4\\testit.ktr", "w")
        gfile.write(gcode)
        gfile.close()

    return filename
