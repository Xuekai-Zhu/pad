def solution():
    """Gabriel and Luri each own a portable media player that can store up to 100 songs. Gabriel has 20 songs on his player while Luri has 3 times as many songs. How many fewer songs can Luri add to his player than Gabriel can add to his?"""
    max_songs = 100
    gabriel_songs = 20
    luri_songs = 3 * gabriel_songs
    gabriel_space = max_songs - gabriel_songs
    luri_space = max_songs - luri_songs
    songs_diff = gabriel_space - luri_space
    result = songs_diff
    return result

print(solution())