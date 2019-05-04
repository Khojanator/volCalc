#! /bin/env python
# Author: Ahsan Ali Khoja
# Contact: ahsan.khoja@gmail.com
# Dated: 05/02/2019
# Desc: A program to read command-line arguments for volCalc algorithm

import argparse

USE = "Program for generating volume of a point cloud using slicing algorithm.\nExample: user$ python readPC.py -i bunny.ply -n 50"

def argumentHandler():
    parser = argparse.ArgumentParser(description=USE, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--inFile', help='Enter the input point cloud file', required=True, dest="inFile")
    parser.add_argument('-n', '--numSlices', help='Enter the number of slices you want to divide the point cloud into', required=True, dest="numSlices", type=int)

    return parser.parse_args()