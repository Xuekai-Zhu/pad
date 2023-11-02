def solution():
    
    season_length = 22
    last_season_length = 26
    num_seasons = 10
    total_episodes = (num_seasons - 1) * season_length + last_season_length
    episode_length = 0.5
    total_time = total_episodes * episode_length
    result = total_time
    return result

print(solution())