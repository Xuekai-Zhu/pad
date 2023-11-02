def solution():
    # Calculate the total hours trained in the first month
    hours_per_day = 5
    days_in_month = 30
    total_hours_month = hours_per_day * days_in_month

    # Calculate the total hours trained including the next 12 days
    remaining_days = 12
    total_hours = total_hours_month + (hours_per_day * remaining_days)

    result = total_hours
    return result

print(solution())