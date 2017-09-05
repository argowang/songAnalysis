#!/usr/bin/python
#coding = utf-8
# -*- coding: utf-8 -*-
from pypinyin import pinyin, lazy_pinyin
import pypinyin
import re
import collections
from pyecharts import Bar

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
		each = pinyin[0].encode('utf-8')
		rhymeList.append(each) #rhymeList will be used for rhyme generation later
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

# find out the rhymes
filteredRhymePair = []
for each in rhymePair:
	if ('ang' in each[0] or 'iang' in each[0] or 'uang' in each[0]):
		if ('ang' in each[1] or 'iang' in each[1] or 'uang' in each[1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('eng' in each[0] or 'ing' in each[0] or 'ueng' in each[0] or 'ong' in each[0] or 'iong' in each[0]):
		if ('eng' in each[1] or 'ing' in each[1] or 'ueng' in each[1] or 'ong' in each[1] or 'iong' in each[1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('en' in each[0] or 'in' in each[0] or 'un' in each[0]):
		if (('en' in each[1] or 'in' in each[1] or 'un' in each[1]) and 'ng' not in each [1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('an' in each[0] or 'ian' in each[0] or 'uan' in each[0]):
		if (('an' in each[1] or 'ian' in each[1] or 'uan' in each[1]) and 'ang' not in each [1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('ou' in each[0] or 'iu' in each[0]):
		if ('ou' in each[1] or 'iu' in each[1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('ao' in each[0] or 'iao' in each[0]):
		if ('ao' in each[1] or 'iao' in each[1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('ei' in each[0] or 'ui' in each[0]):
		if ('ei' in each[1] or 'ui' in each[1] ):
			filteredRhymePair.append(each)
			continue
		continue
	if ('ai' in each[0] or 'uai' in each[0]):
		if ('ai' in each[1] or 'uai' in each[1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('ie' in each[0] or 'ue' in each[0]):
		if (('ie' in each[1] or 'ue' in each[1]) and 'ueng' not in each [1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('e' in each[0] or 'o' in each[0] or'uo' in each[0]):
		if (('e' in each[1] or 'o' in each[1] or 'uo' in each[1]) and 'ie' not in each [1]
			and 'ue' not in each[1] and 'er' not in each [1] and 'ng' not in each[1]
			and 'ou' not in each[1] and 'en' not in each [1] and 'ao' not in each[1]):
			filteredRhymePair.append(each)
			continue		
		continue
	if ('a' in each[0] or 'ua' in each[0] or 'ia' in each[0]):
		if (('a' in each[1] or 'ua' in each[1] or 'ia' in each[0]) and 'ai' not in each [1]
			and 'ao' not in each [1] and 'an' not in each [1] ):
			filteredRhymePair.append(each)
			continue
		continue
	if ('u' in each[0]):
		if ('u' in each[1] and 'ua' not in each[1] and 'uo' not in each [1] and 'uai' not in each [1] and 'ui' not in each [1]
			and 'iu' not in each [1] and 'uan' not in each [1] and 'un' not in each [1] and 'ueng' not in each [1]):
			filteredRhymePair.append(each)
			continue
		continue
	if ('i' in each[0] or 'er' in each[0]):
		if (('i' in each[1] or 'er' in each[1]) and 'ia' not in each [1] and 'ie' not in each [1] and 'ai' not in each [1] 
			and 'ei' not in each [1] and 'ui' not in each [1] and 'iu' not in each [1] and 'in' not in each [1] 
			and 'iong' not in each [1]):
			filteredRhymePair.append(each)
			continue	
		continue

f = open("C:/github/songAnalysis/filteredRhymePair.txt", "ab")
for each in filteredRhymePair:
	f.write(each[0] + ' ' + each[1] + '\n')
f.close


#leave rhyme only
rhymeOnly = []
for each in filteredRhymePair:
	each[0] = re.sub(r'^[bcdfhjklmnpqstwxyz]+','',each[0])
	each[0] = re.sub(r'^g', '', each[0])
	each[0] = re.sub(r'^r', '', each[0])
	each[1] = re.sub(r'^[bcdfhjklmnpqstwxyz]+','',each[1])
	each[1] = re.sub(r'^g', '', each[1])
	each[1] = re.sub(r'^r', '', each[1])
	rhymeOnly.append(each[0]+ ', ' + each[1])

f = open("C:/github/songAnalysis/RhymeOnly.txt", "ab")
for each in filteredRhymePair:
	f.write(each[0] + ' ' + each[1] + '\n')
f.close

rhymeFrequency = collections.Counter(rhymeOnly)
top100 = rhymeFrequency.most_common(100)
sorted_f_dict = sorted(rhymeFrequency.items(), lambda x, y: cmp(x[1],y[1]), reverse=True)

sorted_keys = []
sorted_values = []
f = open("C:/github/songAnalysis/RhymeFrequency.txt", "ab")
for each in sorted_f_dict:
	sorted_keys.append(each[0])
	sorted_values.append(each[1])
	f.write(each[0] + ': ' + str(each[1]) + '\n')	
f.close

attr = sorted_keys[0:99]
v1 = sorted_values[0:99]
bar = Bar("Chinese Hip-hop Music Rhyme Pair Frequency")
bar.add("", attr, v1, is_datazoom_show=True, is_label_show = True)
bar.render(r"C:/github/songAnalysis/Output/rhymeFrequency.html") 