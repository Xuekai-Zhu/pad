def solution():
    """Hansel has a created album on Spotify that contains 25 songs and each song is 3 minutes long. If she adds 10 more songs to the album with the same duration, how many minutes will it take her to finish all the songs in the album?"""
    song_length = 3
    num_songs = 25 + 10
    total_length = song_length * num_songs
    result = total_length
    return result

print(solution())