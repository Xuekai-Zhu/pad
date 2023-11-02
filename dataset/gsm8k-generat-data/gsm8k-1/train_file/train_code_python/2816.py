def solution():
    """Elvis is releasing a new album with 10 songs, but he doesn't want to waste too much time on writing. He spends 5 hours in the studio, where he writes, records, and edits his songs. Each song takes 12 minutes to record, then it takes 30 minutes to edit all of his songs. How many minutes did it take Elvis to write each song, if each song took the same amount of time to write?"""
    total_time_in_minutes = (5 * 60) - 30
    number_of_songs = 10
    time_for_recording = number_of_songs * 12
    time_for_writing = total_time_in_minutes - time_for_recording
    time_per_song = time_for_writing / number_of_songs
    result = time_per_song
    return result

print(solution())