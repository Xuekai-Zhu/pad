def solution():
    concert_length = 80 # in minutes
    intermission_length = 10 # in minutes
    song_length = 5 # in minutes
    long_song_length = 10 # in minutes

    # Calculate the actual length of the concert without intermission
    actual_concert_length = concert_length - intermission_length

    # Calculate the total time spent on all of the regular length songs
    regular_songs_time = (actual_concert_length - long_song_length) / song_length

    # Calculate the total number of regular length songs
    regular_songs = int(regular_songs_time)

    # Add one for the long song
    total_songs = regular_songs + 1
    result = total_songs
    return result

print(solution())