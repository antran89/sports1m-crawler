# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:54:45 2016

@author: tranlaman
"""
import json
import matplotlib.pyplot as plt
import numpy as np

train_json_file = 'sports1m_train.json'
with open(train_json_file, "r") as fobj:
    train_data = json.load(fobj)
    
durations = []
for sample in train_data:
    dur = sample.get('duration')
    durations.append(dur)

test_json_file = 'sports1m_test.json'
with open(test_json_file, "r") as fobj:
    test_data = json.load(fobj)
    
test_durations = []
for sample in test_data:
    dur = sample.get('duration')
    durations.append(dur)
assert(len(durations) == len(train_data) + len(test_data))

# some statistics of 
print('total number of videos: %0.2f' % len(durations))
print('min, max duration: %0.2f, %0.2f' % (np.min(durations), np.max(durations)))
print('mean, median duration: %0.2f, %0.2f' % (np.mean(durations), np.median(durations))) 
print('5, 90 quantiles of duration: %0.2f, %0.2f' % (np.percentile(durations, 5), np.percentile(durations, 90)))

# draw histogram
nbins = 100
n, bins, patches = plt.hist(durations, nbins, normed=True, facecolor='green', alpha=0.75)
plt.ylabel('Frequency')
plt.xlabel('Duration in seconds')
plt.title('Sports1M video durations')
plt.show()
