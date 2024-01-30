# this script generates csvlist of selected objects and its dimensions in mm so it can be inserted in to cuting rod solver 
# import modules
import bpy, os
# get the selection
selection = bpy.context.selected_objects
# initialize a blank result variable
result = ""
# iterate through the selected objects
for sel in selection:
    # get the current object's dimensions
    dims = sel.dimensions
    # write the selected object's name and dimensions to a string multiple by 1000 to get mm discard pointer
    result += "%s \t %.0f mm \t %.0f mm \t %.0f mm\n" % (sel.name, dims.x*1000, dims.y*1000, dims.z*1000)
# get path to render output (usually /tmp\)
tempFolder = os.path.abspath (bpy.context.scene.render.filepath)
# make a filename
filename = os.path.join (tempFolder, "dimeensions.csv")
# open a file to write to
file = open(filename, "w")
# write the data to file
file.write(result)
# close the file
file.close()
