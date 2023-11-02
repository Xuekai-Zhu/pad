def solution():
    """Vicky has an excellent internet connection. She can download up to 50 MB/second. She has to download a new program to finish a college assignment. The program’s size is 360GB. If the internet connection is at maximum speed, how many hours does she have to wait until the program is fully downloaded? (There are 1000 MB per GB.)"""
    # Define the size of the program in MB
    program_size = 360000 # 360 GB * 1000 MB/GB

    # Define Vicky's download speed in MB/s
    download_speed = 50

    # Calculate the time needed to download the program in seconds
    download_time = program_size / download_speed

    # Convert download time from seconds to hours
    hours = download_time / 3600

    # Display the download time in hours
    result = hours
    return result

print(solution())