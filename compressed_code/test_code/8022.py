def solution():
    
    total_time_in_minutes = (5 * 60) - 30
    number_of_songs = 10
    time_for_recording = number_of_songs * 12
    time_for_writing = total_time_in_minutes - time_for_recording
    time_per_song = time_for_writing / number_of_songs
    result = time_per_song
    return result

print(solution())