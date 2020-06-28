
import json
with open('./data/song_lyrics_processed_2.json', encoding='utf-8') as fp:
    data = json.load(fp)

with open('./data/visits.json', encoding='utf-8') as fp:
    newData = json.load(fp)

index = 0
for i in data:
    i['total_visits'] = newData[index]['total_visits']
    i.pop('rating')
    index = index+1
    print(i)

with open('./song_lyrics_processed_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)