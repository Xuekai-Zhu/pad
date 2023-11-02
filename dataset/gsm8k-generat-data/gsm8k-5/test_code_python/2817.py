def solution():
    total_recording_time = 10 * 12  # Each song takes 12 minutes to record
    total_editing_time = 30  # It takes 30 minutes to edit all of the songs
    total_time_spent = (5 * 60) + total_recording_time + total_editing_time  # Convert hours to minutes

    # Calculate the time it takes to write each song
    time_per_song = (total_time_spent - total_recording_time - total_editing_time) / 10

    result = time_per_song
    return result

print(solution())