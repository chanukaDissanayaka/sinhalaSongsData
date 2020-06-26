import json
import googletrans
from googletrans import Translator
import random


with open('./song_lyrics_processed.json',encoding='utf-8') as fp:
    data = json.load(fp)


for song in data:

    song['title_en']

    if(song['title_sin'] is None):
        mix_t = song['title_en'].split('-')
        song['title_sin'] = mix_t[1]

    song.pop('title_mix')

with open('./song_lyrics_processed_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
