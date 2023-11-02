def solution():
    """Mason is trying to download a 880 MB game to his phone. After downloading 310 MB, his Internet connection slows to 3 MB/minute. How many more minutes will it take him to download the game?"""
    game_size = 880
    downloaded_size = 310
    full_speed = 2
    slow_speed = 3
    remaining_size = game_size - downloaded_size
    full_speed_time = (downloaded_size / full_speed)
    slow_speed_time = (remaining_size / slow_speed)
    total_time = full_speed_time + slow_speed_time
    result = total_time
    return result

print(solution())