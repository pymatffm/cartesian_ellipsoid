#!/usr/bin/env python
#*-* coding: utf-8 *-*
import numpy as np

'''
Class takes Cartesian coordinates as input
'''
class Cart_To_Ellip:
        def __init__(self, x, y, z):   
            lam, phi, h = self.cartesian_to_ellipsoidal(x, y, z) 


        def cartesian_to_ellipsoidal(self, x, y, z):
            r = np.sqrt(x**2 + y**2 + z**2)
            
            # WGS-84 PARAMETERS, semimajor and semiminor axis
            a = 6378137.0
            b = 6356752.314
            
            # Eccentricity
            e_squared = (a**2 - b**2) / a**2
            
            # Auxiliary quantities
            p = np.sqrt(x**2 + y**2)
            
            # Latitude (phi) & Longitude (lam)
            phi = np.rad2deg(np.arctan(z / ((1- e_squared) * p)))
            lam = np.rad2deg(np.arctan(y/x))
            
            # Radius of curvature in prime vertical
            N = a / np.sqrt(1 - e_squared * (np.sin(np.deg2rad(phi)))**2)
            
            # Altitude
            h = (p / np.cos(np.deg2rad(phi))) - N
            
            return lam, phi, h