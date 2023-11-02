def solution():
    """Elvis is releasing a new album with 10 songs, but he doesn't want to waste too much time on writing. He spends 5 hours in the studio, where he writes, records, and edits his songs. Each song takes 12 minutes to record, then it takes 30 minutes to edit all of his songs. How many minutes did it take Elvis to write each song, if each song took the same amount of time to write?"""
    total_time_in_minutes = 5 * 60
    recording_time_per_song = 12
    editing_time = 30
    total_recording_time = recording_time_per_song * 10
    total_editing_time = editing_time * 10
    total_writing_time = total_time_in_minutes - total_recording_time - total_editing_time
    time_per_song = total_writing_time / 10
    result = time_per_song
    return result

print(solution())