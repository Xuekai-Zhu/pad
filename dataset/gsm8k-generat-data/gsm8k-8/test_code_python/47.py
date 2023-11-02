def solution():
    # Define the size of the file and the download rates
    file_size = 90
    rate1 = 5
    rate2 = 10

    # Calculate how long it takes to download the first 60 MB
    time_first_60 = 60 / rate1

    # Calculate how long it takes to download the remaining 30 MB
    time_remaining = (file_size - 60) / rate2

    # Calculate the total time to download the entire file
    total_time = time_first_60 + time_remaining
    result = total_time
    return result

print(solution())