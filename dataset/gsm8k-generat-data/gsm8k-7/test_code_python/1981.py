def solution():
    num_songs_morning = 10
    num_songs_afternoon = 15
    num_songs_night = 3
    size_per_song = 5  # in MB

    # Calculate the total number of songs Kira downloaded
    total_songs = num_songs_morning + num_songs_afternoon + num_songs_night

    # Calculate the total memory space needed for all the new songs
    total_memory_space = total_songs * size_per_song
    result = total_memory_space
    return result

print(solution())