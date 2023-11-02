def solution():
    """Elvis is releasing a new album with 10 songs, but he doesn't want to waste too much time on writing. He spends 5 hours in the studio, where he writes, records, and edits his songs. Each song takes 12 minutes to record, then it takes 30 minutes to edit all of his songs.   How many minutes did it take Elvis to write each song, if each song took the same amount of time to write?"""
    # Calculate the total time spent recording all 10 songs
    recording_time = 12 * 10  # 12 minutes per song * 10 songs

    # Calculate the total time spent editing all 10 songs
    editing_time = 30

    # Calculate the total time spent on writing
    writing_time = (5 * 60) - recording_time - editing_time  # Convert 5 hours to minutes

    # Calculate the time spent on writing each song
    time_per_song = writing_time / 10

    # Display the time spent on writing each song
    result = time_per_song
    return result

print(solution())