def solution():
    # Calculate the time taken to download the first 60 megabytes
    time_60mb = 60 / 5   # downloads at 5 megabytes per second

    # Calculate the remaining size of the file to be downloaded
    remaining_size = 90 - 60   # the file is 90 megabytes in size

    # Calculate the time taken to download the remaining size
    time_remaining = remaining_size / 10   # downloads at 10 megabytes per second

    # Calculate the total time taken to download the entire file
    total_time = time_60mb + time_remaining
    result = total_time
    return result

print(solution())