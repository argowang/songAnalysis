# -*- coding:utf-8 -*-

# web scraping to obtain the lyircs from music.163.com
import requests
import json
import re
from bs4 import BeautifulSoup


SINGER_ID_LIST = ['1008034', '1197115','12493701', '12127564', '1204010', '1038099', '12021086', '784257', '1211046']

ARTIST_ENDPOINT = 'http://music.163.com/#/artist?id='
LYRICS_ENDPOINT = 'http://music.163.com/api/song/lyric?id=%s&lv=1&kv=1&tv=-1'
SONG_LIST_OUTPUT_DIR = '/home/mrdoggie/songAnalysis/data/scrappedSongList.txt'
LYRICS_OUTPUT_DIR = '/home/mrdoggie/songAnalysis/data/scrappedLyrics.txt'

def processSingleSinger(singerID):
    music_name_set, music_id_set = fetchSongIDListGivenSingleSingerID(singerID)
    for musicName in music_name_set:
        processSingleMusicName(musicName)
    for musicID in music_id_set:
        recordLyricsGivenSingleMusicID(musicID)

def processSingleMusicName(musicName):
    for each in music_name_set:
        f = open(SONG_LIST_OUTPUT_DIR,"ab")
        try:
            f.write(singer_name.encode('utf-8') + each.encode('utf-8')  + '\n') #one song name each line
            f.close
        except AttributeError as e2:
            pass

def recordLyricsGivenSingleMusicID(musicID):
    lrc_url = LYRICS_ENDPOINT % musicID
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
        # Reformat the lyrics. Get ready for later transcription. Notice: this will mess up the looking in texteditor
    all_lyrics = re.sub(r' ','\n',lrc) #convert all whitespace to newline to unify the format
    all_lyrics = re.sub(r'\n+', '\n', all_lyrics) #remove duplicated newline
    f = open(LYRICS_OUTPUT_DIR, "ab")
    try:
    	f.write(all_lyrics.encode('utf-8'))
    	f.close
    except AttributeError as e2:
    	pass

def fetchSongIDListGivenSingleSingerID(singerID):
    singer_url = ARTIST_ENDPOINT + str(singerID)
    web_data = requests.get(singer_url)
    print(web_data.text)
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
    return music_name_set, music_id_set

def main():
    for singerID in SINGER_ID_LIST:
        processSingleSinger(singerID)

if __name__ == "__main__":
    main()
