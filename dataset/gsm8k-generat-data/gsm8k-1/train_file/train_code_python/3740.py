def solution():
    """Roger uses his lunch break to walk the stairs in his office building. He can walk 2,000 steps in 30 minutes. If his daily goal is 10,000 steps, how many minutes will it take him to reach his goal?"""
    steps_per_30_min = 2000
    daily_goal = 10000
    time_to_reach_goal = (daily_goal / steps_per_30_min) * 30
    result = time_to_reach_goal
    return result

print(solution())