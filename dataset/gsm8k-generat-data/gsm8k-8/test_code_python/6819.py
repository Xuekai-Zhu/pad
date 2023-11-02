def solution():
    # Convert program size to MB
    program_size_mb = 360 * 1000

    # Calculate the download time in seconds
    download_time_seconds = program_size_mb / 50

    # Convert download time to hours
    download_time_hours = download_time_seconds / 3600
    result = download_time_hours
    return result

print(solution())