def solution():
    hourly_rate = 10
    num_days_per_week = 2
    hours_per_day = 3
    num_weeks = 6

    # Calculate the total number of hours Jamie works
    total_hours = num_days_per_week * hours_per_day * num_weeks

    # Calculate Jamie's total earnings
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())