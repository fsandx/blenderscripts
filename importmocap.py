import bpy

context = bpy.context
scene = context.scene
object = context.object

fileName = "C:\\Users\\fielduser\\Desktop\\Carolina\\C46_shapekeys.txt"
fileName2 = "C:\\Users\\fielduser\\Desktop\\Carolina\\C46_shapekeys_1Frame.txt"
frameNumber = 1

fileObj = open(fileName,"r")
fileStr = fileObj.read()
framesData = fileStr.splitlines()
frames = []
for frame in framesData:
	frameList = frame.split(" ")
	check = 0
	count = 0
	values = []
	for shapeKey in frameList:
		if check == 1:
			if shapeKey == "0":
				shapeKey = 0.0000
			if shapeKey == "1":
				shapeKey = 1.0000
			if shapeKey != "E":
				values.append(float(shapeKey))
		if shapeKey == "46":
			check += 1
		if shapeKey == "E":
			check = 0
		count += 1
	frames.append(values)

for frameList in frames:
	for (idx, value) in enumerate(frameList):
		# get all the id property names of the object that start with index (0 padded 2 digits) underscore.
		propnames = [name for name in object.keys() if name.startswith("%02d_" % idx)]
		#should only be one or zero
		if len(propnames):
		# ok we have a propname matching the fileindex
		# set the property that drives the shape to the value
			object[propnames[0]] = value
			# insert a keyframe for the value.
			object.keyframe_insert('["%s"]' % propnames[0], frame=frameNumber)
	frameNumber += 1
