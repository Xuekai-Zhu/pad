def solution():
    """John buys a cassette with 2 songs. The first song is 5 minutes and the second song is 60% longer. How much time was the total cassette?"""
    first_song_length = 5
    second_song_length = first_song_length * 1.6
    total_length = first_song_length + second_song_length
    result = total_length
    return result

print(solution())