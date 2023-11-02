def solution():
    """Mason is trying to download a 880 MB game to his phone. After downloading 310 MB, his Internet connection slows to 3 MB/minute. How many more minutes will it take him to download the game?"""
    # Define the total size of the game and the amount already downloaded
    game_size = 880
    downloaded = 310

    # Calculate the remaining size to download
    remaining_size = game_size - downloaded

    # Calculate the number of minutes it will take to download the remaining size
    download_speed = 3 # MB/minute
    download_time = remaining_size / download_speed

    # Display the download time in minutes
    result = download_time
    return result

print(solution())