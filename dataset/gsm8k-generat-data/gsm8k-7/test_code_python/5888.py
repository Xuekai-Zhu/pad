def solution():
    hourly_rate = 5
    hours_per_day = 8
    days_per_week = 6
    days_missed = 1

    # Calculate the total number of hours Julie works in a month
    total_hours = (hours_per_day * days_per_week * 4) - (hours_per_day * days_missed)

    # Calculate Julie's monthly salary
    monthly_salary = total_hours * hourly_rate
    result = monthly_salary
    return result

print(solution())