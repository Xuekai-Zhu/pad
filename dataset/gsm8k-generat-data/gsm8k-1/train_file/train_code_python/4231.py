def solution():
    """Beyonce releases 5 different singles on iTunes. Then she releases 2 albums that each has 15 songs and 1 album that has 20 songs. How many songs has Beyonce released in total?"""
    num_singles = 5
    num_albums = 3
    songs_per_album_1 = 15
    songs_per_album_2 = 15
    songs_per_album_3 = 20
    total_songs = num_singles + (num_albums * (songs_per_album_1 + songs_per_album_2 + songs_per_album_3))
    result = total_songs
    return result

print(solution())