import json
import googletrans
from googletrans import Translator
import random


with open('./song_lyrics.json',encoding='utf-8') as fp:
    data = json.load(fp)

new_data = data
translator = Translator()

artists = []
writers = []
musics = []

all_english = []

for song in data:
    #clean titles
    if(song['title_mix'] is None):
        if(song['title_sin'] is not None):
            song['title_mix'] = song['title_sin']
        else:
            song['title_mix'] = "unknown – නොදනී"
    
    title_mix = song['title_mix']
    title_mix = title_mix.replace(' | ',"")
    title_mix_split = title_mix.split('–')

    song['title_en'] = title_mix_split[0]

    if(song['title_sin'] is None):
        if(len(title_mix_split)>1):
            song['title_sin'] = title_mix_split[1]


    artist = song['artist']
    writer = song['writer']
    music = song['music']

    '''if artist not in artists:
        artists.append(artist)

    if writer not in writers:
        writers.append(writer)

    if music not in musics:
        musics.append(music)'''

    artist_l = artist.split(',')
    for artist in artist_l:
        artist = artist.strip()
        artist.lstrip()
        if artist not in all_english:
            all_english.append(artist)

    writer_l = writer.split(',')
    for writer in writer_l:
        writer = writer.strip()
        writer.lstrip()
        if writer not in all_english:
            all_english.append(writer)

    music_l = music.split(',')
    for music in music_l:
        writer = music.strip()
        music.lstrip()
        if music not in all_english:
            all_english.append(music)
    
    '''
    #artist
    artist = song['artist']
    artist_sin = translator.translate(artist, dest='sinhala').text
    song['artist_sin'] = artist_sin

    #writer
    writer = song['writer']
    writer_sin = translator.translate(writer, dest='sinhala').text
    song['writer_sin'] = writer_sin

    #music
    music = song['music']
    music_sin = translator.translate(music, dest='sinhala').text
    song['music_sin'] = music_sin

    #rating
    rating = (random.randint(10,20))
    song['rating'] = rating
    print(song['title_en'])'''

artitst_dict = {}

for key in all_english:
    artitst_dict[key] = translator.translate(key, dest='sinhala').text

print(artitst_dict)

with open('./artist_details.json', 'w', encoding='utf-8') as f:
    json.dump(artitst_dict, f, ensure_ascii=False, indent=2)

#with open('./song_lyrics_processed_2.json', 'w', encoding='utf-8') as f:
 #   json.dump(newData, f, ensure_ascii=False, indent=2)
