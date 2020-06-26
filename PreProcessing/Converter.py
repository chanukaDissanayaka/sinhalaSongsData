import json

with open('./output_songbook.json') as fp:
    data = json.load(fp)

with open('./song_lyrics.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)


with open('./song_lyrics_indent.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

