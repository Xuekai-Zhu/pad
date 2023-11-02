def solution():
    num_songs = 25
    song_duration = 3
    num_new_songs = 10

    # Calculate the total number of songs after adding new songs
    total_songs = num_songs + num_new_songs

    # Calculate the total duration of all songs in minutes
    total_duration = total_songs * song_duration
    result = total_duration
    return result

print(solution())