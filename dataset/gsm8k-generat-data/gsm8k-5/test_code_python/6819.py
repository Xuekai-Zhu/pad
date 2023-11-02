def solution():
    internet_speed = 50  # Vicky can download up to 50 MB/second
    program_size = 360 * 1000  # The program's size is 360GB, which equals 360,000 MB

    # Calculate the time it takes to download the program
    download_time = program_size / internet_speed

    # Convert the download time from seconds to hours
    download_time_hours = download_time / 3600

    result = download_time_hours
    return result

print(solution())