def solution():
    steps_per_30_min = 2000
    daily_goal = 10000

    # Calculate the total number of steps Roger needs to walk
    total_steps = daily_goal

    # Calculate the total time it will take Roger to reach his goal
    total_time = (total_steps / steps_per_30_min) * 30
    result = total_time
    return result

print(solution())