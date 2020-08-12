# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 05:27:32 2020

@author: So Yee Cheung

Radio astronomy - plotting gaintable

This program is only applicable when CASA is started.

For ploting out gainsolutions for each spectral window in each correlation in each antenna.

I wrote this program based on VLA, it can be modified to process data from other telescopes.
"""
def plotter(visfile,f,x,y,colorax,expform,show): # depending on the situation, can also add spectral window parameter
    antennalist = []
    for i in range(1,30): # list out all antennas in antennalist, VLA has 29 antennas
        if i < 10:
            antennalist.append('VA0'+str(i))
        else:
            antennalist.append('VA'+str(i))
    for ant in antennalist: # iterate over antennas
        for corr in ['L','R']: # iterate over correlations, for cal tables options for correlations are: ’R’,’L’,’RL’,’X’,’Y’,’XY’,’/’
            plotms(vis=visfile,xaxis=x,yaxis=y,field=f,coloraxis=colorax,expformat=expform,showgui=show,correlation=corr,antenna=ant,plotfile='AL525_C001223_markup/'+y+'/'+ant+'_'+y+'_'+corr+'.'+expform)

