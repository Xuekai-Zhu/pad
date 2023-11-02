def solution():
    
    steps_per_30_min = 2000
    daily_goal = 10000
    time_to_reach_goal = (daily_goal / steps_per_30_min) * 30
    result = time_to_reach_goal
    return result

print(solution())