def solution():
    """Mark does a gig every other day for 2 weeks. For each gig, he plays 3 songs. 2 of the songs are 5 minutes long and the last song is twice that long. How many minutes did he play?"""
    num_gigs = 7 * 2
    num_songs_per_gig = 3
    short_song_length = 5
    long_song_length = 2 * short_song_length
    total_minutes_played = num_gigs * num_songs_per_gig * (2 * short_song_length + long_song_length)
    result = total_minutes_played
    return result

print(solution())