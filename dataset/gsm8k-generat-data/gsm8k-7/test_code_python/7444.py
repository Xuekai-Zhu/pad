def solution():
    num_days = 14
    gigs_per_day = 1
    num_songs_per_gig = 3
    song1_length = 5
    song2_length = 5
    song3_length = 2 * song2_length

    # Calculate the total number of gigs Mark does in 2 weeks
    total_gigs = num_days * gigs_per_day

    # Calculate the total length of all songs Mark played
    total_song_length = total_gigs * num_songs_per_gig * (song1_length + song2_length + song3_length)

    # Convert the total song length to minutes
    total_minutes = total_song_length

    result = total_minutes
    return result

print(solution())