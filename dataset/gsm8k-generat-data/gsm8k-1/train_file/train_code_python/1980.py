def solution():
    """Kira wants some new music on her phone. She downloads 10 songs in the morning. Later on that day, she finds 15 more songs she likes so she downloads them, and at night a friend of hers recommends 3 more songs she also downloads. Knowing that each song has a size of 5 MB, how much memory space in MB will the new songs occupy?"""
    songs_in_morning = 10
    songs_in_day = 15
    songs_at_night = 3
    song_size = 5 # in MB
    total_songs = songs_in_morning + songs_in_day + songs_at_night
    total_size = total_songs * song_size
    result = total_size
    return result

print(solution())