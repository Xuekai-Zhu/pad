def solution():
    """Vicky has an excellent internet connection. She can download up to 50 MB/second. She has to download a new program to finish a college assignment. The program’s size is 360GB. If the internet connection is at maximum speed, how many hours does she have to wait until the program is fully downloaded? (There are 1000 MB per GB.)"""
    internet_speed = 50 # MB/second
    program_size = 360 * 1000 # MB
    download_time = program_size / internet_speed # seconds
    download_time_hours = download_time / 3600 # hours
    result = download_time_hours
    return result

print(solution())