def solution():
    # Calculate the total amount James makes in a week
    hourly_rate = 20
    hours_per_day = 8
    days_per_week = 4
    total_hours = hours_per_day * days_per_week
    total_amount = hourly_rate * total_hours
    result = total_amount
    return result

print(solution())