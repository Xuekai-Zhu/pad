def solution():
    """Beyonce releases 5 different singles on iTunes. Then she releases 2 albums that each has 15 songs and 1 album that has 20 songs. How many songs has Beyonce released in total?"""
    total_singles = 5
    album_1_songs = 15
    album_2_songs = 15
    album_3_songs = 20
    total_album_songs = album_1_songs + album_2_songs + album_3_songs
    total_songs = total_singles + total_album_songs
    result = total_songs
    return result

print(solution())