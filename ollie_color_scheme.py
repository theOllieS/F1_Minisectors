#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from matplotlib import pyplot as plt
import matplotlib.font_manager as font_manager
import os
from matplotlib import font_manager as fm, rcParams





fpath = os.path.join(rcParams["datapath"], "/Users/........./Formula1-Regular.ttf")#Download F1 font https://www.formula1.com/etc/designs/fom-website/fonts/F1Regular/Formula1-Regular.ttf
prop = fm.FontProperties(fname=fpath)
f1font = os.path.split(fpath)[1]

fpathbold = os.path.join(rcParams["datapath"], "/Users/........./Formula1-Bold.ttf")#Download F1 font https://www.formula1.com/etc/designs/fom-website/fonts/F1Regular/Formula1-Regular.ttf
prop_bold = fm.FontProperties(fname=fpathbold)
f1fontbold = os.path.split(fpathbold)[1]


def ollie_color_scheme():
    plt.rcParams['figure.facecolor'] = '#141414'
    plt.rcParams['axes.edgecolor'] = '#ffffff'
    plt.rcParams['xtick.color'] = '#f1f2f3'
    plt.rcParams['ytick.color'] = '#f1f2f3'   
    plt.rcParams['axes.labelcolor'] = '#F1f2f3'
    plt.rcParams['axes.facecolor'] = '#141414'
    # plt.rcParams['axes.facecolor'] = '#292625'
    plt.rcParams['axes.titlesize'] = 'x-large'
    plt.rcParams['font.family'] = 'f1font'
    plt.rcParams['font.weight'] = 'medium'
    plt.rcParams['text.color'] = '#ffffff'
    plt.rcParams['axes.titlesize'] = '19'
    plt.rcParams['axes.titlepad'] = '12'
    plt.rcParams['axes.titleweight'] = 'light'
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['legend.fancybox'] = False
    plt.rcParams['legend.facecolor'] = (0.1, 0.1, 0.1, 0.7)
    plt.rcParams['legend.edgecolor'] = (0.1, 0.1, 0.1, 0.9)
    plt.rcParams['legend.markerscale'] = 10
    plt.rcParams['savefig.transparent'] = False
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['grid.color'] = '#999999'
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['grid.linewidth'] = 0.75

ollie_color_scheme()
    
