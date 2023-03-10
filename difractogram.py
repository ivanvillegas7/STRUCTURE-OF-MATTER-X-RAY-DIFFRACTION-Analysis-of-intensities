# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21

@author: Iván Villegas Pérez
"""

'''
This program reads the data from a certain file, plots the difractogram and prints the values of
two times the angle at which each peak is, the sine square, and the normalization to the first peak.
'''

import numpy as np

from typing import List

import matplotlib.pyplot as plt

#Read the data from a given file

with  open("M1-0001.x_y", "r") as infile: #Change the name for a different file.
    
    lines = infile.readlines()
        
    angle: List[str] = []

    intensity: List[float] = []
        
    #You might need to create more lists if you have more peaks. Or delete some if you have less.
    
    peak1_a: List[float] = []
    
    peak1_i: List[float] =[]
    
    peak2_a: List[float] = []
    
    peak2_i: List[float] =[]
    
    peak3_a: List[float] = []
    
    peak3_i: List[float] =[]
    
    peak4_a: List[float] = []
    
    peak4_i: List[float] =[]
    
    peak5_a: List[float] = []
    
    peak5_i: List[float] =[]
    
    peak6_a: List[float] = []
    
    peak6_i: List[float] =[]

    for  line in  lines:

        vals = line.split()

        angle.append(float(vals[0]))
        
        intensity.append(float(vals[1]))
        
        #You might have to change the values for a different file.

        if float(vals[0]) >= 27 and float(vals[0]) <= 30:
            
            peak1_a.append(float(vals[0]))
            
            peak1_i.append(float(vals[1]))
            
        elif float(vals[0]) >= 39 and float(vals[0]) <= 42:
            
            peak2_a.append(float(vals[0]))
            
            peak2_i.append(float(vals[1]))
            
        elif float(vals[0]) >= 49 and float(vals[0]) <= 52:
            
            peak3_a.append(float(vals[0]))
            
            peak3_i.append(float(vals[1]))
            
        elif float(vals[0]) >= 56 and float(vals[0]) <= 60:
            
            peak4_a.append(float(vals[0]))
            
            peak4_i.append(float(vals[1]))
            
        elif float(vals[0]) >= 65 and float(vals[0]) <= 69:
            
            peak5_a.append(float(vals[0]))
            
            peak5_i.append(float(vals[1]))
            
        elif float(vals[0]) >= 70 and float(vals[0]) <= 78:
            
            peak6_a.append(float(vals[0]))
            
            peak6_i.append(float(vals[1]))

#%%

#Make the difractogram.

plt.figure()

#The text of the figure is in Spanish because I have to present the report in this lenguage.

plt.plot(angle, intensity, color='red')

plt.xlabel(r'2$\theta$ [$^o$]')

plt.ylabel(r'Intensidad [u.a.]')

plt.title(r'Difractograma de la muestra $M1-0001$')

plt.grid(True)

plt.savefig('difractograma M1-0001.pdf')

#%%

def index_max(intensity_peak: List[float]) -> int:
    
    '''
    This function computes the iondex of the highest element in a given list.
    
    Parameters:
        -intensity_peak: list of intensities in a short angular range; the list should have the name peakj_i, where j is a number.
    Returns:
        -index: index at which the maximum element of the given list is located.
    '''
    
    index: int = intensity_peak.index(max(intensity_peak))
    
    return index

#Print the values needed for the indexation.

print(f'\nFirst visible peak angle is 2θ = {peak1_a[index_max(peak1_i)]}.\n')

print(f'Sin^2(θ1) = {np.sin(peak1_a[index_max(peak1_i)]*np.pi/(2*180))**2}\n')

print(f'Second visible peak angle is 2θ = {peak2_a[index_max(peak2_i)]}.\n')

print(f'Sin^2(θ2) = {np.sin(peak2_a[index_max(peak2_i)]*np.pi/(2*180))**2}\n')

print(f'Third visible peak angle is 2θ = {peak3_a[index_max(peak3_i)]}.\n')

print(f'Sin^2(θ3) = {np.sin(peak3_a[index_max(peak3_i)]*np.pi/(2*180))**2}\n')

print(f'Fourth visible peak angle is 2θ = {peak4_a[index_max(peak4_i)]}.\n')

print(f'Sin^2(θ4) = {np.sin(peak4_a[index_max(peak4_i)]*np.pi/(2*180))**2}\n')

print(f'Fifth visible peak angle is 2θ = {peak5_a[index_max(peak5_i)]}.\n')

print(f'Sin^2(θ5) = {np.sin(peak5_a[index_max(peak5_i)]*np.pi/(2*180))**2}\n')

print(f'Sixth visible peak angle is 2θ = {peak6_a[index_max(peak6_i)]}.\n')

print(f'Sin^2(θ6) = {np.sin(peak6_a[index_max(peak6_i)]*np.pi/(2*180))**2}\n')
