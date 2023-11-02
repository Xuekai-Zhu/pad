def solution():
    # Calculate the remaining data that needs to be downloaded
    remaining_data = 880 - 310  # game size is 880 MB, already downloaded 310 MB
    remaining_data_in_MB = remaining_data * 1024  # convert remaining data from MB to KB

    # Calculate the time remaining to download the game
    time_remaining_in_minutes = remaining_data_in_MB / (3 * 60)  # connection speed is 3 MB/minute

    result = time_remaining_in_minutes
    return result

print(solution())