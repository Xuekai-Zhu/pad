def solution():
    
    total_seasons = 12
    episodes_per_season = 20
    total_episodes = total_seasons * episodes_per_season
    watched_episodes = total_episodes / 3
    remaining_episodes = total_episodes - watched_episodes
    result = remaining_episodes
    return result

print(solution())