def solution():
    num_days_per_week = 5
    num_hours_per_day = 1
    num_weeks = 8

    # Calculate the total number of hours Jane wants to exercise
    weekly_goal = num_days_per_week * num_hours_per_day

    # Calculate the total number of hours Jane actually exercises in 8 weeks
    total_hours = weekly_goal * num_weeks
    result = total_hours
    return result

print(solution())