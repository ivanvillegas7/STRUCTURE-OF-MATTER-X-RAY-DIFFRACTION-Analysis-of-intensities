# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21

@author: Iván Villegas Pérez
"""

'''
This program reads the data from a certain file, plots the difractogram and prints the values of
two times the angle at which each peak is, the sine square, and the normalization to the first peak.
'''

from typing import List

import matplotlib.pyplot as plt

#Read the data from a given file

with  open("M1-0001.x_y", "r") as infile: #Change the name for a different file.
    
    lines = infile.readlines()
        
    angle: List[str] = []

    intensity: List[float] = []

    for  line in  lines:

        vals = line.split()

        angle.append(float(vals[0]))
        
        intensity.append(float(vals[1]))

#Make the difractogram.

plt.figure()

#The text of the figure is in Spanish because I have to present the report in this lenguage.

plt.plot(angle, intensity, color='red')

plt.xlabel(r'2$\theta$ [$^o$]')

plt.ylabel(r'Intensidad [u.a.]')

plt.title(r'Difractograma de la muestra $M1-0001$')

plt.grid(True)

plt.savefig('difractograma M1-0001.pdf')
