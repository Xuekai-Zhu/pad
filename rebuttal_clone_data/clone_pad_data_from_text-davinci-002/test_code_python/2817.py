def solution():
    total_hours = 5
    total_minutes = total_hours * 60
    song_recording_time = 10 * 12
    song_editing_time = 10 * 30
    total_time = song_recording_time + song_editing_time
    song_writing_time = total_minutes - total_time
    result = song_writing_time / 10
    return result

print(solution())