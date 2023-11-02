def solution():
    
    episodes_this_week = 8
    mins_per_episode = 44
    mon_mins = 138
    thu_mins = 21
    fri_eps = 2
    fri_mins = fri_eps * mins_per_episode
    weekend_mins = (episodes_this_week * mins_per_episode) - mon_mins - thu_mins - fri_mins
    result = weekend_mins
    return result

print(solution())