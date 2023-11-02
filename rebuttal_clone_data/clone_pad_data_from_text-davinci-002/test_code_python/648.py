def solution():
    total_songs = 30
    songs_played_1 = 5
    songs_played_2 = 7
    songs_ played_3 = (total_songs - songs_played_1 - songs_played_2) / 2
    songs_played_4 = (total_songs - songs_played_1 - songs_played_2 - songs_played_3)
    result = (songs_played_3 + songs_played_4) / 2
    return result

print(solution())