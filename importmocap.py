 
import bpy
#shapekeyvalues read into a list
context = bpy.context
scene = context.scene
object = context.object
f1_shapekeyvalues= [0.233, 000,0,0.459846,0.459846,0,0,0.4688,0,0,0,0,0.248373,0.251515,0.257494,0,0,0,0,0,0,0,0.0120583,0,0,0,0,0,0.00016598,0.0290387,0.0700718,0.139935,0.0558537,0,0,0.0958857,0,0.00139159,0,0,0.0204706,0,0,0,0.000694557,0,0]
f2_shapekeyvalues= [0.111, 000,0,0.459846,0.459846,0,0,0.4688,0,0,0,0,0.248373,0.251515,0.257494,0,0,0,0,0,0,0,0.0120583,0,0,0,0,0,0.00016598,0.0290387,0.0700718,0.139935,0.0558537,0,0,0.0958857,0,0.00139159,0,0,0.0204706,0,0,0,0.000694557,0,0]
f3_shapekeyvalues= [0.333, 000,0,0.459846,0.459846,0,0,0.4688,0,0,0,0,0.248373,0.251515,0.257494,0,0,0,0,0,0,0,0.0120583,0,0,0,0,0,0.00016598,0.0290387,0.0700718,0.139935,0.0558537,0,0,0.0958857,0,0.00139159,0,0,0.0204706,0,0,0,0.000694557,0,0]
f4_shapekeyvalues= [0.999, 000,0,0.459846,0.459846,0,0,0.4688,0,0,0,0,0.248373,0.251515,0.257494,0,0,0,0,0,0,0,0.0120583,0,0,0,0,0,0.00016598,0.0290387,0.0700718,0.139935,0.0558537,0,0,0.0958857,0,0.00139159,0,0,0.0204706,0,0,0,0.000694557,0,0]
sk_values = [f1_shapekeyvalues,f2_shapekeyvalues,f3_shapekeyvalues,f4_shapekeyvalues]
frame = 1

for shapekeyvalues in sk_values:
    for (idx, value) in enumerate(shapekeyvalues):
        # get all the id property names of the object that start with index (0 padded 2 digits) underscore.
        propnames = [name for name in object.keys() if name.startswith("%02d_" % idx)]
        if len(propnames):  #should only be one or zero
            # ok we have a propname matching the fileindex
            # set the property that drives the shape to the value
            object[propnames[0]] = value
            # insert a keyframe for the value.
            object.keyframe_insert('["%s"]' % propnames[0],frame=frame)  #assume setting frame somewhere else
            #print(propnames[0])
            print(frame)
    frame +=1
            

 