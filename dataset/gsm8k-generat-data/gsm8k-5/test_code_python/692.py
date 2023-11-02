def solution():
    monthly_salary = 576  # Edric's monthly salary is $576
    days_per_week = 6  # Edric works 6 days per week
    hours_per_day = 8  # Edric works 8 hours per day

    # Calculate the total number of hours Edric works in a month
    total_hours = days_per_week * hours_per_day * 4  # 4 weeks in a month

    # Calculate Edric's hourly rate
    hourly_rate = monthly_salary / total_hours
    result = hourly_rate
    return result

print(solution())