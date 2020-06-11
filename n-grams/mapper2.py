#!/usr/bin/env python3

import sys
import nltk 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

punctuations = '''!()+-=|{}[];:'"\,<>./?@#$%^&*_~`''' 

punct_list = ["\"", "'", "\\", "!", "(", ")", "+", "-", "=", "|", "{", "}", "[", "]", ";", ":", ",", ".", "<", ">", "/", "?", "@", "#", "$", "%", "^", "&", "*", "_", "~", "`", "``", "''", "--", "..."]

ps = PorterStemmer()

keywords = ["science", "sea", "fire"]
kw_stem = [ps.stem(x) for x in keywords]

def getNGrams(wordlist, n):
	ngrams = []
	for i in range(len(wordlist)-(n-1)):
		ngrams.append(wordlist[i:i+n])
	return ngrams

def checkSubStringKeyword(keywords, x):
	for i in keywords:
		if x.find(i) != -1:
			op = 1
		else:
			op = 0
	return op

for line in sys.stdin:
	line  = line.strip()
	words = word_tokenize(line)
	words = [word.lower() for word in words]
	
	ngramslist = getNGrams(words, 3)
	
	all_ng = []
	keyword_ng = []
	for each_ng in ngramslist:
		new_ng = []
		for x in each_ng:
			#if x in keywords or (checkSubStringKeyword(keywords, x) == 1):
			x1 = ps.stem(x)
			if x1 in kw_stem:
				new_ng.append("$")
			elif x1 not in punct_list:
				new_ng.append(x)
		if len(new_ng) == 3:
			x1 = "_".join(new_ng)
		all_ng.append(x1)
		if "$" in new_ng and len(new_ng) == 3:
			x2 = "_".join(new_ng)
			keyword_ng.append(x2)

	for ng in keyword_ng:
		print(ng, "\t1")
