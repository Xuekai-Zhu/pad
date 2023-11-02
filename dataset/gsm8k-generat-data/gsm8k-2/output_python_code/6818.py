def solution():
    """Vicky has an excellent internet connection. She can download up to 50 MB/second. She has to download a new program to finish a college assignment. The program’s size is 360GB. If the internet connection is at maximum speed, how many hours does she have to wait until the program is fully downloaded? (There are 1000 MB per GB.)"""
    program_size_in_MB = 360000
    download_speed = 50
    download_time_in_seconds = program_size_in_MB / download_speed
    download_time_in_hours = download_time_in_seconds / 3600
    result = download_time_in_hours
    return result

print(solution())