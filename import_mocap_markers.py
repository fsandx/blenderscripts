import bpy

DATA_FILE = "MY_FILE.tsv"
markerNames = []
markers = []
isMarkersRead = False
cf = 0

for line in open(DATA_FILE,'r').readlines():
	if line.find("MARKER_NAMES") > -1:
		isMarkersRead = True
		markerNames = line.split()
		for markerName in markerNames:
			if markerName != "MARKER_NAMES":
				markerName = bpy.data.objects[markerName]
				markers.append(markerName)
	elif isMarkersRead:
		markerPoints = []
		point = []
		positions = line.split()
		mCount = 0
		count = 0
		for position in positions:
			if count <= 2:
				point.append(float(position))
				if count == 2:
					markers[mCount].location = (point[0], point[1], point[2])
					point = []
					count = 0
					mCount += 1
				else:
					count += 1

		cf += 1
		print("frame: ", cf)
		for marker in markers:
			marker.keyframe_insert(data_path='location', frame=(cf))
