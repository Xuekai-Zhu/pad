def solution():
    """The file, 90 megabytes in size, downloads at the rate of 5 megabytes per second for its first 60 megabytes, and then 10 megabytes per second thereafter. How long, in seconds, does it take to download entirely?"""
    # Define the size of the file in megabytes and the download rates
    file_size = 90
    rate_1 = 5
    rate_2 = 10

    # Calculate the time it takes to download the first 60 megabytes
    time_1 = 60 / rate_1

    # Calculate the remaining file size
    remaining_size = file_size - 60

    # Calculate the time it takes to download the remaining file size at the second rate
    time_2 = remaining_size / rate_2

    # Calculate the total download time
    total_time = time_1 + time_2

    # return the result
    result = total_time
    return result

print(solution())