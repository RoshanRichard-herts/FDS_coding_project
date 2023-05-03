#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:36:45 2023

@author: roshanrichard
"""

import numpy as np 
import matplotlib.pyplot as plt

# reading the csv file into an array
data_array = np.genfromtxt('data3.csv', delimiter=',')

# creating another array, representing the distribution of newborn weights in a given dataset
count, bins = np.histogram(data_array, bins=30, range=(2.1, 4.5))
print("The counts are ", count.size)
print("Bin range are ", bins.size)

# bincenter rounds bins which is 41 into 40
#binwidth stores the differcence value between the values stored in bin 
bincenter = 0.5 * (bins[1:] + bins[:-1])
binwidth = bins[1:] - bins[:-1]

counts_norm = count / np.sum(count)

#normalising the counts before plotting the histogram
print("bincenter is ", bincenter.size)
print("Normalised count is ",counts_norm.size)

cum_sum = np.cumsum(counts_norm)
print("The cummulative sum is :", cum_sum)

# calculating the average weight of newborn babies in the given region
W = np.mean(bincenter)

# calculating the average weight of babies between W and W * .085
X = data_array[(data_array < W) & (data_array > W*0.85)] 
X = np.mean(X)


print("Mean value is: ", W)
print("X value is: ", X)

plt.figure(figsize = (6, 4))
plt.style.use("ggplot")
plt.gca().set_facecolor('lightgrey')

#distribution
plt.bar(bincenter, counts_norm, width = 0.88 * binwidth, color = "green", label = "New born babies distribution")
plt.axvline(x=W, color='r', linestyle='--', label=f'W value ({W.round(2)})')
plt.axvline(x=X, color='black', linestyle='--', label=f'X value ({X.round(2)})')

plt.title("Distribution of new born babies in certain regions of Europe", fontsize = 10)
plt.xlabel("Weights of newborn babies (Distribution)", fontsize = 10)
plt.ylabel("Normalised Counts", fontsize = 10)
plt.xlim(2.0, 5.0, 0.5)
plt.ylim(0.00, 0.09, 0.01)
leg = plt.legend(bbox_to_anchor = (1.01, 0.99), fontsize = 10)
leg.get_frame().set_facecolor('w')
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
plt.show()

print('The minimum value of the dataset is ' + str(np.min(data_array)))
print('The maximum value of the dataset is ' + str(np.max(data_array)))


