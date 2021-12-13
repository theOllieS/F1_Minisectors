#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:01:16 2021

@author: olliesowden
"""

" F1 Minisectors without custom font "




import fastf1 
from fastf1 import plotting
from driver_year_color import *
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import matplotlib as mpl
import matplotlib.font_manager as font_manager
import os
from matplotlib import font_manager as fm, rcParams
import datetime





# Enable cache
fastf1.Cache.enable_cache('/Users/olliesowden/.spyder-py3/F1 data') #change to unique cache location



# Load the session
session = fastf1.get_session(2021, 'Abu Dhabi Grand Prix' ,  'Q')


# Load all laps with telemetry
laps = session.load_laps(with_telemetry=True)

 
# Retrieve data from laps within 102.5% of best session time
# Allows for more reliable data collection
laps=laps.pick_quicklaps(threshold=1.03)



# Select only fast laps in Q3      # Not sure how to keep accurate if Q3 red flag
# Can hash out / delete for FP sessions
laps = laps.loc[laps['Time'] >= (laps['Time'].max() - datetime.timedelta(minutes = 14))]

# Get all unique driver number and TLAs
drv_num=laps['DriverNumber'].unique().astype(int)
# All drivers that completed fast laps in Q3
drivers=laps['Driver'].unique()  


# Create list of wanted drivers e.g. head to head with two drivers ['HAM', 'VER']
driver_list = []        # Make = [] if want all drivers


# If you want all drivers laps from Q3 use driver_list = drivers.tolist()
#driver_list = drivers.tolist()


# Something like...
if len(driver_list) == 0:
    driver_list = drivers.tolist()



telemetry = pd.DataFrame()

for driver in driver_list: #Gets telemetry for all drivers in list 

   driver_telemetry = laps.pick_driver(driver).pick_fastest().get_telemetry().add_distance() #Picks fastest lap in Q3
   driver_telemetry['Driver'] = driver
   driver_telemetry['Colour'] = driver_year_color(laps.pick_driver(driver).pick_fastest()['Driver'], session.weekend.year)
   
   telemetry = telemetry.append(driver_telemetry)


# Only keep columns that we want/need for later
telemetry = telemetry[[ 'Distance', 'Speed', 'X', 'Y', 'Driver', 'Colour']]    



" Credit @jasperhvat on medium for this snippet and inspiration"
#https://medium.com/towards-formula-1-analysis/formula-1-data-analysis-tutorial-2021-russian-gp-to-box-or-not-to-box-da6399bd4a39


# Choose how many minisectors we want e.g. 25
num_minisectors = 25

# What is the total distance of a lap?
total_distance = max(telemetry['Distance']) #Not the same for all, maybe find a better method

# Generate equally sized mini-sectors 
minisector_length = total_distance / num_minisectors

#Assign distances to each minisector
minisectors = [0]

for i in range(0, (num_minisectors - 1)):
    minisectors.append(minisector_length * (i + 1))



# Assign minisector to every row in the telemetry data
telemetry['Minisector'] =  telemetry['Distance'].apply(
  lambda z: (
    minisectors.index(
      min(minisectors, key=lambda x: abs(x-z)))+1
  )
)



# Calculate fastest driver (highest average speed) per mini sector
average_speed = telemetry.groupby(['Minisector' , 'Driver'])['Speed'].mean().reset_index()


# Select the driver with the highest average speed
fastest_drivers= average_speed.loc[average_speed.groupby(['Minisector', 'Driver'])['Speed'].idxmax()]



#Perhaps for use later in interactive sector plot
b=fastest_drivers.sort_values(by=['Minisector', 'Speed'])  #try to have speed descending order?


# Sort to find fastest driver for each minisector
fastest_minisector = fastest_drivers.sort_values('Speed', ascending = False).drop_duplicates(['Minisector'])
fastest_minisector = fastest_minisector.sort_values(by = ['Minisector'])
fastest_minisector = fastest_minisector[[ 'Minisector', 'Driver' , 'Speed']].rename(columns={'Speed': 'Sector_avg_speed', 'Driver' : 'Fastest_driver'})


# Get rid of the speed column and rename the driver column
fastest_drivers = fastest_drivers[[ 'Minisector', 'Driver']].rename(columns={'Driver': 'Fastest_driver'})



# Join the fastest minisector dataframe with the full telemetry
# to merge minisector, fastest driver in each and avg speed in that minisector
telemetry = telemetry.merge(fastest_minisector, on=['Minisector'])

# Order the data by distance
telemetry = telemetry.sort_values(by=['Distance'])


# Assign integer value to the fastest driver in each minisector (driver number)
for driver in driver_list: 
    telemetry.loc[telemetry['Fastest_driver'] == driver , 'Fastest_driver_int'] = int(drv_num[np.where(drivers==driver)])
            

# Get X, Y coordinates of the circuit
x = np.array(telemetry['X'].values)
y = np.array(telemetry['Y'].values)

# Divide up the circuit into 2D into segments
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)


minisector_int = telemetry['Fastest_driver_int'].to_numpy().astype(float)


minisector_fastest_drivers = telemetry['Fastest_driver'].unique()
minisector_fastest_drivers_num = telemetry['Fastest_driver_int'].unique()


minisector_colours = []

for driver in minisector_fastest_drivers:
   minisector_colours.append(driver_year_color(laps.pick_driver(driver).pick_fastest()['Driver'], session.weekend.year))
   
minisector_colours = np.array(minisector_colours)



minisector_details = pd.DataFrame({'Fastest_driver' : minisector_fastest_drivers, 'Fastest_driver_int' : minisector_fastest_drivers_num, 'Minisector_colours' :  minisector_colours }, columns=['Fastest_driver', 'Fastest_driver_int', 'Minisector_colours'])


# Sort order by driver number min to max. 
minisector_details = minisector_details.sort_values(by = ['Fastest_driver_int'])

# Get driver number, colour, name for plotting
num_list_ordered = minisector_details['Fastest_driver_int'].tolist()
colour_list_ordered = minisector_details['Minisector_colours'].tolist()
driver_name_ordered = minisector_details['Fastest_driver'].tolist()

############################################################################################################################################


"This seems to work despite but i dont really undertsand why"

#Quick fix to sort out colorbar error, add 1 to the last number
num_list_ordered.insert(len(num_list_ordered),(num_list_ordered[-1] +1))

##############################################################################################################################

# Create figure and size of the figure
fig, ax = plt.rcParams['figure.figsize'] = [16, 9]

# Define the colour map using the driver colours
cmap = mpl.colors.ListedColormap(colour_list_ordered)
cmap.set_over('0.25')
cmap.set_under('0.75')

bounds = num_list_ordered
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# Create a linecollection of segments using the colour map
lc_comp = LineCollection(segments, norm=norm, cmap=cmap)
lc_comp.set_array(minisector_int)
lc_comp.set_linewidth(4)

# Plot the linecollection
plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.axis('off')




# For 1v1 driver vs driver
#plt.title((driver_list[0] + ' vs ' + driver_list[1] + ' ' + str(session.weekend.year) + ' ' + str(session.weekend.name) + ' ' + str(session.name) + '\n' + 'Number of minisectors = ' + str(num_minisectors) ), fontsize = 20)

# For many drivers
plt.title((str(session.weekend.year) + ' ' + str(session.weekend.name) + ' ' + str(session.name) + '\n' + 'Number of minisectors = ' + str(num_minisectors) ), fontsize = 20)



plt.show()




"An attempt to annotate map with driver numbers"
"There is probably a much cleaner way to do this"

"WARNING:- VERY MESSY"


"Effectively the same thing as before but with x,y coordinates"
############################################################################################################################################


# Calculate the average (mean) x,y positions of the fastest minisectors
average_xy = telemetry.groupby(['Minisector' , 'Driver'])['Speed' , 'X', 'Y'].mean().reset_index()
# Ideally the median (x,y) would work best but it doesnt select the driver with the highest mean speed through the sector


# Select the driver with the highest average speed
fastest_drivers_xy= average_xy.loc[average_xy.groupby(['Minisector', 'Driver', 'Y', 'X'])['Speed'].idxmax()]



# Sort to find fastest driver for each minisector
fastest_minisector_xy = fastest_drivers_xy.sort_values('Speed', ascending = False).drop_duplicates(['Minisector'])
fastest_minisector_xy = fastest_minisector_xy.sort_values(by = ['Minisector'])
fastest_minisector_xy = fastest_minisector_xy[[ 'Minisector', 'Driver' , 'Speed', 'X', 'Y']].rename(columns={'Speed': 'Sector_avg_speed', 'Driver' : 'Fastest_driver', 'X' : 'X_avg' , 'Y' : 'Y_avg'})


# Rename the driver column
fastest_drivers_xy = fastest_drivers_xy[[ 'Minisector', 'Driver',  'Speed', 'X', 'Y']].rename(columns={'Driver': 'Fastest_driver', 'X' : 'X_avg' , 'Y' : 'Y_avg'})


############################################################################################################################################


for driver in fastest_minisector_xy['Fastest_driver']:
    fastest_minisector_xy.loc[fastest_minisector_xy['Fastest_driver'] == driver , 'Fastest_driver_int'] = int(drv_num[np.where(drivers==driver)])
    

# Take the mean x,y coordinates for each minisector
x_coords = fastest_minisector_xy['X_avg'].tolist()
y_coords = fastest_minisector_xy['Y_avg'].tolist()
driver_numbers = fastest_minisector_xy['Fastest_driver_int'].values.astype(int)



#for i in range(len(driver_numbers)):
#    plt.text(x_coords[i], y_coords[i], str(driver_numbers[i]),
#         fontsize=5)


# My attempt to make the labelling on or off
def minisector_labels(x_coords, y_coords, driver_numbers):
    for i in range(len(driver_numbers)):
        plt.text(x_coords[i], y_coords[i], str(driver_numbers[i]),
         fontsize=10)


# Call the labelling function        
# Hash out the following line to remove labels
minisector_labels(x_coords, y_coords, driver_numbers)

    


