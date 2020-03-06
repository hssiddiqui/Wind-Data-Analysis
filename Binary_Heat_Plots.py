'''
Author: Hasan Siddiqui

This code helps visualize when you have a period of wind below a certain threshold.
These periods can then be filtered as 1 day, 2 day, 3 day events etc.
'''

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

def filterdays(data):
    days=2
    start=-1
    counter=0
    for i, j in enumerate(data):
        if j == 0 and start == -1:
            start = i
        if j == 0 and start != -1:
            counter += 1
        elif j == 1 and start != -1:
            if counter < days*24:
                data[start:i] = 1
                start = -1
            if counter >= days*24:
                start = -1
            counter = 0
    return data

def binary_data_conv(input_data,threshold):
    #bdata=np.ones(len(input_data))
    bdata = np.ones(8784)
    input_data[-1]=1
    for i, x in enumerate(input_data):
        if x<=threshold:
            bdata[i]=0

    return filterdays(bdata)

def binary_data(data, yshift=0):
    return [yshift+1 if x in data else yshift for x in range(data[-1] + 1)]

def read_data(i=0):
    data = []

    with open('wind_study_ts_0304_modified.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            data.append(row[i])

    return data





data = []
empty=np.zeros(8784)
space=np.ones(8784)


index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
years=[0,8760,17544,26304,35064,43824,52608]

for n in range(50):
    data.append(empty)
for m in range(50):
    data.append(space)

for j in range(6):
    print("Analyzing Year : ", j+1)
    for i in index:
        input_data = []
        input_data = read_data(i)
        input_data.pop(0)
        input_data = [float(i) for i in input_data]

        heatmapdata = binary_data_conv(input_data[years[j]: years[j + 1]], 0.5)
        for l in range(20):
            data.append(heatmapdata)

        for m in range(20):
            data.append(space)

    for n in range(50):
        data.append(empty)
    for m in range(50):
        data.append(space)






#PLOT FUNCTIONS
fig, ax = plt.subplots()
#plt.figure(figsize=(10, 5))
# define the colors
cmap = mpl.colors.ListedColormap(['r', 'k'])

# create a normalize object the describes the limits of
# each color
bounds = [0., 0.5, 1.]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# plot it
ax.imshow(data, interpolation='none', cmap=cmap, norm=norm)
plt.show()