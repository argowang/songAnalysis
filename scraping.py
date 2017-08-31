# -*- coding:utf-8 -*-

# web scraping to obtain the lyircs from music.163.com
import requests
import json
import re
from bs4 import BeautifulSoup


singer_id_list = ['1008034', '1197115','12493701', '12127564', '1204010', '1038099', '12021086', '784257', '1211046']

for id in singer_id_list:
	singer_url = 'http://music.163.com/artist?id=' + str(id)
	web_data = requests.get(singer_url)
	soup = BeautifulSoup(web_data.text, 'lxml')
	singer_name = soup.select("#artist-name")
	singer_name = singer_name[0].get('title')
	r = soup.find('ul', {'class': 'f-hide'}).find_all('a')
	r = (list(r))
	music_name_set=[]
	music_id_set=[]


	# get the list of song id from a webpage
	for each in r:
		song_name = each.text
		music_name_set.append(song_name)
		# print(each.text)
		song_id = each.attrs["href"]
		music_id_set.append(song_id[9:])

	# record the name of the songs analyzed

	for each in music_name_set:
		f = open("/Users/mrdoggie/Desktop/Project/hipHopAnalysis/scrappedSongList.txt", "ab")
		try:
			f.write(singer_name.encode('utf-8') + each.encode('utf-8')  + '\n') #one song name each line
			f.close
		except AttributeError as e2:
			pass

	# record the lyrics
	for each in music_id_set:
		lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(each) + '&lv=1&kv=1&tv=-1'
		lyric = requests.get(lrc_url)
		json_obj = lyric.text
		j = json.loads(json_obj)
		try: #some song may not have lyrics
			lrc=j['lrc']['lyric']
			pat=re.compile(r'\[.*\]')
			lrc=re.sub(pat,"",lrc)
			lrc=lrc.strip()
		except KeyError as e:
			pass
		all_lyrics = lrc
		f = open("/Users/mrdoggie/Desktop/Project/hipHopAnalysis/scrappedLyrics.txt", "ab")
		try:
			f.write(all_lyrics.encode('utf-8'))
			f.close
		except AttributeError as e2:
			pass
