def solution():
    steps_per_minute = 2000 / 30  # Roger can walk 2,000 steps in 30 minutes
    daily_goal = 10000  # Roger's daily goal is 10,000 steps

    # Calculate the number of minutes it will take Roger to reach his daily goal
    minutes_to_reach_goal = (daily_goal / steps_per_minute)

    result = minutes_to_reach_goal
    return result

print(solution())