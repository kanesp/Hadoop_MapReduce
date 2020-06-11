#!/usr/bin/env python3
import sys

wordcount = {}

for line in sys.stdin:
	line = line.strip()
	word, count = line.split("\t", 1)
	try:
		count = int(count)
	except ValueError:
		continue

	try:
		wordcount[word] = wordcount[word] + count
	except:
		wordcount[word] = count

sorted_val = sorted(wordcount.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

top10Freq = sorted_val[:10]
for i in top10Freq:
	print(i[0], "\t", i[1])
