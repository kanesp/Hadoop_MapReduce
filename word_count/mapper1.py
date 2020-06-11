#!/usr/bin/env python3

import sys
import nltk 
from nltk.tokenize import word_tokenize
from string import punctuation

punct_list = list(punctuation) + ["\"", "'", "\\", "!", "(", ")", "+", "-", "=", "|", "{", "}", "[", "]", ";", ":", ",", ".", "<", ">", "/", "?", "@", "#", "$", "%", "^", "&", "*", "_", "~", "`", "``", "''", "--", "..."]

for line in sys.stdin:
	line  = line.strip()
	
	words = word_tokenize(line)

	words = [word.lower() for word in words]
	for word in words:
		if word not in punct_list:
			print(word, "\t1")
