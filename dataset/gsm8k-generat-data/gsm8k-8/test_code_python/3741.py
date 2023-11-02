def solution():
    # Calculate the number of steps he can walk in one minute
    steps_per_minute = 2000 / 30

    # Calculate how many minutes it will take him to reach his goal
    minutes_to_reach_goal = (10000 - steps_per_minute) / steps_per_minute

    result = minutes_to_reach_goal
    return result

print(solution())