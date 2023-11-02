def solution():
    """Mark does a gig every other day for 2 weeks. For each gig, he plays 3 songs. 2 of the songs are 5 minutes long and the last song is twice that long. How many minutes did he play?"""
    gigs_per_week = 3
    weeks = 2
    songs_per_gig = 3
    short_song_length = 5
    long_song_length = short_song_length * 2
    total_short_song_time = gigs_per_week * songs_per_gig * short_song_length * weeks
    total_long_song_time = gigs_per_week * songs_per_gig * long_song_length * weeks
    total_time = total_short_song_time + total_long_song_time
    result = total_time
    return result

print(solution())