def solution():
    """Roger uses his lunch break to walk the stairs in his office building. He can walk 2,000 steps in 30 minutes. If his daily goal is 10,000 steps, how many minutes will it take him to reach his goal?"""
    # Define the number of steps Roger can walk in 1 minute
    steps_per_minute = 2000/30

    # Calculate how many minutes it will take Roger to reach his goal
    minutes_to_reach_goal = (10000/steps_per_minute)

    # return the result
    result = round(minutes_to_reach_goal)
    return result

print(solution())