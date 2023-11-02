def solution():
    concert_time = 80  # in minutes
    intermission_time = 10  # in minutes
    song_time = 5  # in minutes
    long_song_time = 10  # in minutes

    # Calculate the total time spent on songs
    total_song_time = concert_time - intermission_time
    total_song_time -= long_song_time  # subtract the time of the long song
    num_songs = total_song_time // song_time  # integer division discarding the remainder

    # Add one to include the long song
    num_songs += 1

    result = num_songs
    return result

print(solution())