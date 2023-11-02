def solution():
    """Mason is trying to download a 880 MB game to his phone. After downloading 310 MB, his Internet connection slows to 3 MB/minute. How many more minutes will it take him to download the game?"""
    # Define the total size of the game and the amount downloaded so far
    total_size = 880
    downloaded_size = 310

    # Calculate the remaining size to download
    remaining_size = total_size - downloaded_size

    # Calculate the time it will take to download the remaining size with the slower connection
    download_time = remaining_size / 3

    result = download_time
    return result

print(solution())