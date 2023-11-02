def solution():
    # Define the total time spent on recording
    total_recording_time = 12 * 10

    # Define the total time spent on editing
    total_editing_time = 30

    # Define the total time spent on writing
    total_writing_time = 5 * 60 - total_recording_time - total_editing_time

    # Calculate the time spent on writing each song
    time_per_song = total_writing_time / 10
    result = time_per_song
    return result

print(solution())