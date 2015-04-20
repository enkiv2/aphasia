#!/usr/bin/env python

import json, sys

from random import Random
random=Random()

with open("ea-thesaurus.json") as t:
	thesaurus=json.loads("\n".join(t.readlines()))
	for line in sys.stdin.readlines():
		out=""
		for word in line.split():
			if(word.upper() in thesaurus):
				translation=[]
				for i in thesaurus[word.upper()]:
					for j in i.keys():
						for k in range(0, int(i[j])):
							translation.append(j)
				out+=" "+str(random.choice(translation))
			else:
				out+=" "+word
		print(out)

