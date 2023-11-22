def solution():
    
    # Define the time spent writing the song
    writing_time = 4

    # Calculate the time spent recording the song
    recording_time = writing_time / 2

    # Define the time spent editing the song
    editing_time = 90

    # Calculate the total time spent editing
    total_time = writing_time + recording_time + editing_time

    # Calculate the percentage of total time spent editing
    editing_percentage = (editing_time / total_time) * 100

    # Display the percentage of total time spent editing
    result = editing_percentage
    return result

print(solution())