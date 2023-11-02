def solution():
    monthly_salary = 576
    num_hours_per_day = 8
    num_days_per_week = 6
    num_weeks_per_month = 4

    # Calculate the total number of hours Edric works per month
    total_hours = num_hours_per_day * num_days_per_week * num_weeks_per_month

    # Calculate Edric's hourly rate
    hourly_rate = monthly_salary / total_hours
    result = hourly_rate
    return result

print(solution())