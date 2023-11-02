def solution():
    minutes_per_day = 8 + 3  # 8 minutes looking + 3 minutes complaining
    days_per_week = 7

    # Calculate the total time spent looking for keys and complaining per week
    total_time_per_week = minutes_per_day * days_per_week

    result = total_time_per_week
    return result

print(solution())