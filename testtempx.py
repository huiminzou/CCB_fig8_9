# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 21:15:37 2017

@author: xiaojian
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter,WeekdayLocator, MONDAY

timea2012=np.load('timea2012.npy')
timea2013=np.load('timea2013.npy')
timea2014=np.load('timea2014.npy')
timea2015=np.load('timea2015.npy')

timef2012=np.load('timef2012.npy')
timef2013=np.load('timef2013.npy')
timef2014=np.load('timef2014.npy')
timef2015=np.load('timef2015.npy')

tempf2015=np.load('tempf2015.npy')
tempf2014=np.load('tempf2014.npy')
tempf2013=np.load('tempf2013.npy')
tempf2012=np.load('tempf2012.npy')

tempa2015=np.load('tempa2015.npy')
tempa2014=np.load('tempa2014.npy')
tempa2013=np.load('tempa2013.npy')
tempa2012=np.load('tempa2012.npy')


t1x=np.load('t1x.npy')

t2x=np.load('t2x.npy')

time2012x=np.load('time2012x.npy')

time2013x=np.load('time2013x.npy')

f1temx=np.load('f1temx.npy')

f2temx=np.load('f2temx.npy')

temp2012x=np.load('temp2012x.npy')

temp2013x=np.load('temp2013x.npy')


fig,axes=plt.subplots(4,1,figsize=(8,10))
plt.subplots_adjust(wspace=0.1,hspace=0.35)
axes[0].plot(timea2012[0:-100],tempa2012[0:-99],label='Mooring A',color='red')
axes[1].plot(timea2013[0:-100],tempa2013[0:-99],label='Mooring A',color='red')
axes[0].plot(timef2012[0:-100],tempf2012[0:-99],label='FVCOM',color='blue')
axes[1].plot(timef2013[0:-100],tempf2013[0:-99],label='FVCOM',color='blue')

#axes[0].set_ylabel('Degrees Celsius')
#axes[1].set_ylabel('Degrees Celsius')

#axes[0].set_xlabel('a',fontsize=13)
#axes[1].set_xlabel('b',fontsize=13)
axes[0].legend()
axes[1].legend()

axes[2].plot(t1x,f1temx,label='RM04',color='red')
axes[3].plot(t2x,f2temx,label='RM04',color='red')
axes[2].plot(time2012x,temp2012x,label='FVCOM',color='blue')
axes[3].plot(time2013x,temp2013x,label='FVCOM',color='blue')

axes[2].set_ylabel('Degrees Celsius',fontsize=15)
#axes[3].set_ylabel('Degrees Celsius')
#axes[2].set_title('2012')
#axes[3].set_title('2013')
#axes[2].set_xlabel('c',fontsize=13)
#axes[3].set_xlabel('d',fontsize=13)
axes[2].legend()
axes[3].legend()

axes[0].set_ylim(6,14)
axes[1].set_ylim(6,14)
axes[2].set_ylim(6,14)
axes[3].set_ylim(6,14)
for label in axes[0].get_xticklabels():
        label.set_rotation(12)
        label.set_horizontalalignment('right')
for label in axes[1].get_xticklabels():
        label.set_rotation(12)
        label.set_horizontalalignment('right')

for label in axes[2].get_xticklabels():
        label.set_rotation(12)
        label.set_horizontalalignment('right')

for label in axes[3].get_xticklabels():
        label.set_rotation(12)
        label.set_horizontalalignment('right')

axes[0].text(timea2012[100],7,'a',fontsize=14)
axes[1].text(timea2013[100],7,'b',fontsize=14)
axes[2].text(timea2012[85],7,'c',fontsize=14)
axes[3].text(timea2013[90],7,'d',fontsize=14)
#####################set xasix###############################
mondays = WeekdayLocator(MONDAY)
weekFormatter = DateFormatter('%b %d %Y')
axes[3].xaxis.set_major_locator(mondays)

for label in axes[3].get_xticklabels():
        label.set_rotation(15)
        label.set_horizontalalignment('right')
axes[3].xaxis_date()
axes[3].xaxis_font = {'size':'13'}
axes[3].xaxis.set_major_formatter(weekFormatter)

plt.savefig('tempmfxinbtest',dpi=200,bbox_inches = "tight")
plt.savefig('Figure8.eps',format='eps',dpi=400,bbox_inches = "tight")













