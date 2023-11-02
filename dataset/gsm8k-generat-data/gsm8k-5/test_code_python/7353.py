def solution():
    concert_time = 80  # Jay attended a one hour 20 minutes concert
    intermission_time = 10  # There was a 10-minute intermission during the concert
    total_song_time = concert_time - intermission_time  # Total time allocated for singing
    long_song_time = 10  # One song was 10 minutes long
    short_song_time = 5  # All other songs were 5 minutes long

    # Calculate the number of short songs
    num_short_songs = (total_song_time - long_song_time) / short_song_time

    # Add the long song and the number of short songs to get the total number of songs
    total_songs = 1 + num_short_songs
    result = total_songs
    return result

print(solution())