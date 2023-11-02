def solution():
    # Calculate the total number of episodes watched per week
    episodes_per_week = 1 + 2*2  # 1 episode every Monday and 2 episodes every Wednesday

    # Calculate the total number of weeks it will take to watch all the episodes
    total_weeks = 201 / episodes_per_week

    result = total_weeks
    return result

print(solution())