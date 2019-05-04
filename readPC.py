#! /bin/env python
# Author: Ahsan Ali Khoja
# Contact: ahsan.khoja@gmail.com
# Dated: 04/02/2019
# Desc: A program to read and Point Cloud and divide it into planes.

from areaCalc import getPlaneArea
from math import floor
from readArgs import argumentHandler

def extractPC(fh, numIntervals):
	uniqueZ = dict()
	zCount = 0
	firstLine = fh.readline()
	firstLine = firstLine.split(' ')
	minZ = maxZ = eval(firstLine[2])
	rowLen = len(firstLine)
	fh.seek(0)
	pcList = []
	for row in fh.readlines():
		splitRow = row.split(' ')
		if len(splitRow) == rowLen:
			x,y,z = [eval(i) for i in splitRow[:3]]
			if z >= maxZ:
				maxZ = z
			if z <= minZ:
				minZ = z
			pcList.append((x,y,z))
			if not uniqueZ.get(z):
				uniqueZ[z] = 1
				zCount += 1
		else:
			break
	print("Number of Unique z values:", zCount)
	height = (maxZ - minZ) / numIntervals
	projectionPlanes = [[] for i in range(numIntervals)]
	for x,y,z in pcList:
		index = floor((z - minZ)/height)
		if index == numIntervals:
			index -= 1
		projectionPlanes[index].append((x,y))
	return projectionPlanes, height

def getVolume(projectionPlanes, height):
	volume = 0
	for plane in projectionPlanes:
		volume += (getPlaneArea(plane) * height)
	return volume

if __name__ == '__main__':
	args = vars(argumentHandler())
	numSlices = args['numSlices']
	fname = args['inFile']
	# z = 2500
	# fname = "/home/khojanator/Documents/EC/CS488/FinalProject/dataset/vase.ply"
	filehandle = open(fname, 'r')
	projectionPlanes, height = extractPC(filehandle, numSlices)
	filehandle.close()
	print("Number of slices used:", numSlices)
	print("Volume of Point Cloud:", getVolume(projectionPlanes, height))