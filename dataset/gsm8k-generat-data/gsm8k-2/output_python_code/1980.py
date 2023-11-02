def solution():
    """Kira wants some new music on her phone. She downloads 10 songs in the morning. Later on that day, she finds 15 more songs she likes so she downloads them, and at night a friend of hers recommends 3 more songs she also downloads. Knowing that each song has a size of 5 MB, how much memory space in MB will the new songs occupy?"""
    morning_songs = 10
    later_songs = 15
    night_songs = 3
    song_size = 5
    total_songs = morning_songs + later_songs + night_songs
    total_size = total_songs * song_size
    result = total_size
    return result

print(solution())