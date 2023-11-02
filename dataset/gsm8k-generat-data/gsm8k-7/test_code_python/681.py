def solution():
    num_audiobooks = 6
    audiobook_length = 30  # in hours
    daily_listening_time = 2  # in hours

    # Calculate the total time it takes to finish one audiobook
    total_audiobook_time = audiobook_length * 1

    # Calculate the total time it takes to finish all audiobooks
    total_time = num_audiobooks * total_audiobook_time

    # Calculate the number of days it takes to finish all audiobooks
    num_days = total_time / daily_listening_time
    result = num_days
    return result

print(solution())