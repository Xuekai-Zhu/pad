def solution():
    num_songs = 10
    record_time_per_song = 12
    editing_time = 30
    studio_time = 5 * 60  # convert to minutes

    # Calculate the total time spent on recording all songs
    total_recording_time = num_songs * record_time_per_song

    # Calculate the total time spent on the whole process of writing a song
    song_writing_time = (studio_time - editing_time) / num_songs - record_time_per_song

    result = song_writing_time
    return result

print(solution())