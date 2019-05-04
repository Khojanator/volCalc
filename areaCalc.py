#! /bin/env python
# Author: Ahsan Ali Khoja
# Contact: ahsan.khoja@gmail.com
# Dated: 03/01/2019
# Desc: A program to calculate area of a convex polygon bounded by points in a catesian plane

from math import atan, sqrt, pi, inf

def calcArea(coordList):
	posArea = negArea = 0
	lastCoord = coordList[-1]
	for coord in coordList:
		posArea += (coord[1] * lastCoord[0])
		negArea += (coord[0] * lastCoord[1])
		lastCoord = coord
	return (posArea - negArea)/2

def getInnerPoint(coordList):
	topX = bottomX = coordList[0][0]
	topY = bottomY = coordList[0][1]
	for x,y in coordList:
		if x > topX:
			topX = x
		elif x < bottomX:
			bottomX = x

		if y > topY:
			topY = y
		elif y < bottomY:
			bottomY = y
	return ((topX + bottomX)/2, (topY + bottomY)/2)

def createCCWList(coordList):
	innerPoint = getInnerPoint(coordList)
	translated = translatePoints(coordList, innerPoint, -1)
	polarized = polarizePoints(translated)
	sortedPolar, sortedReal = sortCCWPoints(polarized, coordList)
	return sortedReal

def translatePoints(pList, translator, const=1):
	"""Returns a list of translated points"""
	return list(map(lambda x: (x[0] + const*translator[0], x[1] + const*translator[1]), pList))

def polarizePoints(pList):
	"""Returns the list of points in Polar Coordinates in format (theta, radius)"""
	return list(map(lambda x: (getAngle(x), sqrt(x[0]**2 + x[1]**2)), pList))

def getAngle(coord):
	"""Returns the angle formed by vector from Origin to the point in the plane with the positive horizontal axis"""
	try:
		slope = coord[1]/coord[0]
	except ZeroDivisionError:
		slope = inf
	value = atan(slope)
	adjustedForQuad = value+pi if coord[0] < 0 else value
	return adjustedForQuad

def sortCCWPoints(polarPList, pList):
	"""Returns the list of points in CCW direction"""
	zippedPolarCoords = zip(polarPList, pList)
	sortedPolar, sortedReal = list(zip(*sorted(zippedPolarCoords)))
	return sortedPolar, sortedReal

def getPlaneArea(plane):
	if plane:
		CCWplane = createCCWList(plane)
		planarArea = calcArea(CCWplane)
	else:
		planarArea = 0	
	return planarArea

if __name__ == '__main__':
	A = [(1,0),(1,1),(0,1),(0,0)]
	B = [(1,1), (1,0.5), (1,0),(0.5, 1), (0.5,0), (0,0.5), (0,1),(0,0)]
	print(calcArea(A))
	print(calcArea(B))
	print(calcArea(createCCWList(B)))