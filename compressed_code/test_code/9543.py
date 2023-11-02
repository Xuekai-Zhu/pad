def solution():
    
    
    series1_seasons = 12
    series2_seasons = 14
    episodes_per_season = 16
    episodes_lost_per_season = 2
    
    total_episodes = (series1_seasons + series2_seasons) * episodes_per_season
    total_episodes_lost = (series1_seasons + series2_seasons) * episodes_lost_per_season
    episodes_remaining = total_episodes - total_episodes_lost
    
    result = episodes_remaining
    return result

print(solution())