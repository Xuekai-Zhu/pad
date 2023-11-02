def solution():
    """Roger uses his lunch break to walk the stairs in his office building. He can walk 2,000 steps in 30 minutes. If his daily goal is 10,000 steps, how many minutes will it take him to reach his goal?"""
    steps_per_30mins = 2000
    daily_goal = 10000
    mins_per_1000steps = 30 / 2000
    time_to_reach_goal = mins_per_1000steps * daily_goal
    result = time_to_reach_goal
    return result

print(solution())