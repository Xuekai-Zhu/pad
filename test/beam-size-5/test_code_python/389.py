def solution():
    
    # Define the time spent writing the song
    writing_time = 4

    # Define the time spent recording the song
    recording_time = writing_time / 2

    # Define the time spent editing the song
    editing_time = 90

    # Calculate the total work time
    total_time = writing_time + recording_time + editing_time

    # Calculate the percentage of the total work time spent editing
    percentage_editing = (editing_time / total_time) * 100

    # return the result
    result = percentage_editing
    return result

print(solution())