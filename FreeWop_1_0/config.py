
import os, sys
import fakesmodule
import shared

path = os.path.dirname(fakesmodule.__file__)
templates_folder = os.path.join(path, "templates")
configfile = os.path.join(templates_folder, "config.ini")

def configwrite_corpus():
	configfile = os.path.join(templates_folder, "config_corpus.ini")
	import configparser
	config = configparser.ConfigParser()
	
	config.add_section("basics")
	config.set("basics", "parameter_1", "value_1")
	config.set("basics", "parameter_2", "value_2")
	
	#create_Corpus(obj_name,height,depth,width,tl,tr,tt,tb,offt,offb,offft,offbt,offtt,offbb)
    #create_Corpus('Corpus',600,400,300,18,18,18,18,0,0,0,0,0,0)	
	config.add_section("corpus")
	config.set("corpus", "obj_name", str(shared.corpus_template[0]))
	config.set("corpus", "height", str(shared.corpus_template[1]))
	config.set("corpus", "depth", str(shared.corpus_template[2]))
	config.set("corpus", "width", str(shared.corpus_template[3]))
	config.set("corpus", "tl", str(shared.corpus_template[4]))
	config.set("corpus", "tr", str(shared.corpus_template[5]))
	config.set("corpus", "tt", str(shared.corpus_template[6]))
	config.set("corpus", "tb", str(shared.corpus_template[7]))
	config.set("corpus", "offt", str(shared.corpus_template[8]))
	config.set("corpus", "offb", str(shared.corpus_template[9]))
	config.set("corpus", "offft", str(shared.corpus_template[10]))
	config.set("corpus", "offbt", str(shared.corpus_template[11]))
	config.set("corpus", "offtt", str(shared.corpus_template[12]))
	config.set("corpus", "offbb", str(shared.corpus_template[13]))
	with open(configfile, 'w') as example:
	   config.write(example)
	
def configread_corpus():
	configfile = os.path.join(templates_folder, "config_corpus.ini")
	import configparser
	config = configparser.ConfigParser()
	config.read(configfile)
	shared.corpus_template[0]=config.get("corpus", "obj_name")
	shared.corpus_template[1]=config.getfloat("corpus", "height")
	shared.corpus_template[2]=config.getfloat("corpus", "depth")
	shared.corpus_template[3]=config.getfloat("corpus", "width")
	shared.corpus_template[4]=config.getfloat("corpus", "tl")
	shared.corpus_template[5]=config.getfloat("corpus", "tr")
	shared.corpus_template[6]=config.getfloat("corpus", "tt")
	shared.corpus_template[7]=config.getfloat("corpus", "tb")
	shared.corpus_template[8]=config.getfloat("corpus", "offt")
	shared.corpus_template[9]=config.getfloat("corpus", "offb")
	shared.corpus_template[10]=config.getfloat("corpus", "offft")
	shared.corpus_template[11]=config.getfloat("corpus", "offbt")
	shared.corpus_template[12]=config.getfloat("corpus", "offtt")
	shared.corpus_template[13]=config.getfloat("corpus", "offbb")

#get()	Return a string value for the named option.
#getint()	Like get(), but convert value to an integer.
#getfloat()	Like get(), but convert value to a float.
#getboolean()	Like get(), but convert value to a boolean. Returns False or True.

def configwrite_drill():
	configfile = os.path.join(templates_folder, "config_drill.ini")
	import configparser
	config = configparser.ConfigParser()
	
	config.add_section("basics")
	config.set("basics", "parameter_1", "value_1")
	config.set("basics", "parameter_2", "value_2")
	
	#create_Drilling('Drilling',20,20,0,'Top',6,10,True,150,6,34,0,False,False,False,'1',True,test[0].ID)
    #Drilling(fr_obj,spx,spy,spz,dir,dia,depth,aol,lae,anz,abst,angle,mirx,miry,mp,cond,sh,bid)
	config.add_section("drill")
	config.set("drill", "fr_obj", str(shared.drill_template[0]))
	config.set("drill", "spx", str(shared.drill_template[1]))
	config.set("drill", "spy", str(shared.drill_template[2]))
	config.set("drill", "spz", str(shared.drill_template[3]))
	config.set("drill", "dir", str(shared.drill_template[4]))
	config.set("drill", "dia", str(shared.drill_template[5]))
	config.set("drill", "depth", str(shared.drill_template[6]))
	config.set("drill", "aol", str(shared.drill_template[7]))
	config.set("drill", "lae", str(shared.drill_template[8]))
	config.set("drill", "anz", str(shared.drill_template[9]))
	config.set("drill", "abst", str(shared.drill_template[10]))
	config.set("drill", "angle", str(shared.drill_template[11]))
	config.set("drill", "mirx", str(shared.drill_template[12]))
	config.set("drill", "miry", str(shared.drill_template[13]))
	config.set("drill", "mp", str(shared.drill_template[14]))
	config.set("drill", "cond", str(shared.drill_template[15]))
	config.set("drill", "sh", str(shared.drill_template[16]))
					
	with open(configfile, 'w') as example:
	   config.write(example)
	
def configread_drill():
	configfile = os.path.join(templates_folder, "config_drill.ini")
	import configparser
	config = configparser.ConfigParser()
	config.read(configfile)
	shared.drill_template[0]=config.get("drill", "fr_obj")
	shared.drill_template[1]=config.getfloat("drill", "spx")
	shared.drill_template[2]=config.getfloat("drill", "spy")
	shared.drill_template[3]=config.getfloat("drill", "spz")
	shared.drill_template[4]=config.get("drill", "dir")
	shared.drill_template[5]=config.getfloat("drill", "dia")
	shared.drill_template[6]=config.getfloat("drill", "depth")
	shared.drill_template[7]=config.getboolean("drill", "aol")
	shared.drill_template[8]=config.getfloat("drill", "lae")
	shared.drill_template[9]=config.getint("drill", "anz")
	shared.drill_template[10]=config.getfloat("drill", "abst")
	shared.drill_template[11]=config.get("drill", "angle")
	shared.drill_template[12]=config.getboolean("drill", "mirx")
	shared.drill_template[13]=config.getboolean("drill", "miry")
	shared.drill_template[13]=config.getboolean("drill", "mp")
	shared.drill_template[13]=config.get("drill", "cond")
	shared.drill_template[13]=config.getboolean("drill", "sh")

def configwrite_groove():
	configfile = os.path.join(templates_folder, "config_groove.ini")
	import configparser
	config = configparser.ConfigParser()
	
	config.add_section("basics")
	config.set("basics", "parameter_1", "value_1")
	config.set("basics", "parameter_2", "value_2")

	config.add_section("groove")
#shared.groove_template=[obj.Description, obj.StartY,obj.StartY,obj.EndX,obj.EndY,obj.Depth,obj.Width,obj.RadiusCorrection,obj.groovedirection,obj.Condition]	
#create_Grooving(obj_name,spx,spy,epx,epy,depth,wi,rc,dir,cond,bid):
#     #create_Grooving('Grooving',0,0,500,100,10,8,'No','Top','1',test[0].ID)

	config.set("groove", "obj_name", str(shared.groove_template[0]))
	config.set("groove", "spx", str(shared.groove_template[1]))
	config.set("groove", "spy", str(shared.groove_template[2]))
	config.set("groove", "epx", str(shared.groove_template[3]))
	config.set("groove", "epy", str(shared.groove_template[4]))
	config.set("groove", "depth", str(shared.groove_template[5]))
	config.set("groove", "wi", str(shared.groove_template[6]))
	config.set("groove", "rc", str(shared.groove_template[7]))
	config.set("groove", "dir", str(shared.groove_template[8]))
	config.set("groove", "cond", str(shared.groove_template[9]))
	config.set("groove", "angle", str(shared.groove_template[10]))
	config.set("groove", "com", str(shared.groove_template[11]))
	config.set("groove", "mode", str(shared.groove_template[12]))

					
	with open(configfile, 'w') as example:
	   config.write(example)
	
def configread_groove():

	configfile = os.path.join(templates_folder, "config_groove.ini")
	import configparser
	config = configparser.ConfigParser()
	config.read(configfile)

	shared.groove_template[0]=config.get("groove", "obj_name")
	shared.groove_template[1]=config.getfloat("groove", "spx")
	shared.groove_template[2]=config.getfloat("groove", "spy")
	shared.groove_template[3]=config.getfloat("groove", "epx")
	shared.groove_template[4]=config.getfloat("groove", "epy")
	shared.groove_template[5]=config.getfloat("groove", "depth")
	shared.groove_template[6]=config.getfloat("groove", "wi")
	shared.groove_template[7]=config.getboolean("groove", "rc")
	shared.groove_template[8]=config.get("groove", "dir")
	shared.groove_template[9]=config.get("groove", "cond")
	shared.groove_template[10]=config.get("groove", "angle")
	shared.groove_template[11]=config.getboolean("groove", "com")
	shared.groove_template[12]=config.get("groove", "mode")

def configwrite_pocket():
	configfile = os.path.join(templates_folder, "config_pocket.ini")
	import configparser
	config = configparser.ConfigParser()
	
	config.add_section("basics")
	config.set("basics", "parameter_1", "value_1")
	config.set("basics", "parameter_2", "value_2")
	config.add_section("pocket")
	config.set("pocket", "obj_name", str(shared.pocket_template[0]))
	config.set("pocket", "dir", str(shared.pocket_template[1]))
	config.set("pocket", "spx", str(shared.pocket_template[2]))
	config.set("pocket", "spy", str(shared.pocket_template[3]))
	config.set("pocket", "pl", str(shared.pocket_template[4]))
	config.set("pocket", "pw", str(shared.pocket_template[5]))
	config.set("pocket", "pd", str(shared.pocket_template[6]))
	config.set("pocket", "angle", str(shared.pocket_template[7]))
	config.set("pocket", "pr", str(shared.pocket_template[8]))
	config.set("pocket", "dinf", str(shared.pocket_template[9]))
	config.set("pocket", "dr", str(shared.pocket_template[10]))
	config.set("pocket", "cm", str(shared.pocket_template[11]))
	config.set("pocket", "ov", str(shared.pocket_template[12]))
	config.set("pocket", "cond", str(shared.pocket_template[13]))

					
	with open(configfile, 'w') as example:
	   config.write(example)
	
def configread_pocket():

	configfile = os.path.join(templates_folder, "config_pocket.ini")
	import configparser
	config = configparser.ConfigParser()
	config.read(configfile)

	shared.pocket_template[0]=config.get("pocket", "obj_name")
	shared.pocket_template[1]=config.get("pocket", "dir")
	shared.pocket_template[2]=config.getfloat("pocket", "spx")
	shared.pocket_template[3]=config.getfloat("pocket", "spy")
	shared.pocket_template[4]=config.getfloat("pocket", "pl")
	shared.pocket_template[5]=config.getfloat("pocket", "pw")
	shared.pocket_template[6]=config.getfloat("pocket", "pd")
	shared.pocket_template[7]=config.get("pocket", "angle")
	shared.pocket_template[8]=config.getfloat("pocket", "pr")
	shared.pocket_template[9]=config.getfloat("pocket", "dinf")
	shared.pocket_template[10]=config.get("pocket", "dr")	
	shared.pocket_template[11]=config.getboolean("pocket", "cm")	
	shared.pocket_template[12]=config.getfloat("pocket", "ov")
	shared.pocket_template[13]=config.get("pocket", "cond")
	
	#obj_name,dir,spx,spy,pl,pw,pd,angle,pr,dinf,dr,cm,ov,cond
	 #['row_of_holes', 'Top', 11.0, 22.0, 50.0, 50.0, 10.0, 0.0 deg, 15.0, 0.8, 'ccw', False, 80.0, '1']

def configwrite_mpr():
	configfile = os.path.join(templates_folder, "config_mpr.ini")
	import configparser
	config = configparser.ConfigParser()
	
	config.add_section("basics")
	config.set("basics", "parameter_1", "value_1")
	config.set("basics", "parameter_2", "value_2")
	config.add_section("mpr")
	config.set("mpr", "path_1", str(shared.mpr_template[0]))
	config.set("mpr", "path_2", str(shared.mpr_template[1]))

					
	with open(configfile, 'w') as example:
	   config.write(example)
	
def configread_mpr():

	configfile = os.path.join(templates_folder, "config_mpr.ini")
	import configparser
	config = configparser.ConfigParser()
	config.read(configfile)

	shared.mpr_template[0]=config.get("mpr", "path_1")
	shared.mpr_template[1]=config.get("mpr", "path_2")

	