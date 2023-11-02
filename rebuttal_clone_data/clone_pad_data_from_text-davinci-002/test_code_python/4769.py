def solution():
    series1 = 12
    series2 = 14
    episodes_per_season = 16
    episodes_lost = 2
    episodes_remaining1 = (series1 * episodes_per_season) - episodes_lost
    episodes_remaining2 = (series2 * episodes_per_season) - episodes_lost
    total_episodes_remaining = episodes_remaining1 + episodes_remaining2
    result = total_episodes_remaining
    
    return result

print(solution())