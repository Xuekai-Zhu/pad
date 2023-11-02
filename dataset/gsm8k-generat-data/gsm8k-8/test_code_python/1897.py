def solution():
    # Define the total size of the game and the amount downloaded
    total_size = 880
    downloaded = 310

    # Calculate the remaining size to download
    remaining_size = total_size - downloaded

    # Calculate the remaining time to download at a speed of 3 MB/minute
    remaining_time = remaining_size / 3

    result = remaining_time
    return result

print(solution())