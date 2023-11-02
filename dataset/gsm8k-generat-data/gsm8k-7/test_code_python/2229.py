def solution():
    hourly_rate = 2.0
    hours_per_day = 4.0
    days_per_week = 3.0
    weeks = 4.0

    # Calculate the total number of hours Zainab worked
    total_hours = hours_per_day * days_per_week * weeks

    # Calculate the total amount of money Zainab earned
    total_earned = total_hours * hourly_rate
    result = total_earned
    return result

print(solution())