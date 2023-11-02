def solution():
    time_meditating_per_day = 1
    time_reading_per_day = 2 * time_meditating_per_day
    days_per_week = 7

    # Calculate the total time Tim spends reading per week
    total_time_reading_per_week = days_per_week * time_reading_per_day

    result = total_time_reading_per_week
    return result

print(solution())