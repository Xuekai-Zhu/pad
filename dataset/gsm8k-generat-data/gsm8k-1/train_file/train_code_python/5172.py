def solution():
    """Bart makes a mixtape. The first side has 6 songs. The second side has 4 songs. Each song is 4 minutes. How long is the total tape?"""
    first_side_songs = 6
    second_side_songs = 4
    song_length = 4
    total_length = (first_side_songs + second_side_songs) * song_length
    result = total_length
    return result

print(solution())