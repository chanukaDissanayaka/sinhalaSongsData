import json

with open('./data/song_lyrics_processed_3.json', encoding='utf-8') as fp:
    data = json.load(fp)

with open('./data/artist_details_edited.json', encoding='utf-8') as fp:
    artis_data = json.load(fp)


for song in data:
    # artist
    artists_txt = song['artist']
    artists = artists_txt.split(',')

    artist_sin = []

    for artist in artists:
        artist_striped = artist.strip()
        if (artist_striped in artis_data.keys()):
            artist_sin.append(artis_data[artist_striped])

    artist_s = ", ".join(artist_sin)
    song['artist_sin'] = artist_s
    #print(song['artist_sin'], song['artist'])

    # writer
    artists_txt = song['writer']
    artists = artists_txt.split(',')

    artist_sin = []

    for artist in artists:
        artist_striped = artist.strip()
        if (artist_striped in artis_data.keys()):
            artist_sin.append(artis_data[artist_striped])

    artist_s = ", ".join(artist_sin)
    song['writer_sin'] = artist_s
    #print(song['writer_sin'], song['writer'])

    # music
    artists_txt = song['music']
    artists = artists_txt.split(',')

    artist_sin = []

    for artist in artists:
        artist_striped = artist.strip()
        if (artist_striped in artis_data.keys()):
            artist_sin.append(artis_data[artist_striped])

    artist_s = ", ".join(artist_sin)
    song['music_sin'] = artist_s
    #print(song['music_sin'], song['music'])

with open('./song_lyrics_final.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
