#!/usr/bin/env python3

import sys,re
index={}

for line in sys.stdin:
	word,filenameList=line.split('\t')
	index.setdefault(word,{})
	
	for filename in filenameList.split(','):
		filename=filename.strip('\n')
		index[word].setdefault(filename,0)
		
for word in index:
	postings_list=[filename for filename in index[word]]
	
	postings=','.join(postings_list)
	
	print(word,':',postings)
