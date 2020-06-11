#!/usr/bin/env python3

import sys
import numpy as np
N=3
dict1={}
for line in sys.stdin:
	line=line.strip()
	test,labels=line.split('\t')	
	labels=labels.strip(']')
	labels=labels.replace('[','')
	dict1[test]=labels

for k,v in dict1.items():
	cnt=[]
	v=v.split(',')
	for i in v[0:N]:
		cnt.append(int(i))
	max_cnt=np.bincount(cnt)	
	print(k,np.argmax(max_cnt))

		
	
	

