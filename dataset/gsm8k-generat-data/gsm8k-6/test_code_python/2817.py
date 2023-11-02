def solution():
    # Calculate the total time for recording all songs
    recording_time = 12 * 10  # each song takes 12 minutes to record

    # Calculate the total time for editing all songs
    editing_time = 30  

    # Calculate the total time spent on writing
    writing_time = (5 * 60) - recording_time - editing_time  # 5 hours in the studio, subtract time for recording and editing

    # Calculate the time to write one song
    time_per_song = writing_time / 10  

    result = time_per_song
    return result

print(solution())