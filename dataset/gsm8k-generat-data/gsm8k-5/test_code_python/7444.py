def solution():
    gigs_per_week = 3.5  # Mark does a gig every other day for 2 weeks, which is 14 days, so he does 7 gigs per week
    songs_per_gig = 3  # Mark plays 3 songs per gig
    short_song_duration = 5  # Mark plays 2 songs that are 5 minutes long
    long_song_duration = 2 * short_song_duration  # Mark plays 1 song that is twice as long as the other 2 songs

    # Calculate the total duration of Mark's gigs in minutes
    total_duration = gigs_per_week * songs_per_gig * (2 * short_song_duration + long_song_duration) * 2  # Mark does gigs for 2 weeks

    result = total_duration
    return result

print(solution())