def solution():
    
    episodes_weekday = 8
    episodes_weekend = episodes_weekday * 3
    days_weekday = 5
    days_weekend = 2
    total_episodes = (episodes_weekday * days_weekday) + (episodes_weekend * days_weekend)
    result = total_episodes
    return result

print(solution())