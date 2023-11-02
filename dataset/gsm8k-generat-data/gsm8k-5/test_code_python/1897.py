def solution():
    total_size = 880  # The game's total size is 880 MB
    downloaded_size = 310  # So far, Mason has downloaded 310 MB
    remaining_size = total_size - downloaded_size  # Mason still needs to download the remaining size
    download_speed = 6  # Mason's download speed is initially 6 MB/minute
    slowed_speed = 3  # Mason's download speed slows to 3 MB/minute

    # Calculate the time it takes to download the remaining size at the initial speed
    initial_time = (remaining_size - slowed_speed) / download_speed
    # Calculate the time it takes to download the remaining size at the slowed speed
    slowed_time = slowed_speed / remaining_size

    # Add the times together to get the total time
    total_time = initial_time + slowed_time
    result = total_time
    return result

print(solution())