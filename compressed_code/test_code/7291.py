def solution():
    
    game_size = 880
    downloaded = 310
    remaining = game_size - downloaded
    download_rate = 3 
    time_remaining = remaining / download_rate
    result = time_remaining
    return result

print(solution())