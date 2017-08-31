#!/usr/bin/python
#coding = utf-8
# -*- coding: utf-8 -*-
import sys
import thulac
from pyecharts import WordCloud


#input the tuple type, and return specific type of words
#the type should be a string with the corresponding meaning
#common type n:noun np:name ns:location  ni:institution 
#nz:professional word a:adj d:adv v:verb
def filtType (wordList, type):
	filtedList = []
	for ele in wordList:
		if ele[1] == type:
			filtedList.append(ele[0])
	return filtedList

#normalize parsed data into an array of words regardless of its type
def cleanup (wordList):
	cleanList = []
	for ele in wordList:
		cleanList.append(ele[0])
	return cleanList

#helper function for groupAndCount
def findAndReturnIndex(e, l):
	range_list = range(len(l))
	if range_list == []:
		return -1
	else:
		for index in range_list:
			if l[index] == e:
				return index
		return -1


def groupAndCount(wordList, nonDupList, counterList):
	for word in wordList:
		index_returned = findAndReturnIndex(word, nonDupList)
		if index_returned == -1 :
			#not found in the nonDupList, update the list and the counter
			nonDupList.append(word)
			counterList.append(1)
		else:
			#found it in the nonDupList, update the number 
			counterList[index_returned] = counterList[index_returned] + 1


# load input
f=file('/Users/mrdoggie/Desktop/Project/hipHopAnalysis/scrappedLyrics.txt')
raw = f.read()
f.close()


######## NO TYPE is Considered###########
# initiate parser, no type is considered 
# thul = thulac.thulac(T2S=True, filt=True)
# parsed = thul.cut(raw, text=False)
# cleaned_parsed = cleanup(parsed)
# nonDupList = []
# counterList = []
# analysis = groupAndCount(cleaned_parsed, nonDupList, counterList)

# ######### Consider One Type ###############
thul = thulac.thulac(T2S=True, filt=True)
parsed = thul.cut(raw, text=False)
filted_parsed = filtType(parsed, 'n')
nonDupList = []
counterList = []
analysis = groupAndCount(filted_parsed, nonDupList, counterList)

#combine the word with corresponding frequency
frequency_dict = dict(zip(nonDupList, counterList))

#Remove unwanted word in the dictionary
bad_words = ['I', 'me', 'you', 'u', '', 'it', 'my', 'the', 'a', 'to', '\'', 'know', 'i', 'up', 'so', 'm', 'J', 'are', 'do', 'be', 'busy', 's', 
'can', 'Tizzy', 'don', 'if', 'say', 'just', 'wanna', 'fuckin']
for word in bad_words:
	try:
		del frequency_dict[word]
	except:
		pass


#sort according to frequency
sorted_f_dict = sorted(frequency_dict.items(), lambda x, y: cmp(x[1],y[1]), reverse=True)

sorted_word = []
sorted_f =[]
for ele in sorted_f_dict:
	sorted_word.append(ele[0])
	sorted_f.append(ele[1])



#Visualize the output using wordcloud
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", sorted_word[0:100], sorted_f[0:100], word_size_range=[10, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render(r"/Users/mrdoggie/Desktop/Project/hipHopAnalysis/hiphopAnalysis.html")

output = open('/Users/mrdoggie/Desktop/Project/hipHopAnalysis/output.txt','w')
for ele in sorted_f_dict:
	print >> output, ele[0],
	print >> output, ele[1]
output.close()
	