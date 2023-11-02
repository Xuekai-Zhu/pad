def solution():
    program_size = 360 * 1000  # converting GB to MB
    download_speed = 50  # MB per second
    total_download_time = program_size / download_speed  # in seconds
    total_download_time_hours = total_download_time / 3600  # converting seconds to hours
    result = total_download_time_hours
    return result

print(solution())