def solution():
    file_size = 90  # The file is 90 megabytes in size
    initial_speed = 5  # The rate of download for the first 60 megabytes is 5 megabytes per second
    remaining_size = file_size - 60  # The remaining size to download after the initial 60 megabytes
    remaining_speed = 10  # The rate of download after the initial 60 megabytes is 10 megabytes per second

    # Calculate the time it takes to download the first 60 megabytes
    time_first_60 = 60 / initial_speed

    # Calculate the time it takes to download the remaining size
    time_remaining = remaining_size / remaining_speed

    # Calculate the total time it takes to download the entire file
    total_time = time_first_60 + time_remaining
    result = total_time
    return result

print(solution())