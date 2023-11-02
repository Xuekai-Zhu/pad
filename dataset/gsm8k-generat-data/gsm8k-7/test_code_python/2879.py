def solution():
    num_minutes_per_day = 6  # 2 minutes after breakfast, lunch, and dinner
    num_days = 30

    # Calculate the total number of minutes Malcolm spends brushing his teeth
    total_minutes = num_minutes_per_day * num_days

    # Convert minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())