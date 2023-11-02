def solution():
    """The file, 90 megabytes in size, downloads at the rate of 5 megabytes per second for its first 60 megabytes, and then 10 megabytes per second thereafter. How long, in seconds, does it take to download entirely?"""
    # Define the size of the file and the download rates
    FILE_SIZE = 90
    RATE_1 = 5
    RATE_2 = 10

    # Calculate the time to download the first 60 megabytes
    time_1 = 60 / RATE_1

    # Calculate the remaining size of the file
    remaining_size = FILE_SIZE - 60

    # Calculate the time to download the remaining size of the file
    time_2 = remaining_size / RATE_2

    # Calculate the total time to download the file
    total_time = time_1 + time_2

    # return the result
    result = total_time
    return result

print(solution())