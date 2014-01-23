# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:37:12 2014

@author: twoism
"""

tempInF = float(raw_input("Temperature in Farenheit:"))
tempInC = (tempInF - 32) * 5 / 9
print "Temperature in celcius:", round(tempInC,1)