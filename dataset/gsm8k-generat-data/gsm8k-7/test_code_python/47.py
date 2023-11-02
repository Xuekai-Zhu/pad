def solution():
    file_size = 90
    download_speed1 = 5
    download_speed2 = 10

    # Calculate the time it takes to download the first 60 megabytes
    time1 = 60 / download_speed1

    # Calculate the remaining file size
    remaining_file_size = file_size - 60

    # Calculate the time it takes to download the remaining file size
    time2 = remaining_file_size / download_speed2

    # Calculate the total time it takes to download the whole file
    total_time = time1 + time2
    result = total_time
    return result

print(solution())