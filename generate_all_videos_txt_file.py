# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:18:03 2016

@author: tranlaman

Generate all_vid.txt file for Sports1M dataset.
Eliminating some videos having durations larger than 95% quantiles (643s)
90% quantiles (526s)
85% quantiles (416s)
80% quantiles (338s)
"""
import json

duration_threshold = 643 # maximum duration allowed

all_vid_fid = open('all_vid.txt', 'w')

test_json_file = 'sports1m_test.json'
with open(test_json_file, "r") as fobj:
    test_data = json.load(fobj)

test_fid = open('test_vid.txt', 'w')
for sample in test_data:
    dur = sample.get('duration')
    if dur == 0:
        continue
    if dur >= duration_threshold:
        continue
    youtube_url = sample.get('id')
    labels = sample.get('label487')
    line = '%s %d' % (youtube_url, labels[0])
    for ind in xrange(1, len(labels)):
        line += ',%d' % labels[ind]
    # writing into file    
    test_fid.write('%s\n' % line)
    all_vid_fid.write('%s\n' % line)

test_fid.close()        

train_json_file = 'sports1m_train.json'
with open(train_json_file, "r") as fobj:
    train_data = json.load(fobj)

train_fid = open('train_vid.txt', 'w')
for sample in train_data:
    dur = sample.get('duration')
    if dur == 0:
        continue
    if dur >= duration_threshold:
        continue
    youtube_url = sample.get('id')
    labels = sample.get('label487')
    line = '%s %d' % (youtube_url, labels[0])
    for ind in xrange(1, len(labels)):
        line += ',%d' % labels[ind]
    # writing into file    
    train_fid.write('%s\n' % line)
    all_vid_fid.write('%s\n' % line)

train_fid.close()   
all_vid_fid.close()