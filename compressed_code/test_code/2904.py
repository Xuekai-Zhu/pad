def solution():
    
    steps_per_30mins = 2000
    daily_goal = 10000
    mins_per_1000steps = 30 / 2000
    time_to_reach_goal = mins_per_1000steps * daily_goal
    result = time_to_reach_goal
    return result

print(solution())