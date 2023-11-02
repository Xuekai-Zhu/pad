def solution():
    """Mason is trying to download a 880 MB game to his phone. After downloading 310 MB, his Internet connection slows to 3 MB/minute. How many more minutes will it take him to download the game?"""
    game_size = 880
    downloaded = 310
    remaining = game_size - downloaded
    download_rate = 3 # MB/minute
    time_remaining = remaining / download_rate
    result = time_remaining
    return result

print(solution())