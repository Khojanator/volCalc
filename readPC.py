#! /bin/env python
# Author: Ahsan Ali Khoja
# Contact: ahsan.khoja@gmail.com
# Dated: 04/02/2019
# Desc: A program to read and Point Cloud and divide it into planes.

def extractPC(fh, numIntervals):
	firstLine = fh.readline()
	minZ = maxZ = firstLine.split(' ')[2]
	fh.seek(0)
	pcList = []
	for row in fh.readlines():
		splitRow = row.split(' ')
		x,y,z = splitRow[:3]
		if z >= maxZ:
			maxZ = z
		if z <= minZ:
			minZ = z
		pcList.append((x,y,z))
	height = (maxZ - minZ) / numIntervals
	projectionPlanes = [[] for i in range(numIntervals)]
	for x,y,z in pcList:
		index = floor((z - minZ)/height)
		projectionPlanes[index].append((x,y))
	return projectionPlanes, height

def getVolume(projectionPlanes, height):
	volume = 0
	for plane in projectionPlanes:
		volume += (getPlaneArea(plane) * height)