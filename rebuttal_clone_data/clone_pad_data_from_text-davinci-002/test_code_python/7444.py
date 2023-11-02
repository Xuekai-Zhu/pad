def solution():
    gigs_per_week = 2
    songs_per_gig = 3
    minutes_per_short_song = 5
    minutes_per_long_song = minutes_per_short_song * 2
    total_minutes = ((gigs_per_week * songs_per_gig) - 1) * minutes_per_short_song + minutes_per_long_song
    result = total_minutes
    return result

print(solution())