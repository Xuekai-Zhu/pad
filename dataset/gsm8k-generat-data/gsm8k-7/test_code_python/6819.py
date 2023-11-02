def solution():
    max_speed = 50 # in MB/s
    program_size = 360 * 1000 # in MB
    download_time = program_size / max_speed # in seconds
    download_time_hours = download_time / 3600 # in hours
    result = download_time_hours
    return result

print(solution())