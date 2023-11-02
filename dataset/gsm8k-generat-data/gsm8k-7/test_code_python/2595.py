def solution():
    goals_per_15min = 2
    num_quarters = 8  # 2 hours = 120 minutes, divided by 15 minute quarters
    total_goals = goals_per_15min * num_quarters

    # Calculate the average goals per minute
    avg_goals_per_minute = total_goals / 120

    result = avg_goals_per_minute
    return result

print(solution())