#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys

test=pd.read_csv('Test.csv')
train=pd.read_csv(sys.stdin)

x_train=train.iloc[:,0:48]
x_train=(x_train-np.min(x_train))/(np.max(x_train)-np.min(x_train)).values
test=(test-np.min(test))/(np.max(test)-np.min(test)).values
#print(x_train)
labels=train.iloc[:,-1]

labels=np.array(labels)
x_train=np.array(x_train)
test1=np.array(test)

sorted_index=[]

def eucdist(a,b):
	return np.linalg.norm(a-b)
for i in range(0,len(test1)):
	dist=[]
	labels_new=[]
	for j in range(0,len(x_train)):
		dist.append(eucdist(test1[i],x_train[j]))
	np.argsort(dist)
	sorted_index=(np.argsort(dist))
	for k in sorted_index:
		labels_new.append(labels[k])
	test1_n=test1[i].tolist()
	print(test1_n,'\t',labels_new)

