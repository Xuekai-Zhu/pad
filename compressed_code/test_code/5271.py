def solution():
    
    program_size_in_MB = 360000
    download_speed = 50
    download_time_in_seconds = program_size_in_MB / download_speed
    download_time_in_hours = download_time_in_seconds / 3600
    result = download_time_in_hours
    return result

print(solution())