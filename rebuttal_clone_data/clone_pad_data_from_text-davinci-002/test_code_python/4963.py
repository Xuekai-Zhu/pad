def solution():
    cost_per_episode = 100000
    episodes_first_season = 12
    cost_first_season = cost_per_episode * episodes_first_season
    other_seasons = 5 - 1
    episodes_other_seasons = episodes_first_season * 1.5
    cost_other_seasons = cost_per_episode * 2 * episodes_other_seasons
    cost_last_season = cost_per_episode * 24
    total_cost = cost_first_season + cost_other_seasons + cost_last_season
    result = total_cost
    
    return result

print(solution())