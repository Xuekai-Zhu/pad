def solution():
    """The number of songs in a playlist is 300. If John has 20 such playlists, and each song is 10 hours long, how many hours will the 20 playlists last in total?"""
    songs_per_playlist = 300
    playlists = 20
    song_length_hours = 10
    total_hours = songs_per_playlist * playlists * song_length_hours
    result = total_hours
    return result

print(solution())