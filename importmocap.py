# Script for importing Mocap data from Faceshift to Blender,
# and generate keyframe animation.

import bpy
import os

fileName = "faceshift_mocap.txt"
path = os.getcwd()


def getFileData(file):
    fileObj = open(fileName, "r")
    fileStr = fileObj.read()
    framesData = fileStr.splitlines()
    return framesData


def getShapekeyFrames(framesData):
    frames = []
    for frame in framesData:
        frameList = frame.split(" ")
        check = 0
        values = []
        for shapeKey in frameList:
            if check:
                if shapeKey != "E":
                    values.append(float(shapeKey))
            if shapeKey == "46":
                check = 1
            if shapeKey == "E":
                check = 0
        frames.append(values)
    return frames


def addKeyFramesAndProperties(shapekeyFrames):
    context = bpy.context
    object = context.object
    frameNumber = 1

    for frameList in shapekeyFrames:
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


def main():
    fileData = getFileData(path + fileName)
    shapekeyFrames = getShapekeyFrames(fileData)
    addKeyFramesAndProperties(shapekeyFrames)

