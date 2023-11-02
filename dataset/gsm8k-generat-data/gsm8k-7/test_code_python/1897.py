def solution():
    total_size = 880  # in MB
    downloaded_size = 310  # in MB
    download_speed = 5  # in MB/minute
    slow_download_speed = 3  # in MB/minute

    remaining_size = total_size - downloaded_size
    remaining_time = remaining_size / download_speed

    if remaining_time > 0:
        slow_download_time = remaining_size / slow_download_speed
        total_time = remaining_time + slow_download_time
    else:
        total_time = 0

    result = total_time
    return result

print(solution())