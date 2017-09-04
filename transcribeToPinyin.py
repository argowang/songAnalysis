#!/usr/bin/python
#coding = utf-8
# -*- coding: utf-8 -*-
from pypinyin import pinyin, lazy_pinyin
import pypinyin
import re


f=file('C:/github/songAnalysis/scrappedLyrics.txt')
#change into the format that pypinyin can work on
raw = (f.read()).decode('utf-8')
f.close()

#pull out non-English word at the end of the line(The rhyme word)
pat = re.compile("([^0-9a-zA-Z])\n")
lineEnd = pat.findall(raw)

# print lineEnd

f = open("C:/github/songAnalysis/rhymeList.txt", "ab") #on windows
rhymeList = []
for each in lineEnd:
	#transcribe to pinyin, use ignore argument to remove Chinese punctuation
	#notice '-' and ':' still show up in the result, to be dealt with later
	pinyin = lazy_pinyin(each, errors='ignore')
	#encode to output
	try:
		rhymeList.append(pinyin[0].encode('utf-8'))
		f.write(each + '\n')
	except:
		pass
f.close

# group the rhymeList into rhymePair by pairing up two consecutive words
rhymePair = []
f = open("C:/github/songAnalysis/rhymePair.txt", "ab")
for index in (range(len(rhymeList) -1 )):
	rhymePair.append([rhymeList[index].encode('utf-8'), rhymeList[index+1].encode('utf-8')])
	f.write(rhymeList[index].encode('utf-8') + ' ' + rhymeList[index+1].encode('utf-8') + '\n')
f.close


