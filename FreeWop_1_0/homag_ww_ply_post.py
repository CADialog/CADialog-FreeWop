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
# *   Maybe it is necessary to adjust the ouput-path.                        *
# *                                                                         *
# ***************************************************************************/
"""Postprocessor to output *.ply for WoodWop."""
import FreeCAD
import Path.Post.Utils as PostUtils
import PathScripts.PathUtils as PathUtils
import datetime
import math

global counter
counter=1


TOOLTIP = """
This is a postprocessor file for the Path workbench. It is used to 
create a polygon-file for importing into WoodWop.

"""

MACHINE_NAME = """WoodWop"""

TOOL_CHANGE = """"""

HEADER = """[H
VERSION="Konturzugliste WoodWOP 4.0 Alpha
]1

"""

PRECISION = 3

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
        #print("arctrue")
        return True
    else:
        #print("arctfalse")
        return False


def export(objectslist, filename, argstring):

    gcode = ""
    nextgcode=""
    lastgcode=""
    coordx=0.0
    coordy=0.0
    coordz=0.0
    coordi=0.0
    coordj=0.0
    lastcoordx=0
    lastcoordy=0
    lastcoordz=0
    lastcoordi=0
    lastcoordj=0
    global counter
    counter=0

    for obj in objectslist:
        for command in PathUtils.getPathWithPlacement(obj).Commands:
            
            if (command.Name=="G1" or command.Name=="G0") :
                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, PRECISION)
                        if "Y"== parameter:
                            coordy=round(value, PRECISION)                            
                        if "Z"== parameter:
                            coordz=round(value, PRECISION)
                
                lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj
                if counter==0:
                    
                    "SIZE X1 Y1\nU\nX0.0Y0.0\nD\n"
                    nextgcode="SIZE X1.0 Y1.0\nU\n"+"X"+str(coordx)+" Y"+str(coordy)+"\nD"
                    if nextgcode!=lastgcode:
                        gcode=gcode+nextgcode
                        lastgcode=nextgcode  

                else:
                    nextgcode="\nX"+str(coordx)+" Y"+str(coordy)+" Z"+str(coordz) 
                    if nextgcode!=lastgcode:
                        gcode=gcode+nextgcode
                        lastgcode=nextgcode

                counter=counter+1
            if command.Name=="G3":
                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, PRECISION)
                        if "Y"== parameter:
                            coordy=round(value, PRECISION)                            
                        if "Z"== parameter:
                            coordz=round(value, PRECISION)
                        if "I"== parameter:
                            coordi=round(value, PRECISION)
                        if "J"== parameter:
                            coordj=round(value, PRECISION)                            
                
                rarc=angleUnder180("G3",lastcoordx,lastcoordy,coordx,coordy,coordi,coordj,)
                if rarc==True:
                    ds="1"
                else:
                    ds="3"
                absi=round((lastcoordx+coordi),PRECISION)
                absj=round((lastcoordy+coordj),PRECISION)
                lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj
         
                nextgcode ="\nX"+str(coordx)+" Y"+str(coordy)+" Z"+str(coordz)+" I"+str(absi)+" J"+str(absj)+" CCW" 
                if nextgcode!=lastgcode:
                        gcode=gcode+nextgcode
                        lastgcode=nextgcode
                
                counter=counter+1
            if command.Name=="G2":

                for parameter, value in command.Parameters.items():
                    if "F"!= parameter:
                        if "X"== parameter:
                            coordx=round(value, PRECISION)
                        if "Y"== parameter:
                            coordy=round(value, PRECISION)                            
                        if "Z"== parameter:
                            coordz=round(value, PRECISION)
                        if "I"== parameter:
                            coordi=round(value, PRECISION)
                        if "J"== parameter:
                            coordj=round(value, PRECISION)                            
                
                rarc=angleUnder180("G2",lastcoordx,lastcoordy,coordx,coordy,coordi,coordj,)
                if rarc==True:
                    ds="0"
                else:
                    ds="2"
                absi=round((lastcoordx+coordi),PRECISION)
                absj=round((lastcoordy+coordj),PRECISION)         
                lastcoordx,lastcoordy,lastcoordz,lastcoordi,lastcoordj=coordx,coordy,coordz,coordi,coordj

                nextgcode ="\nX"+str(coordx)+" Y"+str(coordy)+" Z"+str(coordz)+" I"+str(absi)+" J"+str(absj)+" CW" 
                if nextgcode!=lastgcode:
                        gcode=gcode+nextgcode
                        lastgcode=nextgcode
                
                counter=counter+1

    # Open editor window
    if FreeCAD.GuiUp:
        dia = PostUtils.GCodeEditorDialog()
        dia.editor.setText(gcode)
        result = dia.exec_()
        if result:
            gcode = dia.editor.toPlainText()

 
        gfile = open("C:\\MACHINE1\\Control\\c1\\data\\cnc\\ml4\\testit.ply", "w")
        
        
        gfile.write(gcode)
        gfile.close()

    return filename
