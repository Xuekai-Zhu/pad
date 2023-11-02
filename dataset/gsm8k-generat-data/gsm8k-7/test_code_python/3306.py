def solution():
    time_per_day = 0.5  # 30 minutes is equal to 0.5 hours
    num_days_week1 = 3
    num_days_week2 = 5
    total_days = num_days_week1 + num_days_week2

    # Calculate the total time Larry jogs in two weeks
    total_time = total_days * time_per_day

    # Convert total time to hours
    total_time_hours = total_time

    result = total_time_hours
    return result

print(solution())